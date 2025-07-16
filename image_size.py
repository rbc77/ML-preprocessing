import os
from PIL import Image

# Define the base dataset folder
BASE_FOLDER = r"D:\coco\Datasets\buffalo_final"

# Subdirectories where images are stored
SUBSETS = ["train", "test", "valid"]
IMAGE_FOLDER_NAMES = ["images"]  # Only scan inside the "images" folders

image_sizes = set()  # To store unique image sizes

# Loop through each subset (train, test, val)
for subset in SUBSETS:
    for folder in IMAGE_FOLDER_NAMES:
        image_dir = os.path.join(BASE_FOLDER, subset, folder)

        if not os.path.exists(image_dir):
            print(f"Warning: {image_dir} does not exist!")
            continue

        # Process all images in the folder
        for filename in os.listdir(image_dir):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(image_dir, filename)
                try:
                    with Image.open(img_path) as img:
                        width, height = img.size
                        image_sizes.add((width, height))  # Store unique sizes
                except Exception as e:
                    print(f"Error reading {filename}: {e}")

# Print all unique image sizes found
print("Unique image sizes in dataset:", image_sizes)
