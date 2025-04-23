# from tf_keras.layers import Conv2D, MaxPool2D
# from tf_keras import Input, Model
# NOTE: If running on your local machine instead of BLT, comment out the two lines below and uncomment the two above.
from tensorflow.keras.layers import Conv2D, MaxPool2D
from tensorflow.keras import Input, Model

from tensorflow.nn import weighted_cross_entropy_with_logits
from functools import partial
from random import shuffle, seed
from BatchGenerator import BatchGenerator
import numpy as np

# Weirdly, this can be much higher running on my laptop than on BLT. It may have to do with the GPUs.
BATCH_SIZE = 1

# Load data
tiles = [31, 32, 33, 34, 35, 77, 78, 79, 80, 81, 110, 111, 125, 126, 156, 157, 171, 172, 202, 203, 217, 218, 248, 249, 250, 262, 263, 264, 295, 296, 308, 309, 310, 341, 342, 353, 354, 355, 356, 357, 358, 366, 367, 387, 388, 389, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 413, 433, 434, 435, 436, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 480, 481, 482, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 617, 618, 619, 620, 621, 622, 623, 624, 662, 663, 664, 665, 666, 667, 707, 708, 709, 710, 711, 753, 754, 755, 756, 797, 798, 799, 800, 801, 842, 843, 844, 845, 846, 847, 886, 887, 888, 889, 890, 891, 931, 932, 933, 934, 935, 936, 976, 977, 978, 979, 980, 981, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1059, 1060, 1067, 1068, 1069, 1070, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1244, 1245, 1246, 1290, 1291, 1292]
seed(0)
shuffle(tiles)

# Break into training, validation, and testing sets
n = len(tiles)
train_tiles = tiles[:int(n * 0.6)]
valid_tiles = tiles[int(n * 0.6):int(n * 0.8)]
test_tiles = tiles[int(n * 0.8):]

# Create generators
train_gen = BatchGenerator(train_tiles, '/home/drake/lidar/lidar_chm', '/home/drake/lidar/lidar_tag', batch_size=BATCH_SIZE)
valid_gen = BatchGenerator(valid_tiles, '/home/drake/lidar/lidar_chm', '/home/drake/lidar/lidar_tag', batch_size=BATCH_SIZE)

# Define model
# TODO You have to define your model!

# Compile model
def weighted_loss(a, b):
    return weighted_cross_entropy_with_logits(a, b, pos_weight=50)

model.compile(optimizer='adam', loss=weighted_loss, metrics=['accuracy'])

# Train model
print('\nTRAINING')
history = model.fit(train_gen, epochs=20, validation_data=valid_gen, verbose=2)

# Test model
# Uncomment this if you are done tweaking parameters and want to see how accurate your model is
# print('\nTESTING')
# test_gen = BatchGenerator(test_tiles, '/home/drake/lidar/lidar_chm', '/home/drake/lidar/lidar_tag', batch_size=BATCH_SIZE)
# model.evaluate(test_gen)

# Count portions of tagged pixels in correct and predicted test images
valid_gen = BatchGenerator(valid_tiles, '/home/drake/lidar/lidar_chm', '/home/drake/lidar/lidar_tag', batch_size=BATCH_SIZE)
i = 0
for chm, tag in valid_gen:
    if chm.size == 0:  # For some reason we get an empty image for the last batch
        break
    predict = model.predict(chm, verbose=0) > 0.5
    print(f'\nBatch {i}: {np.sum(predict)} predicted, {np.sum(tag)} actual')
    i += 1

# Old code I was using to display images. As it is won't run on BLT because BLT has no GUI.
# import matplotlib
# matplotlib.use('TkAgg')
# print(train_tiles)
# train_gen = BatchGenerator(train_tiles, '../lidar_chm', '../lidar_tag', batch_size=BATCH_SIZE, scale_factor=1)
# chm, tag = train_gen.__getitem__(0)
# i = 4
# plt.imshow(chm[i])
# plt.show()
# plt.imshow(predict[i])
# plt.show()