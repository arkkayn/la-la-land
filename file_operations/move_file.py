import shutil
import os

def move_file(source_folder, destination_folder, filename):
    # Absolute paths to the test folders in Documents
    source_path = os.path.join('/Users/laurenkraynak/Documents', source_folder, filename)
    destination_path = os.path.join('/Users/laurenkraynak/Documents', destination_folder, filename)

    print(f"Source path: {source_path}")
    print(f"Destination path: {destination_path}")

    try:
        shutil.move(source_path, destination_path)
        print(f"File '{filename}' has been moved from '{source_folder}' to '{destination_folder}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found in '{source_folder}'.")
    except PermissionError:
        print("Permission denied. Please check your access rights.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
move_file('test_folder_1', 'test_folder_2', 'test.pdf')