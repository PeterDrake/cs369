# Adapted (hastily!) from https://github.com/PeterDrake/sky/blob/summer-2023/src/ManualGlareRemover.py

import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import glob
import numpy as np
from skimage.morphology import flood_fill


def load_photo(path):
    photo = Image.open(path)
    a = np.array(photo)
    a[np.isnan(a)] = np.nanmin(a)
    a = 191 * (a - np.nanmin(a)) / (np.nanmax(a) - np.nanmin(a))  # Range 0-255
    a = a.astype(np.uint8)
    return a


class LidarTagger:
    """
    Tool for manually tagging buildings in forest LiDAR data.
    """

    FOOTPRINT = np.ones((3, 3))  # Neighborhood for flood fill

    def __init__(self, root_, data_dir, save_dir, tiles_to_process):
        """
        :param root_: Tk window within which the GUI appears
        :param data_dir: Directory containing the chm files
        :param tiles_to_process: List of tile numbers
        """
        self.root = root_
        self.data_dir = data_dir
        self.tiles_to_process = tiles_to_process
        self.save_dir = save_dir
        self.root.title('LiDAR Tagger')
        self.top_frame = Frame(root, width=1000, height=1000)
        self.top_frame.grid(row=0, column=0)
        self.bottom_frame = Frame(root, width=1000, height=120)
        self.bottom_frame.grid(row=1, column = 0)
        self.photo = None
        self.photo_array = None
        self.photo_canvas = None
        self.photo_canvas_image_id = None
        self.tag_label = None
        self.undo_button = None
        self.prev_button = None
        self.next_button = None
        self.save_button = None
        self.histories = [[] for _ in tiles_to_process]
        self.timestamps_to_process = list(tiles_to_process)
        self.timestamp_index = 0  # Index into timestamps_to_process
        self.timestamp = None
        self.load_images()
        self.layout()

    def layout(self):
        # Clear out existing elements
        if self.photo_canvas:  # Either all or none of them should exist, so checking one suffices
            self.photo_canvas.destroy()
            self.tag_label.destroy()
            self.undo_button.destroy()
            self.prev_button.destroy()
            self.next_button.destroy()
            self.save_button.destroy()
        # Title
        # Note that, since load_images has been called, self.timestamp_index holds the 0-based index
        # of the NEXT image to be edited. We display that anyway as it is also the 1-based index
        # of the image currently being edited.
        self.root.title(f'LiDAR Tagger: {self.timestamp} ({self.timestamp_index}/{len(self.timestamps_to_process)})')
        # Photo
        self.photo_canvas = Canvas(self.top_frame, width=1000, height=1000)
        self.photo_canvas_image_id = self.photo_canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.photo_canvas.pack(side='left')
        self.photo_canvas.bind('<Button-1>', self.click)
        self.root.bind('<Key>', self.key_pressed)
        # Labels
        self.tag_label = Label(self.bottom_frame, text="Tag structure\n(click)")
        self.tag_label.grid(row=0, column=0, padx=10)
        self.undo_button = Button(self.bottom_frame, text="Undo\n(backspace)", command=self.undo)
        self.undo_button.grid(row=0, column=1)
        self.prev_button = Button(self.bottom_frame, text="Prev\n(<)", command=self.prev)
        self.prev_button.grid(row=0, column=2)
        if self.timestamp_index == 1:
            self.prev_button['state'] = DISABLED
        self.next_button = Button(self.bottom_frame, text="Next\n(>)", command=self.next)
        self.next_button.grid(row=0, column=3)
        self.save_button = Button(self.bottom_frame, text="Save all\n(enter)", command=self.save)
        self.save_button.grid(row=0, column=4)
        if self.timestamp_index == len(self.timestamps_to_process):
            self.next_button['state'] = DISABLED
        else:
            self.save_button['state'] = DISABLED

    def load_images(self):
        self.timestamp = self.timestamps_to_process[self.timestamp_index]
        self.timestamp_index += 1
        if self.histories[self.timestamp_index - 1]:
            self.photo_array = self.histories[self.timestamp_index - 1].pop()
        else:
            self.photo_array = load_photo(self.photo_path())
        self.photo = ImageTk.PhotoImage(Image.fromarray(self.photo_array))



    def photo_path(self):
        return glob.glob(f'{self.data_dir}/chm_tile_{self.timestamp}*tif')[0]

    def click(self, event):
        self.histories[self.timestamp_index - 1].append(self.photo_array)
        self.photo_array = self.photo_array.copy()
        self.photo_array[event.y, event.x] = 255  # Full white indicates a tagged structure
        self.photo_array = flood_fill(self.photo_array,
                                      (event.y, event.x),
                                      255,
                                      tolerance=230,
                                      footprint=LidarTagger.FOOTPRINT)
        self.update_photo()

    def update_photo(self):
        self.photo = ImageTk.PhotoImage(Image.fromarray(self.photo_array))
        self.photo_canvas.itemconfig(self.photo_canvas_image_id, image=self.photo)

    def undo(self):
        if self.histories[self.timestamp_index - 1]:
            self.photo_array = self.histories[self.timestamp_index - 1].pop()
            self.update_photo()

    def prev(self):
        self.timestamp_index -= 2
        self.next()

    def next(self):
        self.histories[self.timestamp_index - 1].append(self.photo_array)
        self.load_images()
        self.layout()

    def save(self):
        self.histories[self.timestamp_index - 1].append(self.photo_array)
        for i, h in enumerate(self.histories):
            path = f'{self.save_dir}/tile_{self.tiles_to_process[i]}_tag.npy'
            a = (h[-1] == 255).astype(np.float32)  # Ignore the warning; a is a NumPy array of bools
            np.save(path, a)
        if tkinter.messagebox.askyesno('Finished', 'Files saved. Quit?'):
            self.root.destroy()

    def key_pressed(self, event):
        if event.keysym in ['comma', 'less', 'Left']:
            if self.prev_button['state'] == NORMAL:
                self.prev()
        elif event.keysym in ['period', 'greater', 'Right']:
            if self.next_button['state'] == NORMAL:
                self.next()
        elif event.keysym == 'Return':
            if self.next_button['state'] == DISABLED:  # Because you're looking at the last image
                self.save()
        elif event.keysym == 'BackSpace':
            self.undo()
        else:
            print('Unknown key pressed: <' + event.keysym + '>')

if __name__ == "__main__":
    root = Tk()
    app = LidarTagger(root, '../lidar_chm', '../lidar_tag', [800, 801, 842, 843, 844, 845, 846, 847, 886, 887, 888, 889, 890, 891])
    root.mainloop()
