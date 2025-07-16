import os

# Paths to your dataset
image_folder = r"D:\coco\Datasets\snake_final\train\images"  # Replace with the path to your images
label_folder = r"D:\coco\Datasets\snake_final\train\labels"  # Replace with the path to your labels

# List of unwanted image file names (with extensions)
unwanted_image_numbers = [
     "138.jpg", "139.jpg", "140.jpg", "201.jpg", "202.jpg", "203.jpg", "309.jpg", "310.jpg", "311.jpg"
]

# Loop through each unwanted image
for image_name in unwanted_image_numbers:
    # Construct full paths for image and label
    image_path = os.path.join(image_folder, image_name)
    label_name = os.path.splitext(image_name)[0] + ".txt"
    label_path = os.path.join(label_folder, label_name)

    # Debug: Print constructed paths
    print(f"Looking for image: {image_path}")
    print(f"Looking for label: {label_path}")

    # Check and delete the image
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Deleted image: {image_path}")
    else:
        print(f"Image not found: {image_path}")

    # Check and delete the corresponding label
    if os.path.exists(label_path):
        os.remove(label_path)
        print(f"Deleted label: {label_path}")
    else:
        print(f"Label not found: {label_path}")

print("Deletion completed.")
