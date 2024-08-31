import os

def is_image_file(file_path):
    return file_path.lower().endswith(('.png', '.jpg', '.jpeg'))

def generate_output_path(base_path, image_path, output_type):
    relative_path = os.path.relpath(image_path, start = 'photos')
    output_dir = os.path.join(base_path, output_type, os.path.dirname(relative_path))
    os.makedirs(output_dir, exist_ok = True)
    return os.path.join(output_dir, os.path.basename(image_path))