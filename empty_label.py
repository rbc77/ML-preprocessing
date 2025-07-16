import os

# Path to the main dataset folder
labels_dir = r"D:\coco\Datasets\coco_final"

# Check if the directory exists
if not os.path.exists(labels_dir):
    print("❌ Error: Labels directory does not exist!")
    exit()

empty_files = []

# Recursively scan train, test, and val folders
for root, _, files in os.walk(labels_dir):
    for file in files:
        file_path = os.path.join(root, file)
        # Check if the file is a .txt label file and is empty
        if file.endswith(".txt") and os.path.isfile(file_path) and os.stat(file_path).st_size == 0:

            empty_files.append(file_path)

# Print results
if empty_files:
    print(f"🚨 Found {len(empty_files)} empty label files:")
    for file in empty_files:
        print(f"   - {file}")

    # Ask user before deleting
    confirm = input("\n❗ Do you want to delete all empty label files? (yes/no): ").strip().lower()
    if confirm == "yes":
        for file in empty_files:
            os.remove(file)
        print(f"✅ Deleted {len(empty_files)} empty label files.")
    else:
        print("❌ Deletion canceled. No files were deleted.")
else:
    print("✅ No empty label files found!")
