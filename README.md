# image_cartoon_converter

A Python tool using OpenCV to transform standard images into cartoon-style renderings by combining bilateral filtering and adaptive thresholding.

## Example Result

![Example Result](screenshot.png)

## Features

- **Cartoon Effect**: Converts photos into stylized cartoon art.
- **Edge Detection**: Generates bold outlines using adaptive thresholding.
- **Bilateral Filter**: Smoothes colors while preserving sharp edges.
- **Comparison View**: Displays original and processed images side-by-side.

## Project Files

- `Image_Cartoon_Converter.py`: Main execution script.
- `image.jpg`: Input image file.
- `screenshot.png`: Result screenshot for demonstration.
- `cartoon_output.jpg`: The final processed output.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy