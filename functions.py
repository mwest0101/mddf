import os
import datetime
import sys
import shutil
import argparse
import locale
from datetime import datetime
import re 
import html
import unicodedata


copiados=0
errores=0
total=0
fileName=""
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
      
      return fecha.start()
   else:
      
      return -1
   
def readRemoveFile():
   try:
      with open(os.getcwd()+'\\remove.list', "r") as file:
         lineas = file.readlines()
   except:
      print ("Can't read : "+os.getcwd()+'\\remove.list')
      
   return lineas
def removeStrs(cadena):
      cadena=cadena.replace("  "," ")
      cadena=cadena.replace("  "," ")
      cadena=cadena.replace("  "," ")
      cadena=cadena.replace("__","_")
      return cadena
   
def cleanStrangeChars(lineas,cadena):
   for linea in lineas:
      #print(removeExtrangeChars(linea))
      cadena=cadena.replace(removeExtrangeChars(linea),"")
      removeStrs(cadena)
    
   
   return cadena
   
def searchRegAndReplace(cadena,cadRegExp):   
   patron = re.compile(cadRegExp)
   fecha = re.search(patron, cadena)
   if fecha:
      cadena=cadena.replace(fecha.group(), '')
   return cadena

def remove_date(cadena):
   cadena=searchRegAndReplace(cadena,"\d{1,2}[/-]\d{1,2}[/-]\d{4} \[.*\]")
   cadena=searchRegAndReplace(cadena,"\d{1,2}[/-]\d{1,2}[/-]\d{4} \(.*\)")
   cadena=searchRegAndReplace(cadena,"\d{1,2}[/-]\d{1,2}[/-]\d{4}")
   cadena=searchRegAndReplace(cadena,"\d{4}[/-]\d{1,2}[/-]\d{1,2} \[.*\]")
   cadena=searchRegAndReplace(cadena,"\d{4}[/-]\d{1,2}[/-]\d{1,2} \(.*\)")
   cadena=searchRegAndReplace(cadena,"\d{4}[/-]\d{1,2}[/-]\d{1,2}")
   cadena=searchRegAndReplace(cadena,"\d{4}[/-]\d{1,2}")                              
   cadena=searchRegAndReplace(cadena,"\d{1,2}[/-]\d{4}")
   return cadena   

def remove_first_char(cadena):
   
   if cadena[0] == "_":
      cadena= cadena[1:]
   
   if cadena[-1] == "_":
      cadena= cadena[:-1]
   
   return cadena
    
def getLastFolder(cadena):
   directory = os.path.dirname(cadena)
   base = os.path.basename(directory)
   return base

def addTextToFile(pathToFile,cadena,printLog):
      try: 
         file = open(pathToFile,'a')
         file.write('\n' + cadena)
         file.close()  
      except:
         if(printLog==True):
            print ("Can't write the file: "+pathToFile)
            print ("With Text: "+cadena)
      


def getHeadHtml():
   cadena="""
   <!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
   <title>MDDF2 Procces Files List</title>
   </head>
      <body>
      <style>
         img {
         max-width: 20rem;
         }
      </style>
         <table class=\"table table-striped-columns\">
            <tr>
               <th>#</th>
               <th>Source path</th>
               <th>Target path</th>
               <th>Status</th>
               <th>Cont</th>
               <th>Image Source</th>
               <th>Image Target</th>
            </tr>"""
   return cadena
def getLineHtml(number,srcPath,tarPath,status,imageSource,imageTarget,strcont):
   print(srcPath)
   cadena=""
   cadena=cadena+"<tr>"
   cadena=cadena+"<td>"+number+"</td>"
   cadena=cadena+"<td>"+escape_html(srcPath)+"</td>"
   cadena=cadena+"<td>"+escape_html(tarPath)+"</td>"
   cadena=cadena+"<td>"+status+"</td>"      
   cadena=cadena+"<td>"+strcont+"</td>" 
   cadena=cadena+"<td><img src=\""+imageSource+"\" ></td>"      
   cadena=cadena+"<td><img src=\""+imageTarget+"\" ></td>"      
   cadena=cadena+"</tr>"
   return cadena
   
def getFooterHtml():
   cadena="""</table>
   </body>
   </html>
   """
   return cadena

