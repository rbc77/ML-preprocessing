import os
import zipfile

def extract_all_zips_in_folder(main_folder):
    """
    Extracts all zip files inside the given folder.
    Each zip file will be extracted into a subfolder with the same name as the zip file (without the .zip extension).

    Args:
        main_folder (str): Path to the folder containing the zip files.
    """
    # Iterate through all files in the main folder
    for filename in os.listdir(main_folder):
        # Check if the file is a zip file
        if filename.endswith('.zip'):
            zip_path = os.path.join(main_folder, filename)
            extract_folder = os.path.join(main_folder, os.path.splitext(filename)[0])  # Folder name = zip file name

            # Create a directory for the extracted content if it doesn't exist
            os.makedirs(extract_folder, exist_ok=True)

            # Extract the zip file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
                print(f"Extracted {filename} into {extract_folder}")

# Specify the path to the `datasets` folder
datasets_folder = r"D:\coco\datasets"

# Extract all zip files in the `datasets` folder
extract_all_zips_in_folder(datasets_folder)
