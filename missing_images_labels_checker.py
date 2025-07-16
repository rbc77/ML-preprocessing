import os

# Paths to the image and label directories
images_path = r"D:\coco\Datasets\Datasetsmerged_final\train\images"
labels_path = r"D:\coco\Datasets\Datasetsmerged_final\train\labels"

# Initialize lists to track missing labels and images
missing_labels = []
missing_images = []

# Get the list of image and label filenames (without extensions)
image_files = [os.path.splitext(f)[0] for f in os.listdir(images_path) if f.endswith(('.jpg', '.png'))]
label_files = [os.path.splitext(f)[0] for f in os.listdir(labels_path) if f.endswith('.txt')]

# Check for missing labels
for image in image_files:
    if image not in label_files:
        missing_labels.append(image)

# Check for missing images
for label in label_files:
    if label not in image_files:
        missing_images.append(label)

# Print results
print("Missing Labels (Images with no corresponding labels):")
for img in missing_labels:
    print(f"Image: {img}")

print("\nMissing Images (Labels with no corresponding images):")
for lbl in missing_images:
    print(f"Label: {lbl}")

# Optional: Save the results to a file
with open("missing_files_report.txt", "w") as report:
    report.write("Missing Labels (Images with no corresponding labels):\n")
    report.write("\n".join(missing_labels) + "\n")
    report.write("\nMissing Images (Labels with no corresponding images):\n")
    report.write("\n".join(missing_images) + "\n")
