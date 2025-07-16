import os

def update_class_id(label_folder, old_class_ids, new_class_ids):
    """
    Updates the class IDs in the label files inside the given folder.

    Args:
        label_folder (str): The path to the folder containing label files.
        old_class_ids (list): List of old class IDs to be replaced.
        new_class_ids (list): List of new class IDs to replace the old ones.
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
                    # Check if the current class_id is in old_class_ids and replace it with the corresponding new_class_id
                    if class_id in old_class_ids:
                        index = old_class_ids.index(class_id)  # Find the index of the old_class_id
                        parts[0] = str(new_class_ids[index])  # Replace with corresponding new_class_id
                    updated_lines.append(' '.join(parts) + '\n')  # Add newline at the end of each line

            # Write updated lines back to the file
            with open(file_path, 'w') as f:
                f.writelines(updated_lines)
            print(f"Updated {filename} in {label_folder}")

def update_dataset_class_ids(train_folder, val_folder, test_folder, old_class_ids, new_class_ids):
    """
    Updates class IDs in training, validation, and test datasets.

    Args:
        train_folder (str): Path to the training labels folder.
        val_folder (str): Path to the validation labels folder.
        test_folder (str): Path to the test labels folder.
        old_class_ids (list): List of old class IDs to be replaced.
        new_class_ids (list): List of new class IDs to replace the old ones.
    """
    # Update train dataset labels
    update_class_id(train_folder, old_class_ids, new_class_ids)

    # Update validation dataset labels
    update_class_id(val_folder, old_class_ids, new_class_ids)

    # Update test dataset labels
    update_class_id(test_folder, old_class_ids, new_class_ids)

# Usage example:
test_label_folder = r"D:\coco\Datasets\navya_dataset_done_by_RBC\test\labels"      # Path to your test labels folder
train_label_folder = r"D:\coco\Datasets\navya_dataset_done_by_RBC\train\labels"  # Path to your train labels folder
val_label_folder = r"D:\coco\Datasets\navya_dataset_done_by_RBC\valid\labels"      # Path to your validation labels folder

old_class_ids = [92, 107]  # List of old class IDs you want to replace
new_class_ids = [30, 46]  # List of new class IDs to use

# Update class IDs in train, validation, and test folders
update_dataset_class_ids(train_label_folder, val_label_folder, test_label_folder, old_class_ids, new_class_ids)