def escape_html(text):
   replace_dict = {" ":"&nbsp;","¡":"&iexcl;","¢":"&cent;","£":"&pound;","¤":"&curren;","¥":"&yen;",
                  "¦":"&brvbar;","§":"&sect;","¨":"&uml;","©":"&copy;","ª":"&ordf;","«":"&laquo;",
                  "¬":"&not;","­":"&shy;","®":"&reg;","¯":"&macr;","°":"&deg;","±":"&plusmn;",
                  "²":"&sup2;","³":"&sup3;","´":"&acute;","µ":"&micro;","¶":"&para;","·":"&middot;",
                  "¸":"&cedil;","¹":"&sup1;","º":"&ordm;","»":"&raquo;","¼":"&frac14;","½":"&frac12;",
                  "¾":"&frac34;","¿":"&iquest;","À":"&Agrave;","Á":"&Aacute;","Â":"&Acirc;","Ã":"&Atilde;",
                  "Ä":"&Auml;","Å":"&Aring;","Æ":"&AElig;","Ç":"&Ccedil;","È":"&Egrave;","É":"&Eacute;",
                  "Ê":"&Ecirc;","Ë":"&Euml;","Ì":"&Igrave;","Í":"&Iacute;","Î":"&Icirc;","Ï":"&Iuml;",
                  "Ð":"&ETH;","Ñ":"&Ntilde;","Ò":"&Ograve;","Ó":"&Oacute;","Ô":"&Ocirc;","Õ":"&Otilde;",
                  "Ö":"&Ouml;","×":"&times;","Ø":"&Oslash;","Ù":"&Ugrave;","Ú":"&Uacute;","Û":"&Ucirc;",
                  "Ü":"&Uuml;","Ý":"&Yacute;","Þ":"&THORN;","ß":"&szlig;","à":"&agrave;","á":"&aacute;",
                  "â":"&acirc;","ã":"&atilde;","ä":"&auml;","å":"&aring;","æ":"&aelig;","ç":"&ccedil;",
                  "è":"&egrave;","é":"&eacute;","ê":"&ecirc;","ë":"&euml;","ì":"&igrave;","í":"&iacute;",
                  "î":"&icirc;","ï":"&iuml;","ð":"&eth;","ñ":"&ntilde;","ò":"&ograve;","ó":"&oacute;",
                  "ô":"&ocirc;","õ":"&otilde;","ö":"&ouml;","÷":"&divide;","ø":"&oslash;","ù":"&ugrave;",
                  "ú":"&uacute;","û":"&ucirc;","ü":"&uuml;","ý":"&yacute;","þ":"&thorn;","ÿ":"&yuml;"}

   for char, accented_char in replace_dict.items():
      text = text.replace(char, accented_char)
   return text

def strangeCharToNormalChar(text):
   replace_dict = {"À":"A;","Á":"A","Â":"A","Ã":"A",
                     "Ä":"A","Å":"A","Æ":"A","Ç":"C","È":"E","É":"E",
                     "Ê":"E","Ë":"E","Ì":"I","Í":"I","Î":"I","Ï":"I",
                     "Ð":"D","Ñ":"N","Ò":"O","Ó":"O","Ô":"O","Õ":"O",
                     "Ö":"o","×":"x","Ø":" DIAM ","Ù":"U","Ú":"U","Û":"U",
                     "Ü":"U","Ý":"Y","Þ":"p","ß":"B","à":"a","á":"a",
                     "â":"a","ã":"a","ä":"a","å":"a","æ":"a","ç":"c",
                     "è":"e","é":"e","ê":"e","ë":"e","ì":"i","í":"i",
                     "î":"i","ï":"i","ð":"o","ñ":"n","ò":"o","ó":"o",
                     "ô":"o","õ":"o","ö":"o","÷":" div ","ø":" diam ","ù":"u",
                     "ú":"u","û":"u","ü":"o","ý":"y","þ":"p","ÿ":"y"}

   for char, accented_char in replace_dict.items():
      text = text.replace(char, accented_char)
   return text  
 

   





