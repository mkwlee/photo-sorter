from PIL import Image, ImageFilter
from pillow_heif import HeifImagePlugin
import imageio.v3 as imageio
import os, sys
import shutil
from helper import months_dict, get_progress_bar, count_total_elements

baseDir = os.listdir(sys.argv[1])
listFolders = []
for x in baseDir:
    listFolders.append(os.listdir(sys.argv[1]+'/'+x))
# listFiles = os.listdir(sys.argv[1])
totalFiles = count_total_elements(listFolders)
print('Sorting...\n')
count = 1
for index, folder in enumerate(listFolders):
    for file in folder:
        print("\033[A                             \033[A")
        print(str(count) + '/' + str(totalFiles), get_progress_bar(count, totalFiles))
        count+=1
        # print(sys.argv[1]+baseDir[index]+'/'+file)
        try:
            metadata = imageio.immeta(sys.argv[1]+'/'+baseDir[index]+'/'+file)
            possible_date_keys = ['datetime', 'creation_time', 'date', 'timestamp', 'DateTime']
            correct_key = None
            for key in possible_date_keys:
                if key in metadata:
                    correct_key = key
                    break
            if correct_key is not None:
                listDate = (metadata[correct_key][:7]).split(':')
                if len(listDate) == 1:
                    listDate = listDate[0].split('-')
                strDateDir = listDate[0] + '/' + listDate[1] + months_dict[listDate[1]] + '/'
                if not os.path.exists('output/' + strDateDir):
                    os.makedirs('output/'+strDateDir)
                shutil.move(sys.argv[1]+'/'+baseDir[index]+'/'+file, 'output/'+strDateDir+file)
            else:
                if not os.path.exists('output/undated'):
                    os.makedirs('output/undated')
                shutil.move(sys.argv[1]+'/'+baseDir[index]+'/'+file, 'output/undated/'+file)
        except Exception as e:
            pass
