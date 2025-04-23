# Adapted (hastily!) from https://github.com/PeterDrake/sky/blob/master/src/BatchGenerator.py

# from tf_keras.utils import Sequence
# NOTE: If running on your local machine instead of BLT, comment out the line below and uncomment the one above.
from tensorflow.keras.utils import Sequence

import tensorflow as tf
import numpy as np
import glob
from PIL import Image


def load_photo(path):
    photo = Image.open(path)
    a = np.array(photo)
    a[np.isnan(a)] = np.nanmin(a)
    a = 191 * (a - np.nanmin(a)) / (np.nanmax(a) - np.nanmin(a))  # Range 0-255
    a = a.astype(np.uint8)
    return a

class BatchGenerator(Sequence):
    """Loads batches of data (each batch as an Nx1000x1000 numpy array) for network training."""

    def __init__(self, tiles, chm_dir, tag_dir, batch_size=32):
        """
        :param tiles: List of tile numbers for the data to be put into batches.
        :param chm_dir: Directory where chm images live.
        :param tag_dir: Directory where the tagged numpy arrays live.
        :param batch_size: Number of images in each batch.
        """
        self.tiles = tiles
        self.chm_dir = chm_dir
        self.tag_dir = tag_dir
        self.batch_size = batch_size

    def __len__(self):
        """
        Returns number of batches (not number of images) in the data rounded up.
        Since Python does not have a ceiling division function, we use floor division on negative values.
        https://newbedev.com/is-there-a-ceiling-equivalent-of-operator-in-python
        """
        return -(-len(self.tiles) // self.batch_size)

    def __getitem__(self, index):
        """
        Returns tuple (photos, labeled TSI masks) corresponding to batch #index.
        Dimension of chm_batch is (batch_size x 1000 x 1000).
        Dimension of tag_batch is (batch_size x 1000 x 1000).
        """
        i = index * self.batch_size  # Index of the beginning of the batch
        batch_tile_names = self.tiles[i : i + self.batch_size]  # Tile numbers for this batch
        n = len(batch_tile_names)
        chm_paths = [glob.glob(f'{self.chm_dir}/chm_tile_{t}*tif')[0] for t in batch_tile_names]
        tag_paths = [f'{self.tag_dir}/tile_{t}_tag.npy' for t in batch_tile_names]
        chm_batch = np.zeros((n, 1000, 1000), dtype="uint8")  # Shape (N, 1000, 1000)
        for j, path in enumerate(chm_paths):
            chm_batch[j] = load_photo(path)  # Shape (1000, 1000)
        tag_batch = np.zeros((n, 1000, 1000), dtype="float32")  # Shape (N, 1000, 1000)
        for j, path in enumerate(tag_paths):
            tag_batch[j] = np.load(path)  # Shape (1000, 1000)
        return chm_batch, tag_batch

tf.random.set_seed(0)
