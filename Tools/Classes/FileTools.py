import os
from pathlib import Path
from bs4 import BeautifulSoup
from Tools.DUTs import DUT_Classes as DUT


class FileAttr:

    #Constructor
    def __init__(self, filepath:Path):
        self.Filepath = filepath


    #Methods
    def TotalFiles(self,filepath):
        self.Filepath = filepath
        ListofPaths = list()
        FileNumber = 0

        for root,dir,files in os.walk(self.Filepath):
            for file in files:
                if file != None:
                    ListofPaths.append((os.path.join(root, file)))
                    FileNumber += 1
        print(f'Total Number of Files -> {FileNumber}')
        return FileNumber


    def SeachFileByName(self,filepath, filename):
        self.Filepath = filepath
        ListofMatches = list()
        FileNumber = 0

        for root,dir,files in os.walk(self.Filepath):
            for file in files:
                if file != None:
                    if file == filename:
                        FileNumber += 1
                        filePath = ((os.path.join(root, file)))
                        Match = DUT.File_DUT(FileNumber, file, filePath)
                        ListofMatches.append(Match)
                        print(f'ID - {Match.ID}) Name : {Match.FileName} | Path -> {Match.Filepath}')
        return ListofMatches


    def SeachEmptyFiles(self,filepath):
        self.Filepath = filepath
        ListOfFiles = list()
        FileNumber = 0

        for root,dir,files in os.walk(self.Filepath):
            for file in files:
                if file != None:
                    filePath = ((os.path.join(root, file)))
                    if os.stat(filePath).st_size == 0:
                        FileNumber += 1
                        Match = DUT.File_DUT(FileNumber, file, filePath)
                        ListOfFiles.append(Match)
                        print(f'ID - {Match.ID}) Name : {Match.FileName} | Path -> {Match.Filepath}')
                    else:
                        with open(filePath,'r') as F:
                            FirstChar = F.read(100)
                            if not FirstChar:
                                FileNumber += 1
                                Match = DUT.File_DUT(FileNumber, file, filePath)
                                ListOfFiles.append(Match)
                                print(f'ID - {Match.ID}) Name : {Match.FileName} | Path -> {Match.Filepath}')
        return ListOfFiles



    def GetPaths(self,filepath):
        self.Filepath = filepath
        ListOfFiles = list()

        for root,dir,files in os.walk(self.Filepath):
            for file in files:
                if file != None:
                    filePath = ((os.path.join(root, file)))
                    ListOfFiles.append(filePath)
        return ListOfFiles