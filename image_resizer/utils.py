import os

def is_image_file(file_path):
    return file_path.lower().endswith(('.png', '.jpg', '.jpeg'))

def generate_output_path(base_path, image_path, external_root, output_type):
    """
    Generates the correct output path for the resized image, maintaining the same
    structure as the input directory.
    """
    # Determine relative path from the external photos root directory
    relative_path = os.path.relpath(image_path, start=external_root)
    
    # Create corresponding output directory structure under the desired output folder (single, listing, or thumbnail)
    output_dir = os.path.join(base_path, output_type, os.path.dirname(relative_path))
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate the full output path with the same image name
    return os.path.join(output_dir, os.path.basename(image_path))