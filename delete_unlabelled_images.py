import os

# Directories for images and labels
images_dir = r"D:\coco\Datasets\goat_final\train\images"
labels_dir = r"D:\coco\Datasets\goat_final\train\labels"  # Replace with your label directory

# Get the list of image files (assuming they are .jpg or .png)
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]

# Get the list of label files (assuming they are .txt)
label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

# Extract the base names (without extension) of images and labels
image_bases = {os.path.splitext(f)[0] for f in image_files}
label_bases = {os.path.splitext(f)[0] for f in label_files}

# Find images that do not have corresponding labels
missing_labels = image_bases - label_bases

# Delete missing images
for missing in missing_labels:
    image_path = os.path.join(images_dir, f"{missing}.jpg")  # Change extension if necessary
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Deleted image: {missing}.jpg")

print(f"Total images deleted: {len(missing_labels)}")
