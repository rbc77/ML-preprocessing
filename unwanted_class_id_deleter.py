import os

def process_labels_and_images(labels_dir, images_dir, unwanted_classes):
    """
    Removes unwanted class IDs from label files and deletes empty labels and corresponding images.

    Args:
        labels_dir (str): Path to the labels folder.
        images_dir (str): Path to the images folder.
        unwanted_classes (list): List of class IDs to be removed.
    """
    label_files = [f for f in os.listdir(labels_dir) if f.endswith(".txt")]
    total_deleted = 0  # Counter for deleted label-image pairs
    total_updated = 0  # Counter for updated label files

    for label_file in label_files:
        label_path = os.path.join(labels_dir, label_file)
        image_path = os.path.join(images_dir, label_file.replace(".txt", ".jpg"))  # Assuming images are .jpg

        # Read the label file
        with open(label_path, "r") as file:
            lines = file.readlines()

        # Filter out the lines corresponding to unwanted classes
        updated_lines = []
        for line in lines:
            class_id = int(line.split()[0])  # The first value in each line is the class ID
            if class_id not in unwanted_classes:
                updated_lines.append(line)  # Keep lines with valid class IDs

        # If no valid classes are left, delete the label file and its corresponding image
        if not updated_lines:
            os.remove(label_path)  # Delete the label file
            if os.path.exists(image_path):
                os.remove(image_path)  # Delete the image file if it exists
            total_deleted += 1
            print(f"Deleted: {label_path} and {image_path}")
        else:
            # If valid classes are left, update the label file
            if len(updated_lines) < len(lines):
                with open(label_path, "w") as file:
                    file.writelines(updated_lines)  # Write the updated lines back to the file
                total_updated += 1
                print(f"Updated: {label_path} (removed unwanted classes)")

    print(f"Total label-image pairs deleted: {total_deleted}")
    print(f"Total label files updated: {total_updated}")


# Paths to the labels and images directories
labels_dir = r"D:\coco\Datasets\coco_final\train\labels"  # Replace with your labels folder path
images_dir = r"D:\coco\Datasets\coco_final\train\images"  # Replace with your images folder path

# List of unwanted class IDs
unwanted_classes = {4, 8, 9, 10, 11, 12, 24, 25, 26, 27, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                    48, 49, 50, 51, 52, 53, 54, 55, 63, 64, 65, 66, 67, 70, 73, 74, 76, 77, 78, 79, 60, 69}  # Replace with the class IDs you want to remove

# Run the function
process_labels_and_images(labels_dir, images_dir, unwanted_classes)

