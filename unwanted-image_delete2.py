import os

# Replace with the paths to your image and label folders
image_folder = r"D:\coco\Datasets\bull_final\train\images"
label_folder = r"D:\coco\Datasets\bull_final\train\labels"

# Specify the range of files to delete (inclusive)
start_number = 13
end_number =  15
# Generate the list of filenames within the specified range
files_to_delete = [str(i) for i in range(start_number, end_number + 1)]

# Counters for tracking deletions
images_deleted = 0
labels_deleted = 0

# Iterate through the list and delete corresponding images and labels
for file_name in files_to_delete:
    # Construct file paths for the image and label
    image_file = os.path.join(image_folder, f"{file_name}.jpg")  # Adjust if using another image format
    label_file = os.path.join(label_folder, f"{file_name}.txt")  # Adjust if using another label format

    # Delete the image file
    if os.path.exists(image_file):
        os.remove(image_file)
        images_deleted += 1
        print(f"Deleted image: {image_file}")
    else:
        print(f"Image not found: {image_file}")

    # Delete the label file
    if os.path.exists(label_file):
        os.remove(label_file)
        labels_deleted += 1
        print(f"Deleted label: {label_file}")
    else:
        print(f"Label not found: {label_file}")

# Display the totals
print("\nSummary:")
print(f"Total images deleted: {images_deleted}")
print(f"Total labels deleted: {labels_deleted}")
