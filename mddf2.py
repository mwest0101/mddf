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
#def move_files(src_folder,tar_folder,
# delStrFromFileName,delDateFromFileName,delStrFromFolderName,delDateFromFolderName,
# addDateToFileName,addFolderToFileName,addFolderToNewFolder):

parser = argparse.ArgumentParser()
parser.add_argument("sd", help="Source directory")
parser.add_argument("td", help="Target directory")
parser.add_argument('-m',   '--move_file',     action='store_true', help='move files')
parser.add_argument('-c',   '--copy_file',     action='store_true', help='copy files')
parser.add_argument('-f',   '--create_folder', action='store_true', help='create folders')
parser.add_argument('-d',   '--demo',          action='store_true', help='Create a html output')
parser.add_argument('-dsf', '--delStringFilename', action='store_true', help='Delete String in file name, remove the strings in ("remove.list" file)')
parser.add_argument('-ddf', '--delDateFilename', action='store_true',   help='Delete date string from target flename')
parser.add_argument('-dsd', '--delStringDirectory', action='store_true', help='Delete string in directory name, remove the string in(default: "remove.list")')
parser.add_argument('-ddd', '--delDateDirectory', action='store_true',  help='Delete date string  from target directory(if source directory was added)')



parser.add_argument('-adf', '--addDateToFileName',      action='store_true',    help='Add date to filename')
parser.add_argument('-aff', '--addFolderToFileName',    action='store_true',   help='Add folder to filename')
parser.add_argument('-afd', '--addFolderToNewFolder',   action='store_true',   help='Add source folder to new folder name')
parser.add_argument('-rmc', '--removeChar',             action='store_true',   help='Remove a normalize strange char')
parser.add_argument('-rep', '--replace',             action='store_true',   help='Replace files, (Autorename by default) ')

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
  
    move_files(src_folder,tar_folder,
               args.move_file,args.copy_file,args.create_folder,args.demo,
               args.delStringFilename,args.delStringFilename,args.delStringDirectory,args.delDateDirectory,
               args.addDateToFileName,args.addFolderToFileName,args.addFolderToNewFolder,
               args.removeChar,args.replace)
    