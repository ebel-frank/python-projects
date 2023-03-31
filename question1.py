#Write a python program zip.py to create a zip file.
#The program should take name of zip file as first
#argument and files to add as rest of the arguments.

import zipfile
import os
os.chdir('C:\\Users\\ebeledike\\Desktop')

name = input("Enter a name: ")
file1 = input("Enter file1: ")
file2 = input("Enter file2: ")
file3 = input("Enter file3: ")

name += ".zip"

def Zip(name, file1, file2, file3):
    z = zipfile.ZipFile(name, 'w')
    z.writestr(file1, data="")
    z.writestr(file2, data="")
    z.writestr(file3, data="")
    z.close()

if __name__ == '__main__':
    Zip(name, file1, file2, file3)
