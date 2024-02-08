import os
import sys
from PIL import Image
from helper import months_dict

listFiles = os.listdir(sys.argv[1])

for file in listFiles:
    image = Image.open(sys.argv[1]+'/'+file)
    dictExif = image.getexif()
    if 306 in dictExif:
        listDate = (dictExif[306][:7]).split(':')
        strDateDir = listDate[0]+'/'+months_dict[listDate[1]]+'/'
        print(file, strDateDir)
        if not os.path.exists('output/'+strDateDir):
            os.makedirs('output/'+strDateDir)
        image.save('output/'+strDateDir+file)

