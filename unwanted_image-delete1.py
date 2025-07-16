import os

# Replace with the paths to your image and label folders
image_folder = r"D:\coco\Datasets\bull_final\valid\images"
label_folder = r"D:\coco\Datasets\bull_final\valid\labels"

# List of files (without extensions) you want to delete
files_to_delete = [ 1389                                                                                                                                             ]

# Iterate through the list and delete corresponding images and labels
for file_name in files_to_delete:
    # Construct file paths for the image and label
    image_file = os.path.join(image_folder, f"{file_name}.jpg")  # Adjust if using another image format
    label_file = os.path.join(label_folder, f"{file_name}.txt")  # Adjust if using another label format

    # Delete the image file
    if os.path.exists(image_file):
        os.remove(image_file)
        print(f"Deleted image: {image_file}")
    else:
        print(f"Image not found: {image_file}")

    # Delete the label file
    if os.path.exists(label_file):
        os.remove(label_file)
        print(f"Deleted label: {label_file}")
    else:
        print(f"Label not found: {label_file}")

print("Selected images and labels deleted successfully!")
