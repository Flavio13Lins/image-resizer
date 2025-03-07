# Image Resizer & Aligner

## Overview

This Python project resizes and adapts all images inside a folder to a uniform size and proportion. It was created to solve the issue of misaligned images on websites by standardizing their dimensions. The script automatically detects the smallest image size, prompts the user for a target size, and resizes/crops all images accordingly.

## Features

- Bulk resizes images in a folder.
- Identifies the smallest image size.
- Allows users to set a target size.
- Maintains aspect ratio or crops images proportionally.
- Works with various image formats (JPG, PNG, etc.).

## Installation

### Prerequisites

Ensure you have Python installed on your system.

```sh
python --version
```

Install required dependencies:

```sh
pip install pillow
```

## Usage

1. Clone this repository:
   ```sh
   git clone https://github.com/Flavio13Lins/image-resizer.git
   cd image-resizer
   ```
2. Run the script:
   ```sh
   python main.py
   ```
3. Follow the prompts to enter the image folder path and desired size.

## Example

**Before:**

- Image 1: 800x600
- Image 2: 1200x900
- Image 3: 1024x768

**After setting target size to 800x600:**

- All images are resized/cropped to 800x600.

## Contributing

Pull requests are welcome! If you have suggestions, feel free to open an issue or submit a PR.

## Contact

Developed by [Flávio Lins](https://www.linkedin.com/in/flaviolins/). Feel free to reach out!
