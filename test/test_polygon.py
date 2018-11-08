#!/usr/bin/env python
"""
  This module tests the function of Polygon vertices Generation.
  TODO test_concavePolygon and test_convexPolygon
"""

import unittest
import os

from blocksWorld import *

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileDir = os.path.dirname(os.path.realpath('__file__'))
resultDirectory = os.path.join(fileDir, '../data_result/polygon')
expectedDirectory = os.path.join(fileDir, '../data_expected/polygon')

if not os.path.exists(resultDirectory):
    os.makedirs(resultDirectory)

if not os.path.exists(expectedDirectory):
    os.makedirs(expectedDirectory)

points = np.array([
    [5,  5],
    [5, 15],
    [5, 25],
    [5, 35],
    [5, 45],
    [5, 55],
    [5, 65],
    [5, 75]
])


class test_polygon(unittest.TestCase):

    """
        Plotting Images for different types of polygons.
    """

    # Reference images for regularPolygon.
    def test_regularPolygon(self):
        # Reference image for regularPolygon
        fileName = 'test_regularPolygon.png'

        result_regularImage = Image.new(imageMode, imageSize, imageBackground)
        result_regularCanvas = ImageDraw.Draw(result_regularImage)

        # Result image for regularPolygon
        draw(result_regularCanvas, regularPolygon(3, np.array([160, 120]), 50), '3')
        draw(result_regularCanvas, regularPolygon(4, np.array([480, 120]), 90), '4')
        draw(result_regularCanvas, regularPolygon(5, np.array([420, 360]), 60), '5')

        result_regularImage.save(resultDirectory + "/" + fileName, fileType)
        result_regularImage.close()

        # Expected image for regularPolygon
        expected_regularImage = Image.new(imageMode, imageSize, imageBackground)
        expected_regularCanvas = ImageDraw.Draw(expected_regularImage)
        # Triangle
        expected_regularCanvas.text((185, 120), '3')
        expected_regularCanvas.text((147.5, 141.65063509), '3')
        expected_regularCanvas.text((147.5, 98.34936491), '3')
        # Square
        expected_regularCanvas.text((525, 120), '4')
        expected_regularCanvas.text((480, 165), '4')
        expected_regularCanvas.text((435, 120), '4')
        expected_regularCanvas.text((480, 75), '4')
        # Pentagon
        expected_regularCanvas.text((450, 360), '5')
        expected_regularCanvas.text((429.27050983, 388.53169549), '5')
        expected_regularCanvas.text((395.72949017, 377.63355757), '5')
        expected_regularCanvas.text((395.72949017, 342.36644243), '5')
        expected_regularCanvas.text((429.27050983, 331.46830451), '5')

        expected_regularImage.save(expectedDirectory + "/" + fileName, fileType)
        expected_regularImage.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())

    # def test_convexPolygon(self):
    # TODO

    # def test_concavePolygon(self):
    # TODO

    # Reference images for randomPolygon.
    def test_randomPolygon(self):
        # Reference image for randomPolygon
        fileName = 'test_randomPolygon.png'

        result_randomImage = Image.new(imageMode, imageSize, imageBackground)
        result_randomCanvas = ImageDraw.Draw(result_randomImage)

        seed = 5
        # Result image for regularPolygon
        draw(result_randomCanvas, randomPolygon(seed, 3, np.array([160, 120]), 200), '3r')
        draw(result_randomCanvas, randomPolygon(seed, 4, np.array([480, 120]), 200), '4r')
        draw(result_randomCanvas, randomPolygon(seed, 5, np.array([480, 360]), 200), '5r')

        result_randomImage.save(resultDirectory + "/" + fileName, fileType)
        result_randomImage.close()

        # Expected image for regularPolygon
        expected_randomImage = Image.new(imageMode, imageSize, imageBackground)
        expected_randomCanvas = ImageDraw.Draw(expected_randomImage)
        # Triangle
        expected_randomCanvas.text((184.58033898, 168.35739785), '3r')
        expected_randomCanvas.text((219.03871311, 208.49005676), '3r')
        expected_randomCanvas.text((207.97971495, 204.46499933), '3r')
        # Square
        expected_randomCanvas.text((504.58033898, 168.35739785), '4r')
        expected_randomCanvas.text((539.03871311, 208.49005676), '4r')
        expected_randomCanvas.text((527.97971495, 204.46499933), '4r')
        expected_randomCanvas.text((385.80104566, 113.12453088), '4r')
        # Pentagon
        expected_randomCanvas.text((504.58033898, 408.35739785), '5r')
        expected_randomCanvas.text((539.03871311, 448.49005676), '5r')
        expected_randomCanvas.text((527.97971495, 444.46499933), '5r')
        expected_randomCanvas.text((385.80104566, 353.12453088), '5r')
        expected_randomCanvas.text((568.6713434, 389.79491063), '5r')

        expected_randomImage.save(expectedDirectory + "/" + fileName, fileType)
        expected_randomImage.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())


if __name__ == '__main__':
    unittest.main()
