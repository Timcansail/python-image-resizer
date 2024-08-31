import os
from image_resizer import resizer, file_manager, utils

def main():
    # Ask user for external root directory
    root_directory = input("Enter external root directory path: ")

    # Define the output root directory
    output_root = 'root'

    # Create output directories
    for size in ["single", "listing", "thumbnail"]:
        file_manager.create_base_directories(output_root, size)

    # Retreive image paths
    image_paths = file_manager.get_image_paths(root_directory)

    for image_path in image_paths:
        # Determine output paths
        for size, resize_func in [("single", resizer.resize_to_single),
                                  ("listing", resizer.resize_to_listing),
                                  ("thumbnail", resizer.resize_to_thumbnail)]:
            output_path = utils.generate_output_path(output_root, image_path, root_directory, size)
            resize_func(image_path, output_path)

if __name__ == "__main__":
    main()