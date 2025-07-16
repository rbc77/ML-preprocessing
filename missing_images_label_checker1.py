import os

# Paths to the image and label directories
images_path = r"D:\coco\Datasets\Datasetsmerged_final\train\images"
labels_path = r"D:\coco\Datasets\Datasetsmerged_final\train\labels"

# Initialize lists to track missing labels and images
missing_labels = []
missing_images = []

# Get the list of image and label filenames (without extensions)
image_files = [os.path.splitext(f)[0].lower() for f in os.listdir(images_path) if f.lower().endswith(('.jpg', '.png'))]
label_files = [os.path.splitext(f)[0].lower() for f in os.listdir(labels_path) if f.lower().endswith('.txt')]

# Check for missing labels
for image in image_files:
    if image not in label_files:
        missing_labels.append(image)

# Check for missing images
for label in label_files:
    if label not in image_files:
        missing_images.append(label)

# Print limited results for readability
print("Missing Labels (Images with no corresponding labels):")
print("\n".join(missing_labels[:10]))
if len(missing_labels) > 10:
    print(f"...and {len(missing_labels) - 10} more")

print("\nMissing Images (Labels with no corresponding images):")
print("\n".join(missing_images[:10]))
if len(missing_images) > 10:
    print(f"...and {len(missing_images) - 10} more")

# Save the full results to files
with open("missing_labels.txt", "w") as labels_report:
    labels_report.write("\n".join(missing_labels))

with open("missing_images.txt", "w") as images_report:
    images_report.write("\n".join(missing_images))

print("\nReports saved: 'missing_labels.txt' and 'missing_images.txt'")
