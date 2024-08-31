from PIL import Image

def resize_image(input_path, output_path, width):
    with Image.open(input_path) as img:
        aspect_ratio = img.height / img.width
        new_height = int(width * aspect_ratio)
        resized_image = img.resize((width, new_height), Image.ANTIALIAS)
        resized_image.save(output_path)

def resize_to_single(image_path, output_path):
    resize_image(image_path, output_path, 500)

def resize_to_listing(image_path, output_path):
    resize_image(image_path, output_path, 300)

def resize_to_thumbnail(image_path, output_path):
    resize_image(image_path, output_path, 100)