import os
from PIL import PngImagePlugin
from tqdm import tqdm
from image_resizer import resizer, file_manager, utils

def main():
    # Increase the text chunk size limits before processing images
    PngImagePlugin.MAX_TEXT_CHUNK = 100 * 1024 * 1024  # 100MB limit for individual text chunks
    PngImagePlugin.MAX_TEXT_MEMORY = 300 * 1024 * 1024  # 300MB total limit for all text chunks

    # Ask user for external root directory
    root_directory = input("Enter external root directory path: ")

    # Define the output root directory
    output_root = 'root'

    # Create output directories
    for size in ["single", "listing", "thumbnail"]:
        file_manager.create_base_directories(output_root, size)

    # Retreive image paths
    image_paths = file_manager.get_image_paths(root_directory)

    # Add a progress bar for processing images
    for image_path in tqdm(image_paths, desc="Processing Images", unit="image"):
        # Resize and save images for each output size
        for size, resize_func in [("single", resizer.resize_to_single), 
                                  ("listing", resizer.resize_to_listing), 
                                  ("thumbnail", resizer.resize_to_thumbnail)]:
            output_path = utils.generate_output_path(output_root, image_path, root_directory, size)
            try:
                resize_func(image_path, output_path)
            except Exception as e:
                print(f"Failed to process {image_path} for size {size}: {e}")

if __name__ == "__main__":
    main()