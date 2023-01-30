import os
import shutil

fromdir = "C:/Users/HI User/Downloads"
todir = "C:/Users/HI User/Downloads/documents102"

list_files = os.listdir(fromdir)
# print(list_files)

for i in list_files:
    root, extension = os.path.splitext(i)
    if extension == "":
        continue
    if extension in ['.docx','.pdf']:
        path1 = fromdir + '/' + i
        path2 = todir + '/' + 'doc'
        path3 = todir + '/' + 'doc' + '/' + i
        if os.path.exists(path2):
            print("moving " + i + "... ")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving " + i + "... ")
            shutil.move(path1,path3)
