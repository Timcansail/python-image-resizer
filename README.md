# Image Resizer

This project is a Python-based image resizer that processes images from an existing file structure and copies them into a new structure in three different sizes: single, listing, and thumbnail. The program is optimized to skip images that have already been processed, significantly reducing runtime when new images are added.

## Features

- **Multithreaded Processing:** Utilizes multiple threads to efficiently process images.
- **Three Output Sizes:** Creates resized images in three different sizes: single (500px), listing (300px), and thumbnail (100px).
- **Directory Structure Preservation:** Maintains the original directory structure of the input images in the output.
- **File Existence Check:** Skips processing for images that have already been resized, reducing redundant work and speeding up runtime.

## Requirements

- Python 3.6+
- [Pillow (PIL)](https://python-pillow.org/) (Python Imaging Library)
- [tqdm](https://github.com/tqdm/tqdm) (for progress bar)
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) (for multithreading)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/image-resizer.git
    cd image-resizer
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    *Ensure that `requirements.txt` includes:*

    ```text
    Pillow
    tqdm
    ```

## Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. Enter the path to the root directory containing the images you want to process when prompted.

3. The program will create an output directory named `root`, where it will store the resized images in three different folders: `single`, `listing`, and `thumbnail`.

## Directory Structure

- **`main.py`**: The main script that orchestrates the image processing.
- **`resizer.py`**: Contains functions for resizing images to the specified dimensions.
- **`utils.py`**: Utility functions for checking file types and generating output paths.
- **`file_manager.py`**: Functions for handling file operations, such as retrieving image paths and creating directories.
- **`root/`**: The output directory where resized images are saved, preserving the original folder structure.

## Example

1. Suppose you have the following input directory structure:

    ```
    /path/to/images
    ├── folder1
    │   ├── image1.jpg
    │   └── image2.png
    └── folder2
        └── image3.jpeg
    ```

2. After running the script, the output will be:

    ```
    /root
    ├── single
    │   ├── folder1
    │   │   ├── image1.jpg
    │   │   └── image2.png
    │   └── folder2
    │       └── image3.jpeg
    ├── listing
    │   ├── folder1
    │   │   ├── image1.jpg
    │   │   └── image2.png
    │   └── folder2
    │       └── image3.jpeg
    └── thumbnail
        ├── folder1
        │   ├── image1.jpg
        │   └── image2.png
        └── folder2
            └── image3.jpeg
    ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pillow](https://python-pillow.org/) for image processing.
- [tqdm](https://github.com/tqdm/tqdm) for progress visualization.
- Python's standard library modules.

