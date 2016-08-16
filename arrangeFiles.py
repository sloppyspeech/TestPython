#touch 1.zip 2.zip 3.zip 4.zip 6.mp3 7.zip 9.docx 10.doc 12.xml 14.xml 1.txt 2.txt 3.txt 1.mp3 2.mp3 3.mp3
#find . -depth 1 -name \* -exec touch ../Documents/LearnPy/TestMisc2.7/SunDry/{} \;
import sys
import os
import shutil
import re
import datetime as dt

fileDir = {"mp3": "Music",
           "txt": "Documents", "csv":"Documents",
           "zip": "Archive", "tar": "Archive","gz":"Archive",
           "mp4": "Videos",
           "pdf": "Documents/Books","epub": "Documents/Books", "mobi": "Documents/Books","azw3":"Documents/Books",
           "xml":"Xml",
           "doc":"MSDocs","docx":"MSDocs","xls":"MSDocs","xlsx":"MSDocs","pptx":"MSDocs","ppt":"MSDocs",
           "torrent":"Torrents",
           "dmg":"Software","pkg":"Software",
           "jpg":"Photos","svg":"Photos","bmp":"Photos","jpeg":"Photos","png":"Photos",
           "js":"Javascript",
           "exe":"Windows_exes",
           "mpp":"MSProject"
           }

def dbg(isOn=False,par="",val=""):
    if isOn:
        print "["+str(dt.datetime.now())+"] ["+ str(par) + "] : ["+ str(val) +"]"

def printFiles():
    srcDir=str(sys.argv[1])
    debug=str(sys.argv[2])
    trgDirName="testo"

    if srcDir.strip() == None:
        srcDir="."
    if debug.strip() == None:
        debug=False
    else:
        debug=True

    files = os.listdir(srcDir)

    for file in files:
        ext=str(os.path.splitext(file)[1]).replace('.','')
        srcFile=srcDir+"/"+file
        dbg(debug, "Current File ["+file+"] fullPath", srcFile )
        if ext in fileDir.keys():
            trgDir=srcDir+'/'+trgDirName+'/'+fileDir[ext]
            dbg(debug, "Checking existence of Dir", trgDir)
            if not(os.access(trgDir,os.F_OK)):
                dbg(debug,"Dir ["+trgDir+"] does not exist,creating")
                os.makedirs(trgDir)
            try:
                shutil.move(srcFile, trgDir)
            except Exception as why:
                dbg(debug,"******E R R O R****** while moving "+srcFile+" to "+trgDir,why)
                raise Exception

printFiles()
