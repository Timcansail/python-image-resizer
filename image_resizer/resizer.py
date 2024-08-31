from PIL import Image

def resize_image(input_path, output_path, width):
    """
    Resizes an image to a specified width while maintaining the aspect ratio.

    Args:
        input_path (str): The path to the original image.
        output_path (str): The path where the resized image will be saved.
        width (int): The desired width for the resized image.

    Returns:
        None
    """
    with Image.open(input_path) as img:
        aspect_ratio = img.height / img.width
        new_height = int(width * aspect_ratio)
        resized_image = img.resize((width, new_height))
        resized_image.save(output_path)

def resize_to_single(image_path, output_path):
    """
    Resizes an image to 500 pixels in width.

    Args:
        image_path (str): The path to the original image.
        output_path (str): The path where the resized image will be saved.

    Returns:
        None
    """
    resize_image(image_path, output_path, 500)

def resize_to_listing(image_path, output_path):
    """
    Resizes an image to 300 pixels in width.

    Args:
        image_path (str): The path to the original image.
        output_path (str): The path where the resized image will be saved.

    Returns:
        None
    """
    resize_image(image_path, output_path, 300)

def resize_to_thumbnail(image_path, output_path):
    """
    Resizes an image to 100 pixels in width.

    Args:
        image_path (str): The path to the original image.
        output_path (str): The path where the resized image will be saved.

    Returns:
        None
    """
    resize_image(image_path, output_path, 100)
