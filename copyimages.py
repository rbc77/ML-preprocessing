import json
import shutil
import os

# Paths
filtered_json_path = r"D:\coco_filtered\annotations\updated_instances_train2017.json"
original_images_path = r"D:\coco\train2017"  # Original images
output_images_path = r"D:\coco_filtered\train2017"  # Destination folder for filtered images

# Create output directory if it doesn't exist
os.makedirs(output_images_path, exist_ok=True)

# Load the filtered COCO JSON file
with open(filtered_json_path, "r") as f:
    coco_data = json.load(f)

# Collect all the image IDs from the annotations
image_ids = {annotation["image_id"] for annotation in coco_data["annotations"]}

# Print some sample image_ids from the annotations for verification
print(f"Sample image IDs from annotations: {list(image_ids)[:10]}")

# Load the original image filenames
original_images = os.listdir(original_images_path)

# Print the filenames of the first 10 images in the directory for verification
print(f"Sample image filenames in {original_images_path}: {original_images[:10]}")

# Process and copy images
image_count = 0
missing_images = []
for image_file in original_images:
    # Check if the file is an image (you can add more extensions if needed)
    if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        try:
            # Extract the image ID from the filename (assuming filenames are in the format <image_id>.jpg)
            image_id = int(image_file.split('.')[0])

            # Print out image_id and check if it's in image_ids
            print(f"Processing {image_file} with image_id {image_id}")

            # Check if image is in the annotations
            if image_id in image_ids:
                # Copy the image to the new directory
                shutil.copy(os.path.join(original_images_path, image_file),
                            os.path.join(output_images_path, image_file))
                image_count += 1
            else:
                print(f"Image ID {image_id} not found in annotations.")
        except ValueError:
            # Skip files that can't be converted to an integer
            continue
        except FileNotFoundError:
            missing_images.append(image_file)

# Print summary of the process
print(f"Filtered images copied successfully! Total images copied: {image_count}")

# Handle missing images
if missing_images:
    print("Missing images:")
    for missing_image in missing_images:
        print(missing_image)

# Save the updated annotations (if needed)
updated_json_path = r"D:\coco_filtered\annotations\updated_instances_train2017.json"
with open(updated_json_path, "w") as f:
    json.dump(coco_data, f, indent=4)

print(f"Updated annotations saved to {updated_json_path}")
