import numpy as np
import json
import sys, os
from copy import deepcopy

class GridData2D(object):
    def __init__(self):
            self.lonMin = 0.
            self.lonMax = 0.
            self.latMin = 0.
            self.latMax = 0.
            self.countLon = 0.
            self.countLat = 0.
            self.gridVals = []
            self.lon_set = []
            self.lat_set = []

    def getDataInList(self):
        gridDataInList = [[0, 0, 0] for i in range(self.countLat * self.countLon)]

        for j in range(self.countLat):
                for i in range(self.countLon):
                    gridDataInList[j + (i * self.countLon)][0] = self.lat_set[i]
                    gridDataInList[j + (i * self.countLon)][1] = self.lon_set[j]
                    gridDataInList[j + (i * self.countLon)][2] = self.gridVals[i*self.countLat+(self.countLat-j-1)]

        return gridDataInList

    def __str__(self):
        a = {
            "lonMin" : self.lonMin,
            "lonMax" : self.lonMax,
            "latMin" : self.latMin,
            "latMax" : self.latMax,
            "countLon" : self.countLon,
            "countLat" : self.countLat, 
            }
        return json.dumps(a)

class Netcdf4GridReader(GridData2D):
    def __init__(self, pathToNc):
            from netCDF4 import Dataset
            super(Netcdf4GridReader,self).__init__()
            self.dataset = Dataset(pathToNc)

    def initGridByNameAndId(self, gridName):

            gridFunction = self.dataset.variables[gridName]

            lonGridData = self.dataset.variables['lon']
            latGridData = self.dataset.variables['lat']

            self.lon_set = deepcopy(lonGridData[:])
            self.lat_set = deepcopy(latGridData[:])

            self.lonMin = self.lon_set[0]
            self.latMin = self.lat_set[0]

            self.lonMax = self.lon_set[-1]
            self.latMax = self.lat_set[-1]

            self.countLon = len(self.lon_set)
            self.countLat = len(self.lat_set)

            self.dlon = self.lon_set[1] - self.lon_set[0]
            self.dlat = self.lat_set[1] - self.lat_set[0]
            
            self.gridVals = np.zeros(self.countLon*self.countLat, np.float32)

            for j in range(self.countLat): 
                    lin = gridFunction[self.countLat-j-1]
                    for i in range(self.countLon):
                            self.gridVals[i*self.countLat+(self.countLat-j-1)] = lin[i]
            return



def main():
    pathToWorkFolder = '/home/ilichev/tasks/training/django/djangoman/adm/calculations/2/'

    pathToNc = os.path.join(pathToWorkFolder, 'out.nc')

    grid = Netcdf4GridReader(pathToNc)
    gridId = 0
    grid.initGridByNameAndId('gridFunction_{0}'.format(gridId))  
    pathToOut = os.path.join(pathToWorkFolder, f'valsOnGrid_{gridId}.js')
    with open(pathToOut, 'w') as filehandle:  
        filehandle.write('var valsOnGrid = ' + str(grid.getDataInList()))


if __name__ == "__main__":
    sys.exit(main())