import os
import shutil
from glob import glob


def create_folder_structure(output_dir):
    """Creates the folder structure for the merged dataset."""
    for split in ["train", "test", "valid"]:
        os.makedirs(os.path.join(output_dir, split, "images"), exist_ok=True)
        os.makedirs(os.path.join(output_dir, split, "labels"), exist_ok=True)


def copy_and_rename_files(source_dir, output_dir, split, file_counter):
    """Copies and renames images & labels from multiple datasets while keeping them correctly matched."""
    image_source = os.path.join(source_dir, split, "images")
    label_source = os.path.join(source_dir, split, "labels")

    image_dest = os.path.join(output_dir, split, "images")
    label_dest = os.path.join(output_dir, split, "labels")

    os.makedirs(image_dest, exist_ok=True)
    os.makedirs(label_dest, exist_ok=True)

    image_files = sorted(glob(os.path.join(image_source, "*")))

    for image_path in image_files:
        file_extension = os.path.splitext(image_path)[1]
        new_filename = f"{file_counter}{file_extension}"
        new_label_filename = f"{file_counter}.txt"

        new_image_path = os.path.join(image_dest, new_filename)
        new_label_path = os.path.join(label_dest, new_label_filename)

        # Copy image
        shutil.copy2(image_path, new_image_path)

        # Copy label (if exists)
        original_label = os.path.join(label_source, os.path.splitext(os.path.basename(image_path))[0] + ".txt")
        if os.path.exists(original_label):
            shutil.copy2(original_label, new_label_path)
        else:
            print(f"WARNING: No label found for {image_path}. Skipping.")

        file_counter += 1  # Ensure unique numbering for each dataset

    return file_counter  # Return the updated counter to continue numbering


def merge_datasets(dataset_dirs, output_dir):
    """Merges multiple datasets into a single dataset while keeping image-label alignment correct."""
    create_folder_structure(output_dir)

    file_counter = 0  # To ensure unique names across datasets

    for dataset_dir in dataset_dirs:
        print(f"Merging dataset: {dataset_dir}")

        for split in ["train", "test", "valid"]:
            file_counter = copy_and_rename_files(dataset_dir, output_dir, split, file_counter)

    print(f"Datasets merged successfully into: {output_dir}")


# Define dataset paths

# Define the paths to the datasets and output directory
dataset_dirs = [
    r"D:\coco\Datasets\IoT.v1i.yolov8",
    r"D:\coco\Datasets\Object Detection.v1i.yolov8"
]  # Replace with your dataset directories

output_dir = r"D:\coco\datasets\bull_final"  # Replace with the desired output path

# Merge the datasets
merge_datasets(dataset_dirs, output_dir)
