import unittest
import beaconListener
import json
from math import *

class Test(unittest.TestCase):

     def test_degree(self):
         x = '{ "location" : { "x": 10, "z": 10 }}'
         beacon = json.loads(x)
         result = beaconListener.getDegree(beacon, 0, 0)
         compare = degrees(atan2(10, -10))
         self.assertEqual(result, compare)
     
     def test_distance(self):
         x = '{ "location" : { "x": 10, "z": 10 }}'
         beacon = json.loads(x)
         result = beaconListener.getDistance(beacon, 0, 0)
         
         dx = beacon['location']['x'] - 0
         dz = beacon['location']['z'] - 0
         compare = sqrt(dz**2 + dx**2)
         
         self.assertEqual(result, compare)
         
     if __name__ == '__main__':
         unittest.main()
