import os

def update_class_id(label_folder, old_class_id, new_class_id):
    """
    Updates the class ID in the label files inside the given folder.

    Args:
        label_folder (str): The path to the folder containing label files.
        old_class_id (int): The old class ID to be replaced.
        new_class_id (int): The new class ID to replace the old one with.
    """
    # List all label files in the folder
    for filename in os.listdir(label_folder):
        if filename.endswith('.txt'):  # Only process label files (.txt)
            file_path = os.path.join(label_folder, filename)
            with open(file_path, 'r') as f:
                lines = f.readlines()

            # Update class IDs in the label file
            updated_lines = []
            for line in lines:
                parts = line.split()
                if len(parts) > 0:  # Ensure the line is not empty
                    class_id = int(parts[0])
                    if class_id == old_class_id:
                        parts[0] = str(new_class_id)  # Replace old class ID with the new one
                    updated_lines.append(' '.join(parts) + '\n')  # Add newline at the end of each line

            # Write updated lines back to the file
            with open(file_path, 'w') as f:
                f.writelines(updated_lines)
            print(f"Updated {filename} in {label_folder}")

def update_dataset_class_ids(train_folder, val_folder, test_folder, old_class_id, new_class_id):
    """
    Updates class IDs in training, validation, and test datasets.

    Args:
        train_folder (str): Path to the training labels folder.
        val_folder (str): Path to the validation labels folder.
        test_folder (str): Path to the test labels folder.
        old_class_id (int): The old class ID to be replaced.
        new_class_id (int): The new class ID to replace the old one with.
    """
    # Update train dataset labels
    update_class_id(train_folder, old_class_id, new_class_id)

    # Update validation dataset labels
    update_class_id(val_folder, old_class_id, new_class_id)

    # Update test dataset labels
    update_class_id(test_folder, old_class_id, new_class_id)

# Usage example:
test_label_folder = r"D:\coco\Datasets\bull_final\test\labels"
train_label_folder = r"D:\coco\Datasets\bull_final\train\labels"
val_label_folder = r"D:\coco\Datasets\bull_final\valid\labels"

old_class_id = 0  # Old class ID you want to replace
new_class_id = 32  # New class ID to use

# Update class IDs in train, validation, and test folders
update_dataset_class_ids(train_label_folder, val_label_folder, test_label_folder, old_class_id, new_class_id)
