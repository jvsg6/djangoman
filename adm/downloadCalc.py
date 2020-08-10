from .models import Calc
from django.http import HttpResponse, Http404
import sys
import os
def download(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            print(response)
            return response
    raise Http404

def downloadFiles(fileType, calc):
    if fileType == "LanduseFile":
        print("LanduseFile", calc.pk, calc.pathToLanduse)
        return download(calc.pathToLanduse)
    if fileType == "InputFile":
        print('InputFile', calc.pk, calc.pathToInput)
        return download(calc.pathToInput)
    if fileType == "OutputFile":
        print('OutputFile', calc.pk)
    return
