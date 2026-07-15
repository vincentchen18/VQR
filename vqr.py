import argparse, qrcode, cv2, sys
from PIL import Image
# initialisation
# flags:
# -l or --link : specify a link/data to embed in the qr code or you can also specify a data path
# -e or --embed : embed a subimage into the qr code (for logos and stuffs) --> ill make this an optional flag
# -o or --output : specify the name/path of the output file i will make this default to qr.png
# -s or --size : specify a size (optional) minimum 100 for proper scanning
#
def make(): #make the qr code
    pass

def read(): # read a qr code

def main():
    parser = argparse.ArgumentParser(prog="vqr")
    parser.add_argument("-l", "--link")
    parser.add_argument("-e", "--embed")
    parser.add_argument("-o", "--output")
    parser.add_argument("-s", "--size")
    parser.add_argument("-m", "--make", action="store_true")
    parser.add_argument("-r", "--read") #accept path
    args = parser.parse_args()
    if args.make and args.read is not None:
        print("Please choose either --make or --read.")
        sys.exit()
    if args.read is not None and args.make is None:
        if args.link is not None or args.embed is not None or args.output is not None or args.size is not None:
            print("Reading a QR Code does not accept the following fields: link, embed, output, size.")
            sys.exit()

