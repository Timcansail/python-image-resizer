import os
from image_resizer.utils import is_image_file

def get_image_paths(root_directory):
    image_paths = []
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if is_image_file(filename):
                image_paths.append(os.path.join(dirpath, filename))
    return image_paths

def create_output_directory(base_path, output_type):
    output_dir = os.path.join(base_path, output_type)
    os.makedirs(output_dir, exist_ok = True)
    return output_dir

def save_image(image, output_path):
    image.save(output_path)