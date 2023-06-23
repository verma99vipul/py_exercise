import shutil
import os

source_folder='C:/VS code/sam'
target_folder='C:/VS code/sample'

for dirs,subdirst,files in os.walk(source_folder):
    for file in files:
        if file.endswith(".txt"):
            print(file)
            filename =os.path.join(source_folder,dirs,file)
            if os.path.exists(filename):
                print(filename)
                shutil.copy(filename,target_folder)
print('No. of files transferred : ' , len(os.listdir(target_folder)))