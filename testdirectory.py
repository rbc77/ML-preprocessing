import os
from PIL import Image

# Paths
coco_images_dir = r"D:\coco\coc dataset\test2017\test2017"
output_images_dir = r"D:\coco\output_directory2test\images"
os.makedirs(output_images_dir, exist_ok=True)

# Process each image
for file_name in os.listdir(coco_images_dir):
    src_image_path = os.path.join(coco_images_dir, file_name)
    dest_image_path = os.path.join(output_images_dir, file_name)

    try:
        Image.open(src_image_path).save(dest_image_path)
        print(f"Copied {file_name}")
    except Exception as e:
        print(f"Error processing {file_name}: {e}")

print("Image copying completed!")
