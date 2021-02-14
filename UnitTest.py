from VolatilityDataPoint import VolatilityDataPoint
from datetime import datetime
import unittest

class TestMethods(unittest.TestCase):
    def testBasic(self):
        inputString = "2016-02-16,24.959999,25.520000,23.320000,24.110001,24.110001,0"
        vdp1 = VolatilityDataPoint.ParseCSV(inputString)
        vdp2 = VolatilityDataPoint(datetime(2016, 2, 16), 24.959999, 25.520000, 23.320000, 24.110001, 24.110001)
        self.assertEqual(vdp1, vdp2)

if __name__ == "__main__":
    unittest.main()