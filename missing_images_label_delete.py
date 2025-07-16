import os

# Paths to the image and label directories
images_path = r"D:\coco\Datasets\Datasetsmerged_final\train\images"
labels_path = r"D:\coco\Datasets\Datasetsmerged_final\train\labels"

# Initialize a list to track missing labels
missing_labels = []

# Get the list of image and label filenames (without extensions)
image_files = [os.path.splitext(f)[0] for f in os.listdir(images_path) if f.endswith(('.jpg', '.png'))]
label_files = [os.path.splitext(f)[0] for f in os.listdir(labels_path) if f.endswith('.txt')]

# Check for images with no corresponding labels
for image in image_files:
    if image not in label_files:
        missing_labels.append(image)

# Delete images with no corresponding labels
for image in missing_labels:
    image_file_path = os.path.join(images_path, image + ".jpg")  # Assuming images are in .jpg format
    if not os.path.exists(image_file_path):
        image_file_path = os.path.join(images_path, image + ".png")  # Check for .png format if .jpg is not found
    if os.path.exists(image_file_path):
        os.remove(image_file_path)
        print(f"Deleted: {image_file_path}")
    else:
        print(f"Image file not found: {image_file_path}")

print("\nProcess complete. Images without labels have been deleted.")
