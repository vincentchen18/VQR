# ViQR v1.0.0

ViQR (Vinnie's QR) is a QR image forensics tool that allows you to read and generate your own QR Codes, with logo embedding supported! Published to [PyPI](https://pypi.org/project/viqr/1.0.0/).

## Features

### QR Code Generation

- Customisable data generation

- QR Code generation from text file also supported

- Logo embedding supported for business / social media specific QR codes and others

- QR image size is customisable

- Customisable saving filepath

- Overwrite prevention mechanism

- Immediate QR Preview after generation with multi-OS support

### QR Code Reading

- Scans up to multiple QR Codes in the same image.

- Proper image validation

## Usage

QR Code generation:

`viqr -m -l [data] (optional -o [output_path]) (optional -s [size]) (optional -e [path_to_embed_file])`

--> Generates a QR Code for [data] sized [size] pixels at output path [output_path] and optionally embeds the specified image.

`viqr -m -f [file_path] (optional -o [output_path]) (optional -s [size]) (optional -e [path_to_embed_file])`

--> Generates a QR Code for the first data in [file_path] sized [size] pixels at output path [output_path] and optionally embeds the specified image.

QR Code decoding:

`viqr -r [file_path]`

--> Reads (up to multiple) QR codes inside the image at [file_path].


### Usage Table:
| Flag | Description | Default |
|------|-------------|---------|
| `-m`, `--make` | Generate a QR code | — |
| `-r`, `--read` | Read QR code(s) from an image at the given path | — |
| `-l`, `--link` | Data/text to encode (use quotes for URLs) | — |
| `-f`, `--file` | Encode the first line of data from a text file | — |
| `-e`, `--embed` | Path to a logo image to embed in the center | none |
| `-o`, `--output` | Output file path | auto (`qr.png`, `qr1.png`, …) |
| `-s`, `--size` | Output size in pixels (minimum 100) | auto |



## Installation

The ViQR Tool can be installed onto any computer with the following command:

`pip install viqr`

### Requirements/Dependencies:

- Python 3.8+
- qrcode 7.0+
- Pillow 9.0+
- opencv-python 4.3.0+

## AI Use Disclosure for this project:

AI was used minimally to assist in the learning of the argparse module and PyPI publication.

![Example use of ViQR](https://github.com/vincentchen18/viqr/raw/main/img.png)
