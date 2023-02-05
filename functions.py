import os
import datetime
import sys
import shutil
import argparse
import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, '')

def createFolder(cadena_folder):
   if not os.path.exists(cadena_folder):
                  os.makedirs(cadena_folder)
                  
def removeExtrangeChars(cadena):
   cadena=cadena.replace("\r","")
   cadena=cadena.replace("\n","")
   cadena=cadena.replace("\t","")
   cadena=cadena.replace(" ","")
   
   return cadena

def buscar_fecha(cadena):
   patron = re.compile(r'\d{1,2}[/-]\d{1,2}[/-]\d{4}')
   fecha = re.search(patron, cadena)
   if fecha:
      print(fecha.group())
      return fecha.start()
   else:
      print("not found")
      return -1
   
def readRemoveFile():
   with open(os.getcwd()+'\\removeStrFromFiles.list', "r") as file:
      lineas = file.readlines()
   return lineas

def cleanStrangeChars(lineas,cadena):
   for linea in lineas:
      print(removeExtrangeChars(linea))
      cadena=cadena.replace(removeExtrangeChars(linea),"")
   cadena=cadena.replace("  "," ")
   cadena=cadena.replace("  "," ")
   cadena=cadena.replace("  "," ")
   return cadena

   

def remove_date(cadena):
   patron = re.compile(r'\d{1,2}[/-]\d{1,2}[/-]\d{4}')
   fecha = re.search(patron, cadena)
   if fecha:
      #print("encontre "+fecha.group())
      cadena=cadena.replace(fecha.group(), '')
   return cadena   
   
   
def move_files(src_folder,tar_folder,deldate,delstr,addNameFileToNewNameFile,addNameFileToD):
   
        for dirpath, dirnames, filenames in os.walk(src_folder):
            for file in filenames:
               file_path = os.path.join(dirpath, file)
               modify_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                
               dest_folder = os.path.join(tar_folder, modify_date.strftime("%Y"))
               createFolder(dest_folder)
                    
               dest_folder = dest_folder + "\\" + modify_date.strftime("%m - %B")
               createFolder(dest_folder)
                    
               dest_folder = dest_folder + "\\" + modify_date.strftime("%Y-%m-%d [ %A ]")
               
               newFile=file
               
                  
               if (delStrFromFileName==True):
                  newFile=filterFolderFile(newFile) 
                     
               if (delStrFromFolderName==True):
                  dest_folder=filterFolderFile(dest_folder) 
                  
               if (delDateFromFileName==True):
                  newFile=remove_date(newFile) 
                     
               if (delDateFromFolderName==True):
                  dest_folder=remove_date(dest_folder) 
                     
               createFolder(dest_folder)
               
               print ("==========================================")                            
               print ("Moving from: "+file_path)        
               print ("Moving   to:" +dest_folder+"\\" +file)    
               # Mover el archivo a la carpeta de destino
               try:
           
                     
                  shutil.move(file_path, os.path.join(dest_folder, newFile))
               except:
                  f = open(src_folder+'\mddf2_move_log.txt','a')
                  f.write('\n' + "I can't move: "+file_path+"\\" +file)
                  f.close()                    
                  print ("I can't move: "+file_path+"\\" +file)
                  
                  
