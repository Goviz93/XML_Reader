
import os
from pathlib import Path
from bs4 import BeautifulSoup
from xmlTools import FileAttr






filePath = Path(r'C:\Users\Gonzalo.Vizcaino\Desktop\Testing_Python\FlexFlow_Files\BRC_Flexflow_st300')

Signals_Tuple =('opcmtreq','opcmtres','rtchkreq','rtchkres')
n = 0




ListofPaths = list()
FileNumber = 0

for root,dir,files in os.walk(filePath):
    for file in files:
        # print(os.path.join(root,file))
        if file != None:
            #print(f' Nombre -> {(os.path.join(root, file))}')
            ListofPaths.append((os.path.join(root, file)))
            FileNumber += 1
print(f'Total de archivos encontrados -> {FileNumber}')
print(f'Nombre del archivo --> {ListofPaths[n]}')



with open(ListofPaths[n]) as xml:
    try:
        Soup = BeautifulSoup(xml,"lxml")
        for node in Soup:
            FileType = node.signal
            print(f'Tipo de Archivo : {FileType.contents[0]}')


        #print(Soup.find_parent('signal'))


    except SyntaxError:
        print("Syntax Error Founded : ", ListofPaths[n])

FileName = 'opcmtreq_11-01-2021  16.07.13.164.xml'

FileTools = FileAttr(filePath)

#FileTools.TotalFiles(filePath)
#FileTools.SeachFileByName(filePath,FileName)
FileTools.SeachEmptyFiles(filePath)