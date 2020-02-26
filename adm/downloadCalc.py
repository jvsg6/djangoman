from .models import Calc
from django.http import HttpResponse, Http404
import sys
import os
def download(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def downloadFiles(listOfFilesToDownload, calc):
    for reqFileType in listOfFilesToDownload:
        if reqFileType == "LanduseFile":
            print("LanduseFile", calc.pk)
            return download(calc.pathToLanduse)
        if reqFileType == "InputFile":
            print('InputFile', calc.pk)
            return download(calc.pathToInput)
        if reqFileType == "OutputFile":
            print('OutputFile', calc.pk)
    return
