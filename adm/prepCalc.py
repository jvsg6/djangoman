#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import os
import shutil
from .myPaths import reqPaths
from django.template import Context, Template
import subprocess

def startAdm(pathToCalc):
    try:
        p = subprocess.Popen([reqPaths.pathToADM,  '--got=netcdf4','--db', pathToCalc], stdout=subprocess.PIPE)
        return p.poll()
    except OSError:
        print ("Error: Write valid path to ADM!")
        return -1
    return


def insertSrcInContext(srcParameters, contextParameters):
    contextParameters['srcLat'] = str(srcParameters.lat).replace(",", ".")
    contextParameters['srcLon'] = str(srcParameters.lon).replace(",", ".")


def insertCalcAreaInContext(areaCalcParam, contextParameters):
    contextParameters['lonMinCalc'] = str(areaCalcParam.lonMin).replace(",", ".")
    contextParameters['lonMaxCalc'] = str(areaCalcParam.lonMax).replace(",", ".")
    contextParameters['latMinCalc'] = str(areaCalcParam.latMin).replace(",", ".")
    contextParameters['latMaxCalc'] = str(areaCalcParam.latMax).replace(",", ".")

def insertResAreaInContext(areaResParam, contextParameters):
    contextParameters['lonMinRes'] = str(areaResParam.lonMin).replace(",", ".")
    contextParameters['lonMaxRes'] = str(areaResParam.lonMax).replace(",", ".")
    contextParameters['latMinRes'] = str(areaResParam.latMin).replace(",", ".")
    contextParameters['latMaxRes'] = str(areaResParam.latMax).replace(",", ".")
    contextParameters['countLon'] = str(areaResParam.countLon).replace(",", ".")
    contextParameters['countLat'] = str(areaResParam.countLat).replace(",", ".")

def insertDataInContext(post, contextParameters):
    insertSrcInContext(post.srcParameters, contextParameters)
    insertCalcAreaInContext(post.areaCalcParameters, contextParameters)
    insertResAreaInContext(post.areaResParameters, contextParameters)
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
    pathToCalc = os.path.dirname(__file__) + "/calculations/" +post.author.get_username().replace(" ", "-") + "/" + str(post.pk)
    print (pathToCalc)
    os.makedirs(pathToCalc)
    shutil.copyfile(reqPaths.pathToLanduse, pathToCalc + "/landuse.asc")
    changeAndCopyInFile(reqPaths.pathToTemplate, pathToCalc, post)
    startAdm(pathToCalc)
    return
