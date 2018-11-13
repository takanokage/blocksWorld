#!/usr/bin/env python
"""
         This module Test for Valid Image with the given boundaries
         TODO drawPattern
"""

import unittest
import os

from blocksWorld import *

imageSize = (640, 480)
x, y = imageSize
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileDir = os.path.dirname(os.path.realpath('__file__'))
resultDirectory = os.path.join(fileDir, '../data_result/draw')
expectedDirectory = os.path.join(fileDir, '../data_expected/draw')

if not os.path.exists(resultDirectory):
    os.makedirs(resultDirectory)

if not os.path.exists(expectedDirectory):
    os.makedirs(expectedDirectory)

points = [
            np.array([5,  5]),
            np.array([5, 15]),
            np.array([5, 25]),
            np.array([5, 35]),
            np.array([5, 45]),
            np.array([5, 55]),
            np.array([5, 65]),
            np.array([5, 75])
        ]


class TestDraw(unittest.TestCase):
    
    """
     Plotting images for draw and drawWire

    """
    # Reference image for draw
    def test_draw(self):
        fileName = 'test_draw.png'

        # Result image for draw
        result_image = Image.new(imageMode, imageSize, imageBackground)
        result_canvas = ImageDraw.Draw(result_image)
        draw(result_canvas, (np.array(points)), 'A')
        result_image.save(resultDirectory + "/" + fileName, fileType)
        result_image.close()

        # Expected image for draw
        expected_image = Image.new(imageMode, imageSize, imageBackground)
        expected_canvas = ImageDraw.Draw(expected_image)
        for point in points:
            print (point[0], point[1])
            expected_canvas.text((point[0], point[1]), 'A', fill='black')
        expected_image.save(expectedDirectory + "/" + fileName, fileType)
        expected_image.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())

    # Reference image for drawWire
    def test_drawWire(self):
        fileName = 'test_drawWire.png'

        # Result image for drawWire
        result_wireImage = Image.new(imageMode, imageSize, imageBackground)
        result_wireCanvas = ImageDraw.Draw(result_wireImage)
        drawWire(result_wireCanvas, points)
        result_wireImage.save(resultDirectory + "/" + fileName, fileType)
        result_wireImage.close()

        # Expected image for drawWire
        expected_wireImage = Image.new(imageMode, imageSize, imageBackground)
        expected_wireCanvas = ImageDraw.Draw(expected_wireImage)
        size = len(points)
        for i in range(size):
            p0 = points[i]
            p1 = points[(i + 1) % size]
            expected_wireCanvas.line([(p0[0], p0[1]), (p1[0], p1[1])])
        expected_wireImage.save(expectedDirectory + "/" + fileName, fileType)
        expected_wireImage.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())

    # Reference image for drawSolid
    def test_drawSolid(self):
        fileName = 'test_drawSolid.png'

        # Result image for drawSolid
        result_solidImage = Image.new('RGB', imageSize, imageBackground)
        result_solidCanvas = ImageDraw.Draw(result_solidImage)

        drawSolid(result_solidCanvas, ((185, 120), (147.5, 141.65063509), (147.5, 98.34936491)), 'red')
        drawSolid(result_solidCanvas, ((525., 120.), (480., 165.), (435., 120.), (480.,  75.)), 'blue')
        drawSolid(result_solidCanvas, ((450., 360.), (429.27050983, 388.53169549), (395.72949017, 377.63355757),
                                       (395.72949017, 342.36644243), (429.27050983, 331.46830451)), 'green')
        drawSolid(result_solidCanvas, ((200., 360.), (180., 394.64101615), (140., 394.64101615), (120., 360.),
                                       (140., 325.35898385), (180., 325.35898385)), 'black')
        drawSolid(result_solidCanvas, ((355., 160.), (341.82214307, 187.36410189), (312.21176731, 194.12247693),
                                       (288.46608962, 175.18593087), (288.46608962, 144.81406913),
                                       (312.21176731, 125.87752307), (341.82214307, 132.63589811)), 'brown')
        result_solidImage.save(resultDirectory + "/" + fileName, fileType)
        result_solidImage.close()

        # Expected image for drawSolid
        expected_solidImage = Image.new('RGB', imageSize, imageBackground)
        expected_solidCanvas = ImageDraw.Draw(expected_solidImage)

        expected_solidCanvas.polygon(((185, 120), (147.5, 141.65063509), (147.5, 98.34936491)), 'red', outline='black')
        expected_solidCanvas.polygon(((525., 120.), (480., 165.), (435., 120.), (480., 75.)), 'blue', outline='black')
        expected_solidCanvas.polygon(((450., 360.), (429.27050983, 388.53169549), (395.72949017, 377.63355757),
                                      (395.72949017, 342.36644243), (429.27050983, 331.46830451)), 'green',
                                     outline='black')
        expected_solidCanvas.polygon(((200., 360.), (180., 394.64101615), (140., 394.64101615), (120., 360.),
                                      (140., 325.35898385), (180., 325.35898385)), 'black', outline='black')
        expected_solidCanvas.polygon(((355., 160.), (341.82214307, 187.36410189), (312.21176731, 194.12247693),
                                      (288.46608962, 175.18593087), (288.46608962, 144.81406913),
                                      (312.21176731, 125.87752307), (341.82214307, 132.63589811)), 'brown',
                                     outline='black')
        expected_solidImage.save(expectedDirectory + "/" + fileName, fileType)
        expected_solidImage.close()

        result = resultDirectory + "/" + fileName
        expected = expectedDirectory + "/" + fileName

        self.assertTrue(open(result, "rb").read() == open(expected, "rb").read())


if __name__ == '__main__':
    unittest.main()
