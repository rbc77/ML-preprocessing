import os
import glob

def polygon_to_bbox(polygon):
    """
    Convert a polygon annotation to YOLO bounding box format.
    Args:
        polygon (list of tuples): List of (x, y) coordinates.
    Returns:
        (x_center, y_center, width, height) in YOLO format.
    """
    x_coords = [point[0] for point in polygon]
    y_coords = [point[1] for point in polygon]

    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)

    # Convert to YOLO format (normalized values)
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    width = x_max - x_min
    height = y_max - y_min

    return (x_center, y_center, width, height)

def detect_polygon_format(line):
    """
    Detect if a label line is in polygon format.
    Polygon format has multiple coordinate pairs after class_id.
    """
    parts = line.strip().split()
    return len(parts) > 5  # Polygon format has more than 5 values

def process_label_file(file_path):
    """
    Convert polygon labels to bounding box format in a single label file.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

    updated_lines = []
    polygon_count = 0

    for line in lines:
        data = line.strip().split()
        class_id = data[0]

        if detect_polygon_format(line):  # Check if it's a polygon format
            polygon_count += 1
            polygon = [(float(data[i]), float(data[i+1])) for i in range(1, len(data), 2)]

            # Convert polygon to bounding box
            x_center, y_center, width, height = polygon_to_bbox(polygon)
            updated_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
        else:
            updated_lines.append(line.strip())  # Keep existing YOLO labels unchanged

    # Overwrite the file with updated labels
    with open(file_path, "w") as file:
        file.write("\n".join(updated_lines) + "\n")

    return polygon_count

def batch_process_labels(label_folder):
    """
    Process all label files in a folder, converting only polygon format labels.
    """
    label_files = glob.glob(os.path.join(label_folder, "*.txt"))
    total_polygons = 0
    processed_files = 0

    # First, count the total polygon labels
    for file in label_files:
        with open(file, "r") as f:
            for line in f:
                if detect_polygon_format(line):
                    total_polygons += 1
                    break  # Count only once per file

    print(f"Total polygon label files detected: {total_polygons}")

    # Now, start conversion
    for file in label_files:
        polygon_count = process_label_file(file)
        if polygon_count > 0:
            processed_files += 1
            print(f"Converted: {os.path.basename(file)} ({polygon_count} polygons)")

    print(f"Conversion complete. {processed_files} files updated.")

# Example Usage
label_folder = r"D:\coco\Datasets\snake_final\test\labels"  # Change this to your actual folder path
batch_process_labels(label_folder)
