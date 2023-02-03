import os
import datetime
import sys
import shutil
import argparse
import locale
from datetime import datetime


locale.setlocale(locale.LC_TIME, 'es_ES')

parser = argparse.ArgumentParser()
parser.add_argument("sd", help="Source directory")
parser.add_argument("td", help="Target directory")
#parser.add_argument("dn", help="add the date to begint of the file name")
#parser.add_argument("r", help="add the date to begint of the file name")

#print("mddf [source directory] [target directory] \n -dn (add the date to begint of the file name) \n -r (remove string)\n Example: createFolderWithDate.exe -s=\"C:\mi file test\" -m -n -r=file -r=test\" ")
args = parser.parse_args()

if args.sd:    
    src_folder = sys.argv[1]
    tar_folder = sys.argv[2]
    print (tar_folder)
    if(tar_folder!=""):
        tar_folder=src_folder
        
    def move_files(src_folder):
        for dirpath, dirnames, filenames in os.walk(src_folder):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                # Obtener la fecha de modificación del archivo
                modify_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                # Crear la ruta de destino con el nombre del año y mes
                
                dest_folder = os.path.join(tar_folder, modify_date.strftime("%Y"))
                
                # Crear la carpeta de destino si no existe
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                    
                dest_folder = dest_folder + "\\" + modify_date.strftime("%m - %B")
                
                # Crear la carpeta de destino si no existe
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                    
                dest_folder = dest_folder + "\\" + modify_date.strftime("%Y-%m-%d [ %A ]")
                 
                # Crear la carpeta de destino si no existe
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                print ("==========================================")                            
                print ("Moving from: "+file_path+"\\" +file)        
                print ("Moving   to:" +dest_folder+"\\" +file)    
                # Mover el archivo a la carpeta de destino
                shutil.move(file_path, os.path.join(dest_folder, file))


    move_files(src_folder)

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