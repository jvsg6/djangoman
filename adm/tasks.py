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
    pathToCalc = os.path.dirname(__file__) + "/calculations/" + str(post.pk)
    print (pathToCalc)
    os.makedirs(pathToCalc)
    shutil.copyfile(reqPaths.pathToLanduse, pathToCalc + "/landuse.asc")
    changeAndCopyInFile(reqPaths.pathToTemplate, pathToCalc, post)
    post.transportStatus = 1
    post.save()
    startAdm(pathToCalc)
    post.pathToInput = pathToCalc + "/in.xml"
    post.pathToLanduse = pathToCalc + "/landuse.asc"
    post.transportStatus = 2
    post.save()
    return 0