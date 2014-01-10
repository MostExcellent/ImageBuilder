#!/usr/bin/python

from binascii import unhexlify
from PIL import Image
 
if __name__ == "__main__":
	lit = raw_input("Hex string? ") 
	width = raw_input("Width? ")
	height = raw_input("Height? ")
	typecode = raw_input("Enter the code of the mode you want: ")
	if typecode != "1" and typecode != "L" and typecode != "P" and typecode != "RGB" and typecode != "RGBA" and typecode != "CMYK" and typecode != "YCbCr" and typecode != "I" and typecode != "F":
		print "Invalid typecode - defaulting to RGB"
	width = int(width)
	height = int(height)
	filename = raw_input("What do you want the filename to be? ")
	arr = unhexlify(lit)
	arr += " " * (width * height * 3 - len(arr))
	img = Image.fromstring(typecode, (width, height), arr)
	img.save(filename)
	print "Saved %s successfully" % filename
	print "Most magical!"