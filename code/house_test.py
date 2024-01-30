#!/usr/bin/env python3

from PIL import Image
import matplotlib.testing.compare as mpcompare
import unittest
import shapes
import tempfile
import os.path
import svg_turtle
import inspect
from main_script import *

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

CANVAS_SIZE = (997,997)

class TestShapes(unittest.TestCase):
    def _compare_canvas_to_expected(self, expected_filename, override_tmpdir=None):
        ''' compares the current canvas to an expected file.
        Returns None if and only if the files are identical.
        
        If override_tmpdir is set, use that directory for temporary files 
        (useful for generating known good testdata images.
        '''

        TOLERANCE = 1.0 # somewhere between 0 and 255, higher is more lax.

        with tempfile.TemporaryDirectory() as tmp_dirname:
            calling_function = inspect.stack()[1][3]
            tmp_dirname = tmp_dirname if not override_tmpdir else override_tmpdir

            actual_svg = os.path.join(tmp_dirname, '%s.svg' % calling_function)
            actual_png = os.path.join(tmp_dirname, '%s.png' % calling_function)
            self._turtle.save_as(actual_svg)
            
            # canvas generates a svg file, but we have to convert it to a png in
            # order to compare it using matplotlib's library
            drawing = svg2rlg(actual_svg)
            renderPM.drawToFile(drawing, actual_png, fmt="PNG")
            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)


    def setUp(self):
        # this is run before every test
        self._turtle = svg_turtle.SvgTurtle(*CANVAS_SIZE)

    def test_full_house(self):
        main()
        # compare this 20,20,20 turtle against the well-known turtle png
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='code/testdata/full_house.png'))
    def test_clouds(self):
        cloud_start_x1 = -300
        cloud_start_y1 = 300
        cloud_size_1 = 40
        cloud_start_x2 = 250
        cloud_start_y2 = 250
        cloud_size_2 = 30
        draw_cloud(cloud_start_x1, cloud_start_y1, cloud_size_1)
        draw_cloud(cloud_start_x2, cloud_start_y2, cloud_size_2)
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='code/testdata/clouds.png'))
    def test_door(self):
           # Draw door
        door_width = 40
        door_height = 80
        door_color = "brown"
        door_start_x = -door_width/2
        door_start_y = -70
        draw_door(door_start_x, door_start_y, door_width, door_height, door_color)
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='code/testdata/doors.png'))
    def test_trees(self):
        draw_tree(-400, -200, 100, 40, 120)
        draw_tree(300, -200, 100, 40, 120)
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='code/testdata/trees.png'))
    def test_windows(self):
       # Draw windows
        window_start_x1 = -190
        window_start_x2 = -105
        window_start_x3 = 55
        window_start_x4 = 140
        window_start_y = 10
        window_width = 50
        window_height = 50
        draw_window(window_start_x1, window_start_y, window_width, window_height)
        draw_window(window_start_x2, window_start_y, window_width, window_height)
        draw_window(window_start_x3, window_start_y, window_width, window_height)
        draw_window(window_start_x4, window_start_y, window_width, window_height)
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='code/testdata/windows.png'))
    def test_gdoors(self):
         # Draw garage doors
        gdoor_start_x1 = -190
        gdoor_start_x2 = 140
        gdoor_start_y = -50
        gdoor_width = 50
        gdoor_height = 100
        gdoor_color = "grey"   
        draw_door(gdoor_start_x1, gdoor_start_y, gdoor_width, gdoor_height, gdoor_color)
        draw_door(gdoor_start_x2, gdoor_start_y, gdoor_width, gdoor_height, gdoor_color)
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='code/testdata/gdoors.png'))

if __name__ == '__main__':
    unittest.main()