import os

def rename_images_in_folder(folder_path, prefix="image"):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out only image files (e.g., .png, .jpg, .jpeg)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    # Sort the image files to ensure a consistent order
    image_files.sort()
    
    # Rename each image file
    for index, filename in enumerate(image_files):
        # Construct the new file name
        new_name = f"{prefix}_{index + 1}.jpg"  # Change extension as needed
        
        # Get the full file paths
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} -> {new_file_path}")

# Example usage
folder_path = "Output"  # Replace with the path to your folder
rename_images_in_folder(folder_path)
