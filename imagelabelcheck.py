import os

# Paths to the images and labels directories
images_path = "D:/coco/Datasets/Coco_datase_final/train/images"
labels_path = "D:/coco/Datasets/Coco_datase_final/train/labels"

# List to hold orphaned image files (images without corresponding labels)
orphaned_images = []

# Check for orphaned images
for image_file in os.listdir(images_path):
    # Get the corresponding label file (same name but with .txt extension)
    label_file = os.path.join(labels_path, os.path.splitext(image_file)[0] + ".txt")

    # If the label file does not exist, consider the image orphaned
    if not os.path.exists(label_file):
        orphaned_images.append(image_file)

# Output the result
if orphaned_images:
    print("Orphaned images found (without corresponding labels):")
    for img in orphaned_images:
        print(img)
else:
    print("No orphaned images found.")
