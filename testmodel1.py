from ultralytics import YOLO
import os
import cv2
import pandas as pd

# Paths to your model and test images
model_path = r'D:\coco\Datasets\yolo_V8_trained3\weights\best.pt'
test_images_folder = r''
output_folder = r'D:\coco\Datasets\output_test_data'

# Load the trained model
model = YOLO(model_path)

# Loop through each image in the test folder
for image_name in os.listdir(test_images_folder):
    if image_name.endswith(('.jpg', '.png', '.jpeg')):
        image_path = os.path.join(test_images_folder, image_name)

        # Read image
        image = cv2.imread(image_path)

        # Perform inference
        results = model(image)

        # Assuming the result is a list, access the first result
        result = results[0]

        # Get the boxes, class names, and confidence scores
        boxes = result.boxes
        class_ids = boxes.cls.cpu().numpy()  # Move tensor to CPU and convert to numpy array
        confidences = boxes.conf.cpu().numpy()  # Move tensor to CPU and convert to numpy array
        xywh = boxes.xywh.cpu().numpy()  # Move tensor to CPU and convert to numpy array

        # Create a DataFrame for better readability
        df = pd.DataFrame({
            'class_id': class_ids,
            'confidence': confidences,
            'x': xywh[:, 0],  # x center
            'y': xywh[:, 1],  # y center
            'width': xywh[:, 2],
            'height': xywh[:, 3]
        })

        print(f"Results for {image_name}:\n", df)

        # Draw bounding boxes on the image
        for i in range(len(class_ids)):
            x_center, y_center, width, height = xywh[i]
            x1 = int(x_center - width / 2)
            y1 = int(y_center - height / 2)
            x2 = int(x_center + width / 2)
            y2 = int(y_center + height / 2)

            # Draw rectangle on the image
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green rectangle

            # Add label with confidence
            label = f'{model.names[int(class_ids[i])]}: {confidences[i]:.2f}'
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Save the output image with bounding boxes
        output_image_path = os.path.join(output_folder, image_name)
        cv2.imwrite(output_image_path, image)
