import os
import datetime
import sys
import shutil
import argparse
import locale
from datetime import datetime
from functions import *


#locale.setlocale(locale.LC_TIME, 'es_ES')
locale.setlocale(locale.LC_ALL, '')

parser = argparse.ArgumentParser()
parser.add_argument("sd", help="Source directory")
parser.add_argument("td", help="Target directory")
parser.add_argument('-ds', '--delstr', action='store_true', help='delete str in directories and files')
parser.add_argument('-dd', '--deldate', action='store_true', help='delete date str in directories and files')
parser.add_argument('-anf', '--addNameFolderToFolder', action='store_true', help='add name folder to new folder name')
parser.add_argument('-and', '--addNameFolderToFile', action='store_true',   help='add name folder to new file name')


#parser.add_argument("dn", help="add the date to begint of the file name")
#parser.add_argument("r", help="add the date to begint of the file name")

#print("mddf [source directory] [target directory] \n -dn (add the date to begint of the file name) \n -r (remove string)\n Example: createFolderWithDate.exe -s=\"C:\mi file test\" -m -n -r=file -r=test\" ")
args = parser.parse_args()

if args.sd:    
    src_folder = sys.argv[1]
    tar_folder = sys.argv[2]
    print (tar_folder)
    if(tar_folder==""):
        tar_folder=src_folder
  
    move_files(src_folder,tar_folder,args.deldate,args.delstr,args.addNameFolderToFolder,args.addNameFolderToFile)
    



# for dirpath, dirnames, filenames in os.walk(root_dir):
#     for filename in filenames:
#         file_path = os.path.join(dirpath, filename)
#         file_ctime = os.path.getctime(file_path)
#         file_ctime_date = datetime.datetime.fromtimestamp(file_ctime).date()
#         year = file_ctime_date.year
#         month = file_ctime_date.month
#         new_folder_name = f"{year}-{month}"
#         new_folder_path = os.path.join(dirpath, new_folder_name)
#         os.makedirs(new_folder_path, exist_ok=True)
#         new_file_path = os.path.join(new_folder_path, filename)
#         os.rename(file_path, new_file_path)