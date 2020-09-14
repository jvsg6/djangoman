from __future__ import absolute_import, unicode_literals
from celery import Celery
from .myPaths import reqPaths
import subprocess
from .prepCalc import changeAndCopyInFile, startAdm
from .models import Calc
from django.shortcuts import render, get_object_or_404
import os
import shutil
app = Celery('tasks', broker='redis://localhost:6379/')

@app.task
def allAdmActions(pk):
    post = get_object_or_404(Calc, pk=pk)


    pathToCalc = os.path.dirname(__file__) + "/static/calculations/" + str(post.pk)
    pathToGeotiff = os.path.dirname(__file__) + "/static/calculations/" + str(post.pk) + "/geotiff/"
    print ("pathToCalc", pathToCalc)
    print("pathToGeotiff", pathToGeotiff)
    os.makedirs(pathToCalc)
    os.makedirs(pathToGeotiff)


    shutil.copyfile(reqPaths.pathToLanduse, pathToCalc + "/landuse.asc")
    changeAndCopyInFile(reqPaths.pathToTemplate, pathToCalc, post)
    post.transportStatus = 1
    post.save()
    startAdm(pathToCalc)
    for funcNum in [0, 1, 2]:
        os.system(f'gdal_translate -a_srs EPSG:4326 NETCDF:{pathToCalc}/out.nc:gridFunction_{funcNum}  -of Gtiff {pathToGeotiff}/out_gridFunction_{funcNum}.geotiff')
    post.pathToInput = pathToCalc + "/in.xml"
    post.pathToLanduse = pathToCalc + "/landuse.asc"
    post.transportStatus = 2
    post.save()
    return 0