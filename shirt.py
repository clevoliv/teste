#import libraries
import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():

    #start variables
    images = []
    extensions = (".jpg","jpeg",".png")
    imd = "shirt.png"

    #validation of minimum requirements, if true resume
    args_checker()

    filename = splitext(sys.argv[1])
    filename1 = splitext(sys.argv[2])

    #validation of minimum requirements, if true resume
    extension_checker(filename,filename1,extensions)

    try:
        imagefile =  Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    #open shirt
    shirt = Image.open("shirt.png")
    #get file size
    size = shirt.size
    #resize muppet size
    mup = ImageOps.fit(imagefile, size)
    #past shirt in muppet
    mup.paste(shirt,shirt)
    #save result
    mup.save(sys.argv[2])



def args_checker():

    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")

    return True


def extension_checker(filename,filename1,extensions):


    if  filename[1].lower() != filename1[1].lower():
        sys.exit("Input and Output have different extensions")

    if  not filename[1].lower() in extensions or not filename1[1].lower() in extensions:
        sys.exit("Not a valid format")

    return True


if __name__ == "__main__":
    main()