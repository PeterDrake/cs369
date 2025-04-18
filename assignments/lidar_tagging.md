# Overview

Before we can start building neural networks to solve the forest LiDAR problem, we need some tagged data. This assignment will have you looking at height maps and manually tagging buildings. It's not hard work, but there's a lot of it, so I'm crowdsourcing it to the class.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Files
* [Data description](data_description.docx)
* [Signup spreadsheet](https://docs.google.com/spreadsheets/d/1Xulf1-Q6VTSGQ8BqfsmqEbjTy_J95VykzYyPSeMKTuM/edit?usp=sharing)
* [Data folder](https://drive.google.com/drive/folders/1N_Ag6yqq3T26v09aToYpgk1KJg_GjExT)
* [`lidar_tagger.py`](../src/lidar_tagger.py)

# Setup procedure
* Put `lidar_tagger.py` in your `src` folder.
* Download the `chm` folder from the data folder. Put it in your project, as a folder `lidar_chm`, at the same level as (not inside) `src`.
* Create an empty folder called `lidar_tag`, also at the same level as `src`.

# Procedure for Each Batch
1. In the spreadsheet, pick a batch and put your name on it. This will ensure that two people aren't tagging the same data.
2. Edit `lidar_tagger.py` (near the end of the file, on the line beggining `app = LidarTagger(...`) with the list of numbers of the tiles you'll be tagging.
3. Run `lidar_tagger`.
   1. You may need to increase your monitor's resolution to fit the whole window on the screen.
   2. For each image, click on each thing that is clearly a building. Some images won't have any. If you make a mistake, you can undo. It doesn't have to be perfect, but do your best; the more accurate our training data are, the better the networks will be able to do.
   3. After you're processed the images, save them. This will save some .npy files in your `lidar_tag`
4. Using sftp, upload the files to BLT in the directory `/home/drake/lidar/lidar_tag`
5. Mark in the signup spreadsheet that you're done.

# Optional Challenge Problems
Tag more sets of data!

# What to Hand in
There's nothing to hand in on Google Classroom; just upload the files and mark them done in the spreadsheet.
