#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import os

try:
    mypath = os.path.dirname(os.path.abspath(__file__))
except NameError:
    mypath = os.path.dirname(os.path.abspath(sys.argv[0]))

startADM = None

class ReqPaths():
    if "ilichev" in mypath:
        pathToADM = '/home/ilichev/Programs/release/nostra_build/nostraconsole'
        pathToWorkingFolder = os.path.dirname(__file__)
        pathToLanduse ='/home/ilichev/Downloads/landuse.asc'
        pathToTemplate = '/home/ilichev/Downloads/in_template.xml'
        startADM = True
    elif "grozata" in mypath:
        pathToADM = '/home/ilichev/Programs/release/nostra_build/nostraconsole'
        pathToWorkingFolder = os.path.dirname(__file__)
        pathToLanduse ='/home/ilichev/Downloads/landuse.asc'
        pathToTemplate = '/home/ilichev/Downloads/in_template.xml'
        startADM = False

reqPaths = ReqPaths()
