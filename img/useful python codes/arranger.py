import os
from PIL import Image  # Make sure to install the Pillow library for image processing

def is_image_file(filename):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def rename_images():
    folder_path = '.'  # Current directory, change this if your files are in a different folder
    files = os.listdir(folder_path)

    # Filter out only image files
    image_files = [file for file in files if is_image_file(file)]

    # Sort the image files to ensure consistent numbering
    image_files.sort()

    for i, file in enumerate(image_files, start=1):
        # Form the new name for the image file
        new_name = f'draw-{i}{os.path.splitext(file)[1]}'

        # Construct the full paths for the old and new names
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        # Rename the image file
        os.rename(old_path, new_path)

        print(f'Renamed: {file} -> {new_name}')

if __name__ == "__main__":
    rename_images()
