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

    def Simulate(self):
        buyAmount = 15
        sellAmount = 20

        for i in range(len(self.DataPoints)):
            startOfInterval = self.DataPoints[i]
            endOfInterval = self.DataPoints[i + self.HoldInterval]
