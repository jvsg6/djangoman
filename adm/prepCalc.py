#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import os
import shutil
from .myPaths import reqPaths
from django.template import Context, Template
import subprocess
from .tasks import startAdm

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

def allAdmActions(post):
    pathToCalc = os.path.dirname(__file__) + "/calculations/" + str(post.pk)
    print (pathToCalc)
    os.makedirs(pathToCalc)
    shutil.copyfile(reqPaths.pathToLanduse, pathToCalc + "/landuse.asc")
    changeAndCopyInFile(reqPaths.pathToTemplate, pathToCalc, post)
    
    startAdm.delay(pathToCalc)
    post.pathToInput = pathToCalc + "/in.xml"
    post.pathToLanduse = pathToCalc + "/landuse.asc"
    return
