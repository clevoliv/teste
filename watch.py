import re
import sys


def main():
    #input URL address to be parsed
    print(parse(input("HTML: ")))


def parse(s):

    # search for src= inside the URL
        src = re.search(r'src="([^"]+)"', s)
        # extract the end of the interested URL chunk if inside an iframe
        if src:
            m = src.group(1)
            found = re.search(r'embed/([^/]+)', m)
        # extract the end of the interested URL chunk if is embedded by youtube
            if found:
                #returns the complete result
                return ("https://youtu.be/"+found.group(1))
        #returns result for a link inside of iframe but not youtube
            return found
        #returns result for a link outside of iframe
        return src



if __name__ == "__main__":
    main()