from django import template
import os

register = template.Library()

@register.simple_tag
def hello_world(calcNum, funcNum):
    print("calcNum, funcNum", calcNum, funcNum)
    pathToOutFolder = f"/home/ilichev/tasks/training/django/djangoman/adm/calculations/{calcNum}/"
    os.system(f'gdal_translate -a_srs EPSG:4326 NETCDF:{pathToOutFolder}/out.nc:gridFunction_{funcNum}  -of Gtiff {pathToOutFolder}/out_gridFunction_{funcNum}.geotiff')
    return f"salute {calcNum} {funcNum}"