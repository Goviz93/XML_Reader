
import os
from pathlib import Path
from bs4 import BeautifulSoup
from Tools.Classes.FileTools import FileAttr
from Tools.Classes.xmlTools import xmlReader





filePath = Path(r'C:\Users\Gonzalo.Vizcaino\Desktop\Testing_Python\FlexFlow_Files\BRC_Flexflow_st300')


Signals_Tuple =('opcmtreq','opcmtres','rtchkreq','rtchkres')
n = 0

ListofPaths = list()
FileNumber = 0

FileName = 'opcmtreq_11-01-2021  16.07.13.164.xml'



"""
 All functions
"""

FT = FileAttr(filePath)

#FT.TotalFiles(filePath)
#FT.SeachFileByName(filePath,FileName)
#FT.SeachEmptyFiles(filePath)
#AllPaths = FT.GetPaths(filePath,True, 10)
#for index, route in  enumerate(AllPaths):
#    print(f'{index} -> {route}')


path2 = Path(r'C:\Users\Gonzalo.Vizcaino\Desktop\Testing_Python\FlexFlow_Files\BRC_Flexflow_st300\27X210106680\opcmtreq_11-01-2021  16.07.13.164.xml')
RXML = xmlReader()
#RXML.ReadSingleXML(path2)
#Arr = RXML.CountMatchFilesByType(filePath,'opcmtreq',True)
#for route in Arr:
#    print(route)

Arr = RXML.SearchText(filePath,'OK',True)
for route in Arr:
    print(route)

