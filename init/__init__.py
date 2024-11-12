import os
import shutil
import time


def init():
    print("Initiating Hydrapak...")
    start_time = time.time()

    # Get the current working directory
    current_dir = os.getcwd()

    # Define the source path (the "hydrapak" directory in the hydrazine project)
    source_path = os.path.join(os.path.dirname(__file__), "hydrapak")
    print(f"Source path: {source_path}")

    # Define the destination path (the current working directory)
    dest_path = current_dir
    print(f"Destination path: {dest_path}")

    try:
        # Check if the source directory exists
        if os.path.exists(source_path):
            print("Found 'Hydrapak' directory.")

            # Copy the contents of the directory tree
            print("Starting file copying process...")
            shutil.copytree(source_path, dest_path, dirs_exist_ok=True)

            print("File copying completed.")

            end_time = time.time()
            elapsed_time = end_time - start_time

            # List the copied files
            copied_files = [f for f in os.listdir(dest_path) if f != "__pycache__"]
            print(f"\nCopied files:")
            for file in copied_files:
                print(file)

            print(f"\nTotal files copied: {len(copied_files)}")

            print(f"Copy completed successfully! Elapsed time: {elapsed_time:.2f} seconds")

        else:
            print("Error: The 'Hydrapak' directory does not exist in the hydrazine project.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return True