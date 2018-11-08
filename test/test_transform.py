#!/usr/bin/env python
"""
This module test the rotation of vertices for a given points.
"""
import unittest
import os

from blocksWorld import *

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileDir = os.path.dirname(os.path.realpath('__file__'))
resultDirectory = os.path.join(fileDir, '../data_result/transform')
expectedDirectory = os.path.join(fileDir, '../data_expected/transform')

if not os.path.exists(resultDirectory):
    os.makedirs(resultDirectory)

if not os.path.exists(expectedDirectory):
    os.makedirs(expectedDirectory)

points = np.array([
    [50,  5],
    [50, 15],
    [50, 25],
    [50, 35],
    [50, 45],
    [50, 55],
    [50, 65],
    [50, 75]
])


class test_transform(unittest.TestCase):

    """
    This class tests for rotation of vertices for 180 degrees
    """
    # Reference image for rotate.
    def test_rotate(self):
        fileName = 'test_rotate.png'

        # Result image for rotate
        result_image = Image.new(imageMode, imageSize, imageBackground)
        result_canvas = ImageDraw.Draw(result_image)
        draw(result_canvas, points, '+')
        center = np.array([180, 140])
        draw(result_canvas, [center], 'center')
        rotatedPoints = rotate(points, center, 90.0)
        draw(result_canvas, rotatedPoints, 'X')
        result_image.save(resultDirectory + "/" + fileName, fileType)
        result_image.close()

        # Expected image for rotate
        expected_image = Image.new(imageMode, imageSize, imageBackground)
        expected_canvas = ImageDraw.Draw(expected_image)
        for point in points:
            expected_canvas.text((point[0], point[1]), '+')
        expected_canvas.text((180, 140), 'center')
        rotatedPoints = np.array([
            [315., 10.],
            [305., 10.],
            [295., 10.],
            [285., 10.],
            [275., 10.],
            [265., 10.],
            [255., 10.],
            [245., 10.],
        ])
        for point in rotatedPoints:
            expected_canvas.text((point[0], point[1]), 'X')
        expected_image.save(expectedDirectory + "/" + fileName, fileType)
        expected_image.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())


if __name__ == '__main__':
    unittest.main()
