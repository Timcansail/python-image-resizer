import os
from image_resizer.utils import is_image_file

def get_image_paths(root_directory):
    """
    Retrieves all image file paths from the specified root directory and its subdirectories.

    Args:
        root_directory (str): The root directory to search for images.

    Returns:
        list: A list of file paths to all images in the directory.
    """
    image_paths = []
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if is_image_file(filename):
                image_paths.append(os.path.join(dirpath, filename))
    return image_paths

def create_base_directories(base_path, output_type):
    """
    Creates the base directories ('single', 'listing', 'thumbnail') under the specified root directory.

    Args:
        base_path (str): The root directory for storing resized images.
        output_type (str): The type of resized image ('single', 'listing', 'thumbnail').

    Returns:
        None
    """
    output_dir = os.path.join(base_path, output_type)
    os.makedirs(output_dir, exist_ok=True)

def save_image(image, output_path):
    """
    Saves an image to the specified path.

    Args:
        image (PIL.Image.Image): The image object to save.
        output_path (str): The path where the image will be saved.

    Returns:
        None
    """
    image.save(output_path)
