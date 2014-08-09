# Author: AbhishekSolanki
import os

def main():
    file_obj=open("file.txt","r")
    list_dir=[]
    #print file_obj.read()

    for i in file_obj:
        dir_name=i.strip()
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

if __name__=='__main__':
    main()
