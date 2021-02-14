from VolatilityDataPoint import VolatilityDataPoint
from datetime import datetime
import unittest

class TestMethods(unittest.TestCase):

    # Tests that the constructor works
    def testConstructorBasic(self):
        vdp = VolatilityDataPoint(datetime(2016,2,17), 23.400000, 24.160000, 21.830000, 22.309999, 22.309999)
        self.assertEqual(datetime(2016,2,17), vdp.TimeStamp)
        self.assertEqual(23.400000, vdp.Open)
        self.assertEqual(24.160000, vdp.High)
        self.assertEqual(21.830000, vdp.Low)
        self.assertEqual(22.309999, vdp.Close)
        self.assertEqual(22.309999, vdp.AdjClose)

    # Tests that the CSV parser works
    def testParseBasic(self):
        inputString = "2016-02-16,24.959999,25.520000,23.320000,24.110001,24.110001,0"
        vdp1 = VolatilityDataPoint.ParseCSV(inputString)
        vdp2 = VolatilityDataPoint(datetime(2016, 2, 16), 24.959999, 25.520000, 23.320000, 24.110001, 24.110001)
        self.assertEqual(vdp1, vdp2)
    
    # Tests that the parser fails on negative input
    def testParseNegative(self):
        inputString = "abcd"
        vdp = VolatilityDataPoint.ParseCSV(inputString)
        self.assertEqual(vdp, None)

if __name__ == "__main__":
    unittest.main()