# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4, 5, 3 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')

    def testIsocelesTrianglesA(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isoceles', '3, 3, 4 should be isoceles')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classifyTriangle(3, 4, 4), 'Isoceles', '3, 4, 4 should be isoceles')

    def testIsocelesTrianglesC(self):
        self.assertEqual(classifyTriangle(3, 4, 3), 'Isoceles', '3, 4, 3 should be isoceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene', '5, 6, 7 should be Scalene')

    def testMax_sideA(self):
        self.assertEqual(classifyTriangle(201, 1, 1), 'InvalidInput', '201 is invalid input')

    def testMax_sideB(self):
        self.assertEqual(classifyTriangle(1, 201, 1), 'InvalidInput', '201 is invalid input')

    def testMax_sideC(self):
        self.assertEqual(classifyTriangle(1, 1, 201), 'InvalidInput', '201 is invalid input')

    def testMin_sideA(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', 'Each side should greater than 0')

    def testMin_sideB(self):
        self.assertEqual(classifyTriangle(1, 0, 1), 'InvalidInput', 'Each side should greater than 0')

    def testMin_sideC(self):
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', 'Each side should greater than 0')

    def testIsTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle',
                         'The sum of any two sides should greater than the third side')

    def testIsTriangleB(self):
        self.assertEqual(classifyTriangle(2, 3, 1), 'NotATriangle',
                         'The sum of any two sides should greater than the third side')

    def testIsTriangleC(self):
        self.assertEqual(classifyTriangle(3, 1, 2), 'NotATriangle',
                         'The sum of any two sides should greater than the third side')

    def testIsInstanceA(self):
        self.assertEqual(classifyTriangle(2.5, 3, 3), 'InvalidInput', 'Each side should be instance')

    def testIsInstanceB(self):
        self.assertEqual(classifyTriangle(3, 2.5, 3), 'InvalidInput', 'Each side should be instance')

    def testIsInstanceC(self):
        self.assertEqual(classifyTriangle(3, 3, 2.5), 'InvalidInput', 'Each side should be instance')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

