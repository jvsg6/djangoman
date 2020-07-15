from __future__ import absolute_import, unicode_literals
from celery import Celery
from .myPaths import reqPaths
import subprocess


app = Celery('tasks', broker='redis://localhost:6379/')

@app.task
def startAdm(pathToCalc):
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