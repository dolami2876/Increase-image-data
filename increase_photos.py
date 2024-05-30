from PIL import Image, ImageOps
import numpy as np
import os

def convert_to_rgb(image):
    if image.mode == 'RGBA':
        return image.convert('RGB')
    return image

def augment_image(image, base_name, output_dir, num_augmentations=5):
    image = convert_to_rgb(image)
    # Save original image
    image.save(os.path.join(output_dir, f"{base_name}_original.jpg"))
    
    # Flip the image horizontally
    flipped_image = ImageOps.mirror(image)
    flipped_image.save(os.path.join(output_dir, f"{base_name}_flipped.jpg"))
    
    # Rotate the image by 90, 180, and 270 degrees
    for angle in [90, 180, 270]:
        rotated_image = image.rotate(angle)
        rotated_image.save(os.path.join(output_dir, f"{base_name}_rotated_{angle}.jpg"))
    
    # Randomly crop the image
    width, height = image.size
    for i in range(num_augmentations):
        left = np.random.randint(0, width // 4)
        top = np.random.randint(0, height // 4)
        right = np.random.randint(3 * width // 4, width)
        bottom = np.random.randint(3 * height // 4, height)
        
        cropped_image = image.crop((left, top, right, bottom))
        cropped_image = cropped_image.resize((width, height), Image.Resampling.LANCZOS)
        cropped_image.save(os.path.join(output_dir, f"{base_name}_crop_{i}.jpg"))

def augment_images_in_folder(input_folder, output_folder, num_augmentations=5):
    # Create the output directory if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            base_name = os.path.basename(filename).split('.')[0]
            augment_image(image, base_name, output_folder, num_augmentations)

# Example usage
input_folder = "Sparkle"  # Replace with the path to your input folder
output_folder = "Output"  # Replace with the path to your output folder
num_augmentations = 15  # Number of augmentations to perform on each image
augment_images_in_folder(input_folder, output_folder, num_augmentations)
