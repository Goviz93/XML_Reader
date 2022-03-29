
from pathlib import Path
from Classes.FileTools import FileAttr
from Classes.xmlTools import xmlReader





filePath = Path(r'C:\Users\Gonzalo.Vizcaino\OneDrive - Bright Machines\Desktop\GenFlexFlow\IoT\Product')


Signals_Tuple =('opcmtreq','opcmtres','rtchkreq','rtchkres')
n = 0

ListofPaths = list()
FileNumber = 0

FileName = 'opcmtres_28-03-2022  12.30.04.042.xml'



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


#path2 = Path(r'C:\Users\Gonzalo.Vizcaino\Desktop\Testing_Python\FlexFlow_Files\BRC_Flexflow_st300\27X210106680\opcmtreq_11-01-2021  16.07.13.164.xml')
RXML = xmlReader()
#RXML.ReadSingleXML(path2)
Arr = RXML.CountMatchFilesByType(filePath,Signals_Tuple[2],True)
for route in Arr:
    print(route)

"""
Arr = RXML.SearchText(filePath,'112180LP8,00219 220323',True)
for route in Arr:
    print(route)
"""
