import os


def check_class_ids_in_folders(folders):
    """
    Prints unique class IDs and their counts for each folder (train, val, test),
    and also prints the total number of unique classes across all folders.

    Args:
        folders (list): List of paths to folders containing label files (train, val, test).
    """
    all_class_ids = set()  # Store unique class IDs across all folders

    for folder in folders:
        print(f"\nProcessing folder: {folder}")
        class_ids_count = {}

        # List all label files in the folder
        for filename in os.listdir(folder):
            if filename.endswith('.txt'):  # Only process label files (.txt)
                file_path = os.path.join(folder, filename)
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                # Iterate over each line in the label file and extract the class ID
                for line in lines:
                    parts = line.split()
                    class_id = int(parts[0])

                    # Count occurrences of each class ID in the current folder
                    if class_id in class_ids_count:
                        class_ids_count[class_id] += 1
                    else:
                        class_ids_count[class_id] = 1

                    # Add to the set of unique class IDs
                    all_class_ids.add(class_id)

        # Print the class IDs and their counts for the current folder
        print(f"\nClass ID counts in folder: {folder}")
        if not class_ids_count:
            print("No class IDs found.")
        else:
            for class_id, count in sorted(class_ids_count.items()):
                print(f"Class ID {class_id}: {count} occurrences")

    # Print the total number of unique classes across all folders
    print("\nTotal number of unique classes across all folders:", len(all_class_ids))


# Usage example:
test_label_folder = r"D:\coco\Datasets\bull_final\test\labels"
train_label_folder = r"D:\coco\Datasets\bull_final\train\labels"
val_label_folder = r"D:\coco\Datasets\bull_final\valid\labels"

folders = [train_label_folder, val_label_folder, test_label_folder]  # List of folders to process

check_class_ids_in_folders(folders)
