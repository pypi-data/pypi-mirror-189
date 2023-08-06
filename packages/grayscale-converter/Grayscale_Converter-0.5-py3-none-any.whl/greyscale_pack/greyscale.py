from PIL import Image
import matplotlib.pyplot as plt
import sys
import os

def main():
    if len(sys.argv) != 3:
        print("ERROR : NUMBER OF PARAMETERS")
        print("USAGE : python greyscale inputfilepath fileformat")
        exit(1)
    
    elif not os.path.isfile(sys.argv[1]):
        print(f"ERROR : {sys.argv[1]} Don't exist!!")
        exit(1)
    
    if os.path.splitext(sys.argv[1])[1] not in [".jpeg", ".png",".jpg"]:
        print(f"ERROR : {(os.path.splitext(sys.argv[1]))[1]} is not jpeg or png!!")
        exit(1)

    if sys.argv[2] not in ["png","jpeg","jpg"]:
        print("ERROR: specified file not in JPG, JPEG or PNG format")

    else:
        img = Image.open(sys.argv[1])
        #img.show()
        filename = os.path.basename(sys.argv[1])
        name, ext= os.path.splitext(filename)
        ext = sys.argv[2]
        grayScale = img.convert('L')

        output_filename = f"greyscaled_{name}.{ext}"
        grayScale.save(output_filename)

if __name__ == "__main__":
    main()