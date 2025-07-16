import os

# Define dataset directory
dataset_dir = r"D:\coco\Datasets\coco_final"

# Define subfolders to check
subfolders = ["train", "test", "valid"]

# Supported image extensions
image_extensions = [".jpg", ".png", ".jpeg"]

# Store empty labels
empty_labels = []

for subfolder in subfolders:
    labels_dir = os.path.join(dataset_dir, subfolder, "labels")
    images_dir = os.path.join(dataset_dir, subfolder, "images")

    # Skip if labels or images folder doesn't exist
    if not os.path.exists(labels_dir) or not os.path.exists(images_dir):
        print(f"⚠ Skipping {subfolder} as labels or images folder is missing.")
        continue

    for label_file in os.listdir(labels_dir):
        label_path = os.path.join(labels_dir, label_file)

        # Check if label file is empty
        if os.path.isfile(label_path) and os.stat(label_path).st_size == 0:
            empty_labels.append(label_path)

# Print found empty labels
if empty_labels:
    print("\n🚨 Found {} empty label files:".format(len(empty_labels)))
    for label in empty_labels:
        print(f"   - {label}")

    # Ask for user confirmation
    confirm = input("\n❗ Do you want to delete all empty labels and their corresponding images? (yes/no): ").strip().lower()

    if confirm == "yes":
        deleted_files = []
        for label_path in empty_labels:
            label_name = os.path.basename(label_path)
            image_name = os.path.splitext(label_name)[0]  # Get corresponding image name

            # Delete label file
            os.remove(label_path)
            deleted_files.append(label_path)

            # Check and delete corresponding images
            images_dir = os.path.dirname(label_path).replace("labels", "images")
            for ext in image_extensions:
                image_path = os.path.join(images_dir, image_name + ext)
                if os.path.exists(image_path):
                    os.remove(image_path)
                    deleted_files.append(image_path)

        print("\n✅ Deleted the following files:")
        for file in deleted_files:
            print(f"   - {file}")

    else:
        print("\n❌ Deletion cancelled. No files were deleted.")

else:
    print("\n✅ No empty label files found!")
