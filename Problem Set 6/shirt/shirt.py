from PIL import Image
from PIL import ImageOps
import sys
import os

def main():
    check()

    try:
        img = Image.open(sys.argv[1], mode='r', formats=None)
        shirt_img = Image.open('shirt.png', mode='r', formats=None)
        shirt_size = shirt_img.size
        crop = ImageOps.fit(img, shirt_size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        crop.paste(shirt_img, box=shirt_img)
        crop.save(sys.argv[2])
    except:
        sys.exit('File does not exist')

def check():
    if len(sys.argv) > 3:
        sys.exit('Too many arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few arguments')

    split_one = os.path.splitext(sys.argv[1])
    split_two = os.path.splitext(sys.argv[2])

    if split_one[1] not in ['.png', '.jpg', 'jpeg']:
        sys.exit('Not a valid extension')
    if split_two[1] not in ['.png', '.jpg', 'jpeg']:
        sys.exit('Not a valid extension')
    if split_one[1] != split_two[1]:
        sys.exit('Extensions do not match')

if __name__ == '__main__':
    main()