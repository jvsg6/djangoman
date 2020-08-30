#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import os
import shutil
from .myPaths import reqPaths
from django.template import Context, Template
import subprocess
import time
from .myPaths import startADM

def insertSrcInContext(srcParameters, contextParameters):
    contextParameters['srcLat'] = str(srcParameters.lat).replace(",", ".")
    contextParameters['srcLon'] = str(srcParameters.lon).replace(",", ".")


def insertCalcAreaInContext(areaCalcParam, contextParameters):
    contextParameters['lonMinCalc'] = str(areaCalcParam.lonMinCalc).replace(",", ".")
    contextParameters['lonMaxCalc'] = str(areaCalcParam.lonMaxCalc).replace(",", ".")
    contextParameters['latMinCalc'] = str(areaCalcParam.latMinCalc).replace(",", ".")
    contextParameters['latMaxCalc'] = str(areaCalcParam.latMaxCalc).replace(",", ".")

def insertResAreaInContext(areaResParam, contextParameters):
    contextParameters['lonMinRes'] = str(areaResParam.lonMinRes).replace(",", ".")
    contextParameters['lonMaxRes'] = str(areaResParam.lonMaxRes).replace(",", ".")
    contextParameters['latMinRes'] = str(areaResParam.latMinRes).replace(",", ".")
    contextParameters['latMaxRes'] = str(areaResParam.latMaxRes).replace(",", ".")
    contextParameters['countLon'] = str(areaResParam.countLonRes).replace(",", ".")
    contextParameters['countLat'] = str(areaResParam.countLatRes).replace(",", ".")

def insertDataInContext(post, contextParameters):
    insertSrcInContext(post.srcParam, contextParameters)
    insertCalcAreaInContext(post.areaCalcParam, contextParameters)
    insertResAreaInContext(post.areaResParam, contextParameters)
    return

def changeAndCopyInFile(pathToTemplate, pathToCalc, post):
    inFile = open(pathToTemplate, "r")
    inTemplate = Template(inFile.read())
    inFile.close()
    contextParameters = {}
    insertDataInContext(post, contextParameters)
    reqIn = inTemplate.render(Context(contextParameters))
    f = open(pathToCalc + "/in.xml", "w")
    f.write(reqIn)
    f.close()
    return


def startAdm(pathToCalc):
    if startADM:
        try:
            process = subprocess.Popen([reqPaths.pathToADM,  '--got=netcdf4','--db', pathToCalc], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = process.communicate()[0] 
            ret = process.wait()
            print("Start ADM")
            print(" ".join([reqPaths.pathToADM,  '--got=netcdf4','--db', pathToCalc]))
            return ret
        except OSError:
            print ("Error: Write valid path to ADM!")
            return -1
        return -1
    else:
        print("Start ADM")
        print(" ".join([reqPaths.pathToADM,  '--got=netcdf4','--db', pathToCalc]))
        time.sleep(15)
        return 0