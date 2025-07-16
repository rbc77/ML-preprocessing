import json
from pathlib import Path
import shutil


class CocoFilter:
    def __init__(self, input_json, output_json, categories_to_keep, image_input_folder, image_output_folder):
        self.input_json = input_json
        self.output_json = output_json
        self.categories_to_keep = categories_to_keep
        self.image_input_folder = Path(image_input_folder)
        self.image_output_folder = Path(image_output_folder)

        # Create output folder for filtered images if it doesn't exist
        self.image_output_folder.mkdir(parents=True, exist_ok=True)

        # Data structures for the filtered dataset
        self.new_images = []
        self.new_annotations = []
        self.new_categories = []
        self.image_ids_to_keep = set()

    def filter_annotations(self):
        # Load the input JSON file
        with open(self.input_json, 'r') as f:
            coco_data = json.load(f)

        # Extract categories, annotations, and images
        categories = coco_data.get("categories", [])
        annotations = coco_data.get("annotations", [])
        images = coco_data.get("images", [])

        print("Filtering categories...")
        # Filter categories based on user input
        self.new_categories = [cat for cat in categories if cat['name'] in self.categories_to_keep]
        category_ids_to_keep = {cat['id'] for cat in self.new_categories}

        # Identify unwanted category IDs
        unwanted_category_ids = {cat['id'] for cat in categories if cat['name'] not in self.categories_to_keep}

        print(f"Categories kept: {len(self.new_categories)}")

        print("Filtering annotations...")
        # Filter annotations based on the filtered categories
        for ann in annotations:
            if ann['category_id'] in category_ids_to_keep:
                self.new_annotations.append(ann)
                self.image_ids_to_keep.add(ann['image_id'])

        print(f"Annotations kept: {len(self.new_annotations)}")

        print("Filtering images...")
        # Filter images based on the annotations we kept, excluding those linked to unwanted categories
        self.new_images = [
            img for img in images if img['id'] in self.image_ids_to_keep and
                                     not any(ann['category_id'] in unwanted_category_ids for ann in annotations if
                                             ann['image_id'] == img['id'])
        ]

        print(f"Images kept: {len(self.new_images)}")

        # Save filtered JSON data
        filtered_data = {
            "images": self.new_images,
            "annotations": self.new_annotations,
            "categories": self.new_categories
        }

        with open(self.output_json, 'w') as f:
            json.dump(filtered_data, f, indent=4)

        print(f"Filtered annotations and categories saved to {self.output_json}")

    def copy_filtered_images(self):
        # Copy only the images present in the filtered dataset
        print(f"Copying {len(self.new_images)} filtered images to {self.image_output_folder}...")
        for image in self.new_images:
            original_image_path = self.image_input_folder / image['file_name']
            filtered_image_path = self.image_output_folder / image['file_name']

            if original_image_path.exists():
                try:
                    shutil.copy(original_image_path, filtered_image_path)
                except Exception as e:
                    print(f"Error processing image {image['file_name']}: {e}")
            else:
                print(f"Warning: Image {image['file_name']} not found in {self.image_input_folder}")

    def run(self):
        self.filter_annotations()
        self.copy_filtered_images()


def main():
    # User inputs
    input_json_path = "D:/coco/annotations_trainval2017/annotations/instances_train2017.json"  # Path to the input JSON file
    output_json_path = "D:/coco/filtered_train2017_annotation.json"  # Path to save the filtered JSON file
    image_input_folder = "D:/coco/train2017/train2017"  # Path to the folder containing original images
    image_output_folder = "D:/coco/filtered_coco_images_train2017/"  # Path to save filtered images
    categories_to_keep = [
        "person", "bicycle", "car", "motorcycle", "bus", "train", "truck", "boat",
        "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
        "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra",
        "giraffe", "backpack", "umbrella", "handbag", "frisbee", "skis", "snowboard",
        "sports ball", "kite", "baseball bat", "skateboard", "surfboard", "tennis racket",
        "bottle", "knife", "banana", "chair", "couch", "potted plant", "bed", "dining table",
        "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave",
        "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "teddy bear",
        "hair drier"
    ]

    # Initialize and run the filtering process
    coco_filter = CocoFilter(input_json_path, output_json_path, categories_to_keep, image_input_folder,
                             image_output_folder)
    coco_filter.run()


if __name__ == "__main__":
    main()
