import json
import os
import shutil

# Define paths
annotation_file = 'D:/coco/annotations_trainval2017/annotations/instances_train2017.json'
output_file = 'D:/coco/filtered_final_images_filtered_instances_train2017.json'
input_image_folder = 'D:/coco/train2017/train2017'
output_image_folder = 'D:/coco/filtered_final_images_train2017/'

# Create the output image folder if it doesn't exist
if not os.path.exists(output_image_folder):
    os.makedirs(output_image_folder)

# Load the annotations
with open(annotation_file, 'r') as f:
    data = json.load(f)

# Define the classes to keep and remove
wanted_classes = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 31, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 49, 52, 62, 63, 64, 65, 67, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 88, 89]
unwanted_classes = [5, 32, 46, 47, 48, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 87, 90]

# Function to check if an annotation belongs to a wanted or unwanted class
def is_wanted(annotation):
    return annotation['category_id'] in wanted_classes

def is_unwanted(annotation):
    return annotation['category_id'] in unwanted_classes

# Initialize filtered annotations and sets
filtered_annotations = {'images': [], 'annotations': [], 'categories': data['categories']}
kept_image_ids = set()

# Process annotations
for annotation in data['annotations']:
    if is_wanted(annotation):
        filtered_annotations['annotations'].append(annotation)
        kept_image_ids.add(annotation['image_id'])  # Mark the image as valid
    elif is_unwanted(annotation):
        # Skip unwanted annotations but do not mark the image yet
        pass

# Filter images based on valid annotations
for image_info in data['images']:
    if image_info['id'] in kept_image_ids:
        # Copy the image to the output folder
        original_image_path = os.path.join(input_image_folder, image_info['file_name'])
        new_image_path = os.path.join(output_image_folder, image_info['file_name'])
        if os.path.exists(original_image_path):
            shutil.copy(original_image_path, new_image_path)
            filtered_annotations['images'].append(image_info)
        else:
            print(f"Warning: Image {image_info['file_name']} not found in the source folder.")

# Save the filtered annotations
with open(output_file, 'w') as f:
    json.dump(filtered_annotations, f, indent=4)

# Print the summary
print("\nFiltering complete!")
print(f"Total annotations processed: {len(data['annotations'])}")
print(f"Total annotations kept: {len(filtered_annotations['annotations'])}")
print(f"Total images kept: {len(filtered_annotations['images'])}")
print(f"Final filtered annotations saved to {output_file}")
print(f"Filtered images saved to {output_image_folder}")
