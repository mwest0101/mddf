import os
import datetime
import sys
import shutil
import argparse
import locale
from datetime import datetime
import re 

locale.setlocale(locale.LC_ALL, '')

def createFolder(cadena_folder):
   try:                  
      if not os.path.exists(cadena_folder):
         os.makedirs(cadena_folder)
   except:
      print ("Can't Create Folder : "+cadena_folder)
      
def removeExtrangeChars(cadena):
   cadena=cadena.replace("\r","")
   cadena=cadena.replace("\n","")
   cadena=cadena.replace("\t","")
   cadena=cadena.replace(" ","")
   
   return cadena

def buscar_fecha(cadena):
   patron = re.compile('\d{1,2}[/-]\d{1,2}[/-]\d{4}')
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

   
def searchRegAndReplace(cadena,cadRegExp):   
   patron = re.compile(cadRegExp)
   fecha = re.search(patron, cadena)
   if fecha:
      cadena=cadena.replace(fecha.group(), '')
   return cadena


def remove_date(cadena):
   cadena=searchRegAndReplace(cadena,"\d{1,2}[/-]\d{1,2}[/-]\d{4} \[.*\]")
   cadena=searchRegAndReplace(cadena,"\d{1,2}[/-]\d{1,2}[/-]\d{4}")
   cadena=searchRegAndReplace(cadena,"\d{4}[/-]\d{1,2}[/-]\d{1,2} \[.*\]")
   cadena=searchRegAndReplace(cadena,"\d{4}[/-]\d{1,2}[/-]\d{1,2}")
   cadena=searchRegAndReplace(cadena,"\d{4}[/-]\d{1,2}")                              
   cadena=searchRegAndReplace(cadena,"\d{1,2}[/-]\d{4}")

   return cadena   


def remove_first_char(string):
    if string[0] == "_":
        return string[1:]
    return string
    
def getLastFolder(cadena):
   directory = os.path.dirname(cadena)
   base = os.path.basename(directory)
   return base

def move_files(src_folder,tar_folder,
               move_files,copy_files,create_folder,
               delStrFromFileName,delDateFromFileName,delStrFromFolderName,delDateFromFolderName,
               addDateToFileName,addFolderToFileName,addFolderToNewFolder):
   
        for dirpath, dirnames, filenames in os.walk(src_folder):
            for file in filenames:
               file_path = os.path.join(dirpath, file)
               newFile=file
               print ("===========================================================================")  
               
               lastFolder=getLastFolder(file_path)
               
               print("file_path="+file_path)
               print("lastFolder="+lastFolder)
                # --------------------------------------------------               
               # -----DELETE----
               
                # Delete string contained in the file "removeStrFromFiles" 
               # from the file name
               if (delStrFromFileName==True):
                  newFile=cleanStrangeChars(readRemoveFile(),newFile) 
               
               # Delete the date from the file name                         
               if (delDateFromFileName==True):
                  newFile=remove_date(newFile) 

               # Delete string contained in the file "removeStrFromFiles" 
               # from the folder name                     
               if (delStrFromFolderName==True):
                  lastFolder=cleanStrangeChars(readRemoveFile(),lastFolder) 
                  
               # Delete the date from the folder name                                              
               if (delDateFromFolderName==True):
                  lastFolder=remove_date(lastFolder) 
                  
               # --------------------------------------------------                  
               # ------------------ADD-----------------------------
               # Add de date to the start of file name
               addToNewFile=""
               addToNewFolder=""
               
               if (addDateToFileName==True):   
                  print ("Adding date = [ "+modify_date.strftime("%Y-%m-%d")+" ] to file name")
                  addToNewFile=addToNewFile+"_"+modify_date.strftime("%Y-%m-%d")
                  

               # Add de original folder name to the begin of the new file name
               if (addFolderToFileName==True):  
                  print ("Adding last folder = [ "+lastFolder+" ] to file name")
                  addToNewFile=addToNewFile+"_"+lastFolder
                                             
               # Add de original folder name to the begin of the new folder name
               if (addFolderToNewFolder==True):   
                  print ("Adding last folder = [ "+lastFolder+"  ] to folder name")
                  addToNewFolder=addToNewFolder+"_"+lastFolder
                  
              
               
               modify_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                
               dest_folder = os.path.join(tar_folder, modify_date.strftime("%Y"))
               
               
               if (move_files or copy_files or create_folder):
                  createFolder(dest_folder)
                  
                    
               dest_folder = dest_folder + "\\" + modify_date.strftime("%m - %B")
               
               if (move_files or copy_files or create_folder):
                  createFolder(dest_folder)                  
                    
               dest_folder = dest_folder + "\\" + modify_date.strftime("%Y-%m-%d [ %A ]")
               
               
                #concateno y creo ruta destino y nombre de archivo destino completo 
               newFile=addToNewFile+newFile
               dest_folder=dest_folder+addToNewFolder
               dest_folder=dest_folder.strip()
               dest_folder=remove_first_char(dest_folder)
               
               newFile=remove_first_char(newFile)
               if (move_files or copy_files or create_folder):
                  createFolder(dest_folder)                     
               
               
    
               if (move_files):
                  print("Moving Files...")
                  
               if (copy_files):
                  print("Copy Files...")                  
                  
               if (create_folder):
                  print("Creating Folder...")
                                       
               print ("from: "+file_path)        
               print ("to:" +dest_folder+"\\" +file)    
               # Mover el archivo a la carpeta de destino
               if (move_files or copy_files):
                  try:            
                     if  (move_files):
                        shutil.move(file_path, os.path.join(dest_folder, newFile))
                     if (copy_files):
                        shutil.copy(file_path, os.path.join(dest_folder, newFile))
                  except:
                     f1 = open(src_folder+'\mddf2_move_log.txt','a')
                     f1.write('\n' + "I can't move or copy from: "+file_path+"\\" +file)
                     f1.write('\n' + "I can't move or copy to  : "+dest_folder+"\\" +newFile)
                     f1.close()  
                     
                     f2 = open(tar_folder+'\mddf2_move_log.txt','a')
                     f2.write('\n' + "I can't move or copy from: "+file_path+"\\" +file)
                     f2.write('\n' + "I can't move or copy to  : "+os.path.join(dest_folder, newFile))
                     
                     f2.close()                    
                     print ("I can't move or copy: "+file_path+"\\" +file)
                  
                  
