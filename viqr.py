import argparse, qrcode, cv2, sys, os
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

def read(path): # read a qr code
    # we have already verified that the file is a real image (according to magic bytes) and now we gotta view it and check for qr codes.
    image = cv2.imread(path)
    detector = cv2.QRCodeDetector()
    data_response, decoded, points, useless_variable = detector.detectAndDecodeMulti(image)
    if not data_response:
        return "No QR Codes found."
    links = [link for link in decoded if link]
    if not links: # found qr but decoding failed
        return "QR Decoding failed."
    return links

def main():
    parser = argparse.ArgumentParser(prog="viqr")
    parser.add_argument("-l", "--link")
    parser.add_argument("-f", "--file") #file path if for some reason their link/data is in a file
    parser.add_argument("-e", "--embed")
    parser.add_argument("-o", "--output")
    parser.add_argument("-s", "--size")
    parser.add_argument("-m", "--make", action="store_true")
    parser.add_argument("-r", "--read") #accept path
    args = parser.parse_args()
    if args.make and args.read is not None:
        print("Please choose either --make or --read.")
        sys.exit()
    if not args.make and args.read is None: # no action selected
        print("You are missing an action or a filepath. Would you like to make (-m) or read (-r) a QR Code?")
        sys.exit()
    if args.read is not None and not args.make: # reading mode
        if args.link is not None or args.embed is not None or args.output is not None or args.size is not None:
            print("Reading a QR Code does not accept the following fields: link, embed, output, size.")
            sys.exit()
        if os.path.isfile(args.read):
            try:
                with Image.open(args.read) as img:
                    img.verify()  # checks the file is a valid, decodable image
                pass # the image "passed" LMAO
            except Exception:
                print("Your file is either truncated or is not an image file. Please check the magic bytes and make sure the image is correct.")
                sys.exit()
        else:
            print("File path does not exist or target path is not a file.")
            sys.exit()
        response = read(args.read)
        if response == "No QR Codes found.":
            print(f"The provided image at {args.read} does not seem to have any valid QR codes to read.")
            sys.exit()
        elif response == "QR Decoding failed.":
            print(f"QR code(s) were found in your image but were invalid or unscannable.")
            sys.exit()
        else: #success :D
            if len(response) == 1:
                print(f"1 link successfully decoded in {args.read}: {response[0]}")
            else:
                print(f"Multiple links successfully decoded in {args.read}:")
                for number, link in enumerate(response):
                    print(f"{number+1}. {link}")
    elif args.read is None and args.make: # make a qr code
        if args.link is None and args.file is None:
            print("You are missing data to generate a QR Code from.")
            sys.exit()
        if args.link is not None and args.file is not None:
            print("Please specify only one type of data to generate a QR Code from.")
            sys.exit()
        if args.size is not None:
            try:
                size = int(args.size)
                if size < 100:
                    raise ValueError("too small!")
            except Exception:
                print("Please specify a valid integer size in pixels larger than 100.")
                sys.exit()
        if args.link is None and args.file is not None: # submit a file but it fails
            if not os.path.isfile(args.file):
                print(f"The file {args.file} does not exist.")
                sys.exit()
            else:
                f = open(args.file, "r")
                lines = list(f.read().strip().split("\n"))
                if len(lines) > 1:
                    print(f"The file {args.file} seems to be multiline. Please select a file with one line only, or use -l to directly use a link.")
                    sys.exit()
                else:
                    enc = lines[0]
        elif args.link is not None and args.file is None: #submit a link
            enc = args.link
        if args.embed is not None:
            if not os.path.isfile(args.embed):
                print(f"The file {args.embed} does not exist.")
                sys.exit()
            try:
                with Image.open(args.embed) as img:
                    img.verify()
            except Exception:
                print("Your file does not seem to be a valid image.")
                sys.exit()



