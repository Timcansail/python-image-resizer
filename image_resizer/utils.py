import os

def is_image_file(file_path):
    """
    Checks if the given file path corresponds to an image file.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file is an image, False otherwise.
    """
    return file_path.lower().endswith(('.png', '.jpg', '.jpeg'))

def generate_output_path(base_path, image_path, external_root, output_type):
    """
    Generates the output path for the resized image, maintaining the input directory structure.

    Args:
        base_path (str): The base output directory path.
        image_path (str): The path to the original image.
        external_root (str): The root directory of the input images.
        output_type (str): The type of resized image ('single', 'listing', 'thumbnail').

    Returns:
        str: The full output path for the resized image.
    """
    # Determine relative path from the external photos root directory
    relative_path = os.path.relpath(image_path, start=external_root)
    
    # Create corresponding output directory structure under the desired output folder (single, listing, or thumbnail)
    output_dir = os.path.join(base_path, output_type, os.path.dirname(relative_path))
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate the full output path with the same image name
    return os.path.join(output_dir, os.path.basename(image_path))
