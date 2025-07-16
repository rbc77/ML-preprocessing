import json

def extract_image_classes(coco_json_path):
    # Load the COCO JSON file
    with open(coco_json_path, 'r') as f:
        coco_data = json.load(f)

    # Create a mapping of image_id to file_name
    image_id_to_filename = {image['id']: image['file_name'] for image in coco_data['images']}

    # Iterate through annotations and collect image file names and class IDs
    image_classes = {}
    for annotation in coco_data['annotations']:
        image_id = annotation['image_id']
        category_id = annotation['category_id']
        file_name = image_id_to_filename[image_id]

        # Append the class ID for each image
        if file_name not in image_classes:
            image_classes[file_name] = []
        image_classes[file_name].append(category_id)

    # Print the result
    for file_name, class_ids in image_classes.items():
        print(f"Image: {file_name} -> Class IDs: {class_ids}")

# Example usage
coco_json_path = r"D:\coco\Datasets\COCO Dataset.v34-yolov11x-1280.coco\train\_annotations.coco.json"  # Update with your actual JSON file path
extract_image_classes(coco_json_path)
