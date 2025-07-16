import os

# Define paths to the image and label folders
image_folder = r"D:\coco\Datasets\Final_Merged_Dataset\train\images"
label_folder = r"D:\coco\Datasets\Final_Merged_Dataset\train\labels"

# Get a list of all image and label filenames
image_files = set(os.listdir(image_folder))
label_files = set(os.listdir(label_folder))

# Remove file extensions to compare just the base names
image_base_names = {os.path.splitext(image)[0] for image in image_files}
label_base_names = {os.path.splitext(label)[0] for label in label_files}

# Find images without corresponding labels
images_without_labels = image_base_names - label_base_names

# Remove the images without labels
for image_base_name in images_without_labels:
    image_path = os.path.join(image_folder, f"{image_base_name}.jpg")  # Update extension if not .jpg
    if os.path.exists(image_path):
        os.remove(image_path)

print(f"Removed {len(images_without_labels)} images without corresponding labels.")
