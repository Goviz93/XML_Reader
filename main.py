"""
    This code was created to find the following
    info inside of all Flexflow's XML files:
        - Serial Numbers.
        - Pass / Fail Status.
        - Invalid Routes.
        - Route check REQUEST.
        - Route check RESPONSE.
        - Commit REQUEST.
        - Commit RESPONSE.

    Version: 1.0
    Date: 1/21/2021
    Author: GVR.
"""

import os
from pathlib import Path,PurePath
from Tools import WalkTools as Tool

#Set the Folder root.
filePath = Path(r'C:\Users\Gonzalo.Vizcaino\Desktop\Testing_Python\FlexFlow_Files\BRC_Flexflow_st300')
#filePath = Path(r"C:\Users\Gonzalo.Vizcaino\Desktop\BRC_Flexflow_st300")

#Create an empty list.
PathList = list()

#Call Walktrought Function to get all paths.
PathList = Tool.WalkTroughtFiles(filePath)

xmlList = list()
#Call XML parse function
xmlList = Tool.LoadListXML(PathList)

#Call XML node Finder
node = "chkres"
keyWord = input("Type text to find: ")
#Tool.FindXMLbyNode(xmlList,node,keyWord,PathList)
Tool.FindSpecific(xmlList,keyWord,PathList)


