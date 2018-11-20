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
    [320,  250],
    [320,  260],
    [320,  270],
    [320,  280],
])


class test_transform(unittest.TestCase):

    """
    This class tests for rotation and tranformation of points
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
            [70, 280],
            [60, 280],
            [50, 280],
            [40, 280],
        ])
        for point in rotatedPoints:
            expected_canvas.text((point[0], point[1]), 'X')
        expected_image.save(expectedDirectory + "/" + fileName, fileType)
        expected_image.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())

    def test_transform(self):
        fileName = 'test_transform.png'

        # Result image for transform
        result_image = Image.new(imageMode, imageSize, imageBackground)
        result_canvas = ImageDraw.Draw(result_image)

        draw(result_canvas, points, "+")

        draw(result_canvas, transform(points, 160, 0), "0")
        draw(result_canvas, transform(points, 160, 30), "30")
        draw(result_canvas, transform(points, 160, 60), "60")
        draw(result_canvas, transform(points, 160, 90), "90")

        result_image.save(resultDirectory + "/" + fileName, fileType)
        result_image.close()

        # Expected image for transform
        expected_image = Image.new(imageMode, imageSize, imageBackground)
        expected_canvas = ImageDraw.Draw(expected_image)

        draw(expected_canvas, points, "+")

        draw(expected_canvas, ((480, 250), (480, 260), (480, 270), (480, 280)), "0")
        draw(expected_canvas, ((458.56406461, 330), (458.56406461, 340), (458.56406461, 350), (458.56406461, 360)), "30")
        draw(expected_canvas, ((400, 388.56406461), (400, 398.56406461), (400, 408.56406461), (400, 418.56406461)),"60")
        draw(expected_canvas, ((320, 410), (320, 420), (320, 430), (320, 440)), "90")

        expected_image.save(expectedDirectory + "/" + fileName, fileType)
        expected_image.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName
        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())

    def test_scale(self):
            fileName = 'test_scale.png'

            # Result image for scaling
            result_image = Image.new(imageMode, imageSize, imageBackground)
            result_canvas = ImageDraw.Draw(result_image)

            drawSolid(result_canvas, regularPolygon(3, np.array([240, 220]), 100), 'white')
            drawSolid(result_canvas, regularPolygon(4, np.array([420, 320]), 120), 'white')

            drawSolid(result_canvas, scale(np.array([240, 220]), (regularPolygon(3, np.array([240, 220]), 100)),
                                           0.4),'black')
            drawSolid(result_canvas, scale(np.array([420, 320]), (regularPolygon(4, np.array([420, 320]), 120)),
                                           0.5),'black')

            result_image.save(resultDirectory + "/" + fileName, fileType)
            result_image.close()

            # Expected image for scaling
            expected_image = Image.new(imageMode, imageSize, imageBackground)
            expected_canvas = ImageDraw.Draw(expected_image)

            print (regularPolygon(3, np.array([240, 220]), 100))
            print(regularPolygon(4, np.array([420, 320]), 120))

            drawSolid(expected_canvas, ((290., 220.), (215., 263.30127019), (215., 176.69872981)), 'white')
            drawSolid(expected_canvas, ((480., 320.), (420., 380.), (360., 320.), (420., 260.)), 'white')

            drawSolid(expected_canvas, scale((240, 220), ((290., 220.), (215., 263.30127019), (215., 176.69872981)),
                                           0.4), 'black')
            drawSolid(expected_canvas, scale((420, 320), ((480., 320.), (420., 380.), (360., 320.), (420., 260.)),
                                           0.5), 'black')

            expected_image.save(expectedDirectory + "/" + fileName, fileType)
            expected_image.close()

            result = resultDirectory + "/" + fileName
            expected = expectedDirectory + "/" + fileName

            self.assertTrue(open(result, "rb").read() != open(expected, "rb").read())


if __name__ == '__main__':
    unittest.main()