def moveOrCopyFiles(file_path,rutaArchivo,tar_folder,copy_files,move_files):
   global copiados
   global errores
   global total
   
   total=total+1
   try:            
      if  (move_files):
     

         shutil.move(file_path, rutaArchivo)
         band="Move OK"
         operacion="move"
      
         
      if (copy_files):
        

         shutil.copy(file_path, rutaArchivo)
         band="Copy OK"
         operacion="copy"
      
      copiados=copiados+1
         
         
      
      print("--------------------------------------------------------")
      print("File :"+file_path+" was ")
      print(operacion)
      print("to   :"+rutaArchivo)
      print("--------------------------------------------------------")

   except:
      errores=errores+1
      print ("________________________________________________________________")
      print ("****ERROR*******************************************************")
           
      addTextToFile(tar_folder+'\\'+getFechaHora()+'mddf2_Error_log.txt',"==========================================================",True)                                                
      addTextToFile(tar_folder+'\\'+getFechaHora()+'mddf2_Error_log.txt',"I can't "+operacion+" or copy from: "+file_path,True)
      addTextToFile(tar_folder+'\\'+getFechaHora()+'mddf2_Error_log.txt',"I can't "+operacion+" or copy to  : "+rutaArchivo,True) 
      band="FAIL"                     
      print ("I can't "+operacion+" from : "+file_path)
      print ("I can't "+operacion+" to: "+rutaArchivo)
      print ("****************************************************************")  

def getFechaHora():
   global fileName
   if(fileName==""):
      fecha_y_hora_actual = datetime.now()
      fileName=fecha_y_hora_actual.strftime("%d-%m-%Y_%H-%M-%S_")
   return fileName

def checkIfExist(tar_folder,file_path,rutaArchivo):
   bandFileExists=True
   contFileSameName=0
   try:
      while (bandFileExists):
         bandFileExists=False
                        
         if os.path.exists(rutaArchivo):
            #addTextToFile(src_folder+'\\mddf2_Error_log.txt',"The File exist  : "+rutaArchivo) 
            addTextToFile(tar_folder+'\\'+getFechaHora()+'mddf2_Error_log.txt',"The File exist  : "+rutaArchivo,True) 
            bandFileExists=True
            print("The file exists. : "+rutaArchivo)
            file_name, file_ext = os.path.splitext(rutaArchivo)
                  
            contFileSameName=contFileSameName+1
            rutaArchivo=file_name+"_"+str(contFileSameName)+file_ext
            print ("The File was renamed to: ", rutaArchivo)
            
         else:
            if(contFileSameName>0):
               print ("The new file name is: ", rutaArchivo)
               #addTextToFile(src_folder+'\\mddf2_Error_log.txt',"The new file name is : "+rutaArchivo) 
               addTextToFile(tar_folder+'\\'+getFechaHora()+'mddf2_Error_log.txt',"The new file name is  : "+rutaArchivo,True) 
   except:
      print ("---ERROR--------------------------------------------------------")
      print ("----------------------------------------------------------------")                  
      print ("I can't open from: "+file_path)
      print ("I can't open to : "+rutaArchivo)                  
      print ("----------------------------------------------------------------") 
      
      addTextToFile(tar_folder+'\\'+getFechaHora()+'mddf2_Error_log.txt',"==========================================================",True)                                                
      addTextToFile(tar_folder+'\\'+getFechaHora()+'mddf2_Error_log.txt',"I can't open from: "+file_path,True)
      addTextToFile(tar_folder+'\\'+getFechaHora()+'mddf2_Error_log.txt',"I can't open to : "+rutaArchivo,True)                   
                      
   return rutaArchivo              
                      
def move_files(src_folder,tar_folder,
               move_files,copy_files,create_folder,demo,
               delStrFromFileName,delDateFromFileName,delStrFromFolderName,delDateFromFolderName,
               addDateToFileName,addFolderToFileName,addFolderToNewFolder,
               removeChar,replace):
   cont=0
   
   global copiados
   global errores
   global total
   
   

