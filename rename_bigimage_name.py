import os

# Replace with the paths to your image and label folders
image_folder = r"D:\coco\Datasets\Cow Breed Dataset.v1i.yolov8\test\images"
label_folder = r"D:\coco\Datasets\Cow Breed Dataset.v1i.yolov8\test\labels"

# Specify the file extensions
image_extension = ".jpg"  # Change if needed
label_extension = ".txt"

# Create a mapping dictionary to track old and new names
name_mapping = {}

# Rename image files
print("Renaming images...")
for i, filename in enumerate(os.listdir(image_folder), start=1):
    old_image_path = os.path.join(image_folder, filename)
    new_image_name = f"{i}{image_extension}"
    new_image_path = os.path.join(image_folder, new_image_name)

    # Rename the file if it's an image
    if filename.endswith(image_extension):
        os.rename(old_image_path, new_image_path)
        name_mapping[filename] = new_image_name
        print(f"Renamed: {filename} -> {new_image_name}")

# Rename label files based on corresponding images
print("\nRenaming labels...")
for old_name, new_name in name_mapping.items():
    old_label_path = os.path.join(label_folder, old_name.replace(image_extension, label_extension))
    new_label_path = os.path.join(label_folder, new_name.replace(image_extension, label_extension))

    # Rename the label file if it exists
    if os.path.exists(old_label_path):
        os.rename(old_label_path, new_label_path)
        print(f"Renamed label: {old_name.replace(image_extension, label_extension)} -> {new_name.replace(image_extension, label_extension)}")
    else:
        print(f"Label not found for: {old_name}")

# Save the mapping to a file for reference
mapping_file = os.path.join(image_folder, "name_mapping.txt")
with open(mapping_file, "w") as f:
    for old_name, new_name in name_mapping.items():
        f.write(f"{old_name} -> {new_name}\n")

print("\nRenaming complete. Mapping saved to 'name_mapping.txt'.")
