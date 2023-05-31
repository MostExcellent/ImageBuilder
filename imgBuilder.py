from binascii import unhexlify
from PIL import Image
import argparse

def get_valid_typecode(typecode):
    valid_typecodes = ["1", "L", "P", "RGB", "RGBA", "CMYK", "YCbCr", "I", "F"]
    if typecode in valid_typecodes:
        return typecode
    print("Invalid typecode - Defaulting to RGB")
    return "RGB"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Read hex string from a file")
    parser.add_argument("-t", "--typecode", help="Specify the typecode")
    parser.add_argument("-w", "--width", type=int, help="Specify the width")
    parser.add_argument("-h", "--height", type=int, help="Specify the height")
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as file:
            lit = file.read().strip()
    else:
        lit = input("Hex string? ")

    width = args.width if args.width else int(input("Width? "))
    height = args.height if args.height else int(input("Height? "))
    typecode = get_valid_typecode(args.typecode) if args.typecode else "RGB"

    filename = input("What do you want the filename to be? ")

    arr = unhexlify(lit)
    arr += b" " * (width * height * 3 - len(arr))

    img = Image.frombytes(typecode, (width, height), arr)
    img.save(filename)

    print(f"Saved {filename} successfully.")
    print("Most magical!")
