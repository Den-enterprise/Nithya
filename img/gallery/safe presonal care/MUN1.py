import os

folder_path = os.path.dirname(os.path.realpath(__file__))  # Set the folder path to the script's directory
new_name_base = 'SAR'

# List all files in the folder
files = os.listdir(folder_path)

# Sort the files to ensure consistent numbering
files.sort()

# Initialize a counter for numbering
counter = 1

# Loop through the files and rename them
for file in files:
    if os.path.isfile(os.path.join(folder_path, file)):
        file_extension = os.path.splitext(file)[1]
        new_name = new_name_base + str(counter) + file_extension
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        counter += 1