# Obtener la fecha y hora actual


   if (create_folder or move_files or copy_files):            
      addTextToFile(tar_folder+'\\'+getFechaHora()+'result.html', getHeadHtml(),False)
                       
   for dirpath, dirnames, filenames in os.walk(src_folder):
      for file in filenames:
         file_path = os.path.join(dirpath, file)
         
         newFile=file
         cont=cont+1
         modify_date = datetime.fromtimestamp(os.path.getmtime(file_path))   
         print ("===========================================================================")  
         print ("[ "+str(cont)+" ]")
               
         lastFolder=strangeCharToNormalChar(getLastFolder(file_path))
         
         print("file_path="+file_path)
         print("lastFolder="+lastFolder)

         if (delStrFromFileName==True):
            newFile=cleanStrangeChars(readRemoveFile(),newFile) 
               
         if (delDateFromFileName==True):
            newFile=remove_date(newFile) 

         if (delStrFromFolderName==True):
            lastFolder=cleanStrangeChars(readRemoveFile(),lastFolder) 
                  
         if (delDateFromFolderName==True):
            lastFolder=remove_date(lastFolder) 
                  
         addToNewFile=""
         addToNewFolder=""
         lastFolder=lastFolder.strip()
         if (addDateToFileName==True):               
            addToNewFile=addToNewFile+"_"+modify_date.strftime("%Y-%m-%d")            
            print ("Adding date to filename , addToNewFile = ["+addToNewFile+"]")
                  
         if (addFolderToFileName==True):              
            addToNewFile=addToNewFile+"_"+lastFolder
            print ("Adding folder to filename , addToNewFile = ["+addToNewFile+"]")
                                             
         dest_folder = os.path.join(tar_folder, modify_date.strftime("%Y"))
         
         if(removeChar==True):
            dest_folder=strangeCharToNormalChar(dest_folder)                           
         
         if (move_files or copy_files or create_folder):
            createFolder(dest_folder)
               
         dest_folder = dest_folder + "\\" + modify_date.strftime("%m_(%B)")
         
         if(removeChar==True):
            dest_folder=strangeCharToNormalChar(dest_folder)                                      
         
         if (move_files or copy_files or create_folder):
            createFolder(dest_folder)                  
                 
         dest_folder = dest_folder + "\\" + modify_date.strftime("%Y-%m-%d_(%A)")
            
         newFile=addToNewFile+"_"+newFile
         newFile=removeStrs(newFile)
         
         dest_folder=dest_folder.strip()
         dest_folder=remove_first_char(dest_folder)
         
         newFile=remove_first_char(newFile)
         
         if (move_files):
            print("Moving Files...")
               
         if (copy_files):
            print("Copy Files...")                  
               
         if (create_folder):
            print("Creating Folder... "+dest_folder)
            
         if(removeChar==True):
            dest_folder=strangeCharToNormalChar(dest_folder)                           
         
         if (move_files or copy_files or create_folder):
            createFolder(dest_folder)                     
         
         if (addFolderToNewFolder==True):               
            dest_folder=dest_folder+ "\\" +lastFolder
            print ("Adding folder to ne folder name = ["+dest_folder+"]")
         
         if(removeChar==True):
            dest_folder=strangeCharToNormalChar(dest_folder)    
              
         dest_folder=remove_first_char(dest_folder)
         dest_folder=dest_folder.strip()
         
         print ("dest_folder: "+dest_folder)
         print ("newFile: "+newFile)
         rutaArchivo=os.path.join(dest_folder, newFile)
         
         if(removeChar==True):            
            rutaArchivo=strangeCharToNormalChar(rutaArchivo) 
            # Mover el archivo a la carpeta de destino
         if (move_files or copy_files or create_folder):
            createFolder(dest_folder)    
             

                         
         band="NULL" 
         
         if (demo):
            print("Creating Demo...") 
            
            addTextToFile(tar_folder+'\\'+getFechaHora()+'result.html',getLineHtml(str(cont),file_path,rutaArchivo,"OK",file_path,rutaArchivo,"Tot="+str(total)+"|OK="+str(copiados)+"|ER="+str(errores)),False)
            band="SIMULATION"      
            
         
         if(replace!=True):
            rutaArchivo=checkIfExist(tar_folder,file_path,rutaArchivo)
            
           
         
         
         
         
                
         if (move_files or copy_files):
            
            moveOrCopyFiles(file_path,rutaArchivo,tar_folder,copy_files,move_files)
            
         
         if (create_folder or move_files or copy_files):
            addTextToFile(tar_folder+'\\'+getFechaHora()+'result.html',getLineHtml(str(cont),file_path,rutaArchivo,"OK",file_path,rutaArchivo,"Tot="+str(total)+"|OK="+str(copiados)+"|ER="+str(errores)),False)
         print ("=========================================================================")
         print ("Total= "+ str(total) +" OK= "+ str(copiados)+ " FAILS= "+str(errores))
         print ("=========================================================================")
   if (create_folder or move_files or copy_files):            
      addTextToFile(tar_folder+'\\'+getFechaHora()+'result.html', getFooterHtml(),False)                  
