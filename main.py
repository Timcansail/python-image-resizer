import os
from PIL import PngImagePlugin
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from image_resizer import resizer, file_manager, utils

def process_image(image_path, root_directory, output_root):
    results = []
    for size, resize_func in [("single", resizer.resize_to_single), 
                              ("listing", resizer.resize_to_listing), 
                              ("thumbnail", resizer.resize_to_thumbnail)]:
        output_path = utils.generate_output_path(output_root, image_path, root_directory, size)

        # Check if the resized image already exists
        if os.path.exists(output_path):
            results.append((image_path, size, "Skipped: Already exists"))
            continue

        try:
            resize_func(image_path, output_path)
            results.append((image_path, size, "Success"))
        except Exception as e:
            results.append((image_path, size, f"Failed: {e}"))
    return results

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

    # Retrieve image paths
    image_paths = file_manager.get_image_paths(root_directory)

    # Add a progress bar for processing images
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_image, image_path, root_directory, output_root) for image_path in image_paths]
        for future in tqdm(as_completed(futures), total=len(image_paths), desc="Processing Images", unit="image"):
            results = future.result()
            for image_path, size, status in results:
                if "Failed" in status:
                    print(f"Failed to process {image_path} for size {size}: {status}")

if __name__ == "__main__":
    main()