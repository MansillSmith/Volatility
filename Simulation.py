from VolatilityDataPoint import VolatilityDataPoint

class Simulation:
    def __init__(self):
        super().__init__()

    def ParseCSV(self, pathToFile: str):
        lines = ''
        with open(pathToFile, "r") as openedFile:
            lines = openedFile.readlines()
        
        temp = []
        for l in lines:
            temp.append(VolatilityDataPoint.ParseCSV(l))
        
        self.DataPoints = temp