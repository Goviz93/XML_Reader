import os
from pathlib import Path
from bs4 import BeautifulSoup
from Tools.Classes.FileTools import FileAttr
from Tools.DUTs import DUT_Classes as DUT



class xmlReader:


    #Constructor
    def __init__(self):
        self.Filepath = ''


    #Methods
    def ReadSingleXML(self,filepath:Path):
        ValidPath = os.path.isfile(filepath)
        if ValidPath == True:

            with open(filepath) as xml:
                try:
                    print("Readed File : ", filepath)
                    Soup = BeautifulSoup(xml, "lxml")
                    for node in Soup:
                        print(f'{node}')

                except SyntaxError:
                    print("Syntax Error Founded : ", filepath)

        else:
            print(f'The following path isn´t a valid file -> {filepath} ')



    def CountMatchFilesByType(self, DirPath:Path, MatchWord:str,ReturnPaths:bool=False):
        ValidPath = os.path.isdir(DirPath)
        if ValidPath == True:

            returnPaths = list()
            FileNumber = 0

            FT = FileAttr(DirPath)
            PathList = FT.GetPaths(DirPath,True,0)
            for file in PathList:
                with open(file) as xml:
                    try:
                        Soup = BeautifulSoup(xml, "lxml")
                        for node in Soup:
                            FileType = node.signal
                            try:
                                if FileType.string == MatchWord:
                                    FileNumber += 1
                                    returnPaths.append(DUT.File_DUT(FileNumber,os.path.basename(file),file))
                            except AttributeError:
                                 print("AttributeError Error Founded : ", file)

                    except SyntaxError:
                        print("Syntax Error Founded : ", file)

            print(f'Matches Found With -{MatchWord}- : {FileNumber}')
            if ReturnPaths :
                return returnPaths