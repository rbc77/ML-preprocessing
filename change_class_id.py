import os


def update_class_id(label_folder, old_class_id, new_class_id):
    # List all label files in the folder
    for filename in os.listdir(label_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(label_folder, filename)
            with open(file_path, 'r') as f:
                lines = f.readlines()

            # Update class IDs in the label file
            updated_lines = []
            for line in lines:
                parts = line.split()
                class_id = int(parts[0])
                if class_id == old_class_id:
                    parts[0] = str(new_class_id)
                updated_lines.append(' '.join(parts))

            # Write updated lines back to the file
            with open(file_path, 'w') as f:
                f.writelines(updated_lines)
            print(f"Updated {filename}")


# Usage example:
label_folder = r"D:\coco\Datasets\monkey\output_folder\train\labels"  # path to the labels folder
old_class_id = 1  # old class ID to be replaced
new_class_id = 100  # new class ID you want to use

update_class_id(label_folder, old_class_id, new_class_id)
