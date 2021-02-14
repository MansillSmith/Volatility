from datetime import datetime

class VolatilityDataPoint:
    def __init__(self, timeStamp: datetime, open: float, high: float, low: float
    , close: float, adjClose: float):
        super().__init__()
        self.TimeStamp = timeStamp
        self.Open = open
        self.High = high
        self.Low = low
        self.Close = close
        self.AdjClose = adjClose

    def AverageHighLow(self):
        return (self.High + self.Low) / 2

    @staticmethod
    def ParseCSV(line: str):
        try:
            split = line.split(",")
            time = datetime.strptime(split[0], '%Y-%m-%d')
            open = float(split[1])
            high = float(split[2])
            low = float(split[3])
            close = float(split[4])
            adjClose = float(split[5])
            return VolatilityDataPoint(time, open, high, low, close, adjClose)
        except:
            return None

    def __eq__(self, value):
        if type(value) == VolatilityDataPoint:
            b = self.TimeStamp == value.TimeStamp and self.Open == value.Open
            b = b and self.High == value.High and self.Low == value.Low
            b = b and self.Close == value.Close and self.AdjClose == value.AdjClose
            return b
        else:
            return False