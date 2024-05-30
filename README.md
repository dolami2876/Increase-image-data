# Image Augmentation Script

This script is designed to augment images by performing various transformations such as flipping, rotating, and random cropping. The script reads all images from a specified input folder, performs the augmentations, and saves the augmented images to a specified output folder. Additionally, it can be configured to produce a specified number of augmented images per original image.

## Features
Flips images horizontally.
Rotates images by 90, 180, and 270 degrees.
Randomly crops images and resizes them to the original dimensions.
Handles all images in a specified input folder.

## Ensure Pillow is installed:
[ pip install --upgrade pillow ]

## Run the Script:
Adjust the input_folder, output_folder, and num_augmentations variables as needed, then run the script to perform the augmentations.

--------------------------------------------------

# Image Rename Script
This script is designed to rename all images in a specified folder according to a sequential numbering scheme. It ensures that all images are renamed with a consistent prefix followed by a unique number.

## Features
Renames images in a folder with a specified prefix followed by an incrementing number.
Handles various image formats such as .png, .jpg, and .jpeg.

## Run the Script:
Set the folder_path variable to the path of your folder containing the images and optionally adjust the prefix. Then, run the script to rename all images in the folder.
