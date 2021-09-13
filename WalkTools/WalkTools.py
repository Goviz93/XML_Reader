"""
 - Custom Module with multiple tools to...
"""
import os
from pathlib import Path
import xml.etree.ElementTree as ET

# Walk trought Directories
def WalkTroughtFiles(FilePath: Path):
    rootList = list()
    localPath = FilePath
    for root, dir, files in os.walk(localPath):
        for file in files:
            # print(os.path.join(root,file))
            if file != None:
                rootList.append(os.path.join(root, file))
    return rootList


# Load XML Path List
def LoadListXML(FilePathList: list):
    xmlList = list()
    for path in FilePathList:
        if path != None:
            OpenedFile = open(path,'rt')
            try:
                myTree = ET.parse(path,OpenedFile)
                myRoot = myTree.getroot()
                xmlList.append(myRoot)
            except SyntaxError:
                OpenedFile = (path)
                print("Syntax Error Founded : ",path)


    return xmlList


# Finder By Node in XML
def FindXMLbyNode(XMList: list,Node:str,KeyWord:str,FilePathList: list):
    localPath = FilePathList
    for xmlroot in XMList:
        index = XMList.index(xmlroot)
        for Search in xmlroot.iter(Node):
            if Search.text == KeyWord:
                for Serial in xmlroot.iter('sn'):
                    print(Serial.text)
                    print(Search.text)
                    print(localPath[index])
                    print("\n")




def FindSpecific(XMList: list,KeyWord:str,FilePathList: list):
    localPath = FilePathList
    for xmlroot in XMList:
        index = XMList.index(xmlroot)
        #for Search in xmlroot.findall(f'.{KeyWord}'):
        for Search in xmlroot.findall('.//'):
            if Search.text == KeyWord:
                print(f' - {Search.tag}: {Search.text}')
                print(localPath[index])
                print('\n')







