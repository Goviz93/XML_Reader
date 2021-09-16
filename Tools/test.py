
import os
from pathlib import Path
from bs4 import BeautifulSoup
from Tools.Classes.FileTools import FileAttr





filePath = Path(r'C:\Users\Gonzalo.Vizcaino\Desktop\Testing_Python\FlexFlow_Files\BRC_Flexflow_st300')

Signals_Tuple =('opcmtreq','opcmtres','rtchkreq','rtchkres')
n = 0

ListofPaths = list()
FileNumber = 0

"""
with open(ListofPaths[n]) as xml:
    try:
        Soup = BeautifulSoup(xml,"lxml")
        for node in Soup:
            FileType = node.signal
            print(f'Tipo de Archivo : {FileType.contents[0]}')


        #print(Soup.find_parent('signal'))


    except SyntaxError:
        print("Syntax Error Founded : ", ListofPaths[n])

"""
FileName = 'opcmtreq_11-01-2021  16.07.13.164.xml'





FT = FileAttr(filePath)

#FT.TotalFiles(filePath)
#FT.SeachFileByName(filePath,FileName)
FT.SeachEmptyFiles(filePath)