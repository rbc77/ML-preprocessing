import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2

# Define paths
dataset_path = r"D:\coco\Datasets\Final_Dataset\train"
image_folder = os.path.join(dataset_path, "images")
label_folder = os.path.join(dataset_path, "labels")
output_folder = r"D:\coco\Datasets\bbox_info_trainfolder"  # Folder to save outputs

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load class names (optional)
class_names_path = r"D:\coco\Datasets\class_id_to_name.txt"  # Change this or remove it
class_names = None
if os.path.exists(class_names_path):
    with open(class_names_path, "r") as f:
        class_names = [line.strip() for line in f.readlines()]

def draw_and_save_bbox(image_path, label_path, output_path, class_names=None):
    """
    Draws YOLO bounding boxes on an image and saves the output.

    Args:
        image_path (str): Path to the image.
        label_path (str): Path to the YOLO format label file.
        output_path (str): Path to save the output image.
        class_names (list, optional): List of class names.
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Skipping {image_path}: Unable to read image.")
        return
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Get image dimensions
    img_h, img_w, _ = image.shape

    # Read label file
    if not os.path.exists(label_path):
        print(f"Skipping {image_path}: No label file found.")
        return

    with open(label_path, "r") as f:
        labels = f.readlines()

    # Create Matplotlib figure and axis
    fig, ax = plt.subplots(1, figsize=(8, 6))
    ax.imshow(image)

    # Loop through each label and plot bounding boxes
    for label in labels:
        values = label.strip().split()
        class_id = int(values[0])
        x_center, y_center, width, height = map(float, values[1:])

        # Convert YOLO format (relative) to absolute coordinates
        x_min = (x_center - width / 2) * img_w
        y_min = (y_center - height / 2) * img_h
        box_w = width * img_w
        box_h = height * img_h

        # Define class name if available
        class_name = f"Class {class_id}"
        if class_names and class_id < len(class_names):
            class_name = class_names[class_id]

        # Draw bounding box
        rect = patches.Rectangle((x_min, y_min), box_w, box_h, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        # Add label text
        ax.text(x_min, y_min - 5, class_name, color='red', fontsize=10, bbox=dict(facecolor='white', alpha=0.75))

    # Remove axes and save the image
    plt.axis("off")
    output_file = os.path.join(output_folder, os.path.basename(image_path))
    plt.savefig(output_file, bbox_inches="tight", pad_inches=0)
    plt.close(fig)  # Close figure to free memory
    print(f"Saved: {output_file}")

# Process all images in the train/images folder
for image_file in os.listdir(image_folder):
    if image_file.endswith(('.jpg', '.png', '.jpeg')):  # Check for image files
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, os.path.splitext(image_file)[0] + ".txt")  # Matching label file
        output_path = os.path.join(output_folder, image_file)

        # Draw and save bounding boxes
        draw_and_save_bbox(image_path, label_path, output_path, class_names)

print("Processing complete. All images saved in bbox_info_trainfolder.")
