import unittest
import displayio
from adafruit_matrixportal.matrix import Matrix
from lib.draw_tools import (
    nba_team,
    draw_pixel,
    draw_row_singular,
    draw_rows,
    draw_column_singular,
    draw_columns,
    scale_pattern,
    draw_sprite,
    draw_cube,
    draw_triangle,
    draw_zero
)

# A mock pattern (as provided)
mock_pattern = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)

# Create a Matrix instance and a dummy display group (for functions using displayio)
matrix = Matrix(width=64, height=64, bit_depth=1)
display = matrix.display
color_convertor = displayio.ColorConverter(input_colorspace=displayio.Colorspace.RGB565)
group = displayio.Group()
mock_bitmap = displayio.Bitmap(display.width, display.height, 16)
mock_palette = displayio.Palette(2)
mock_palette[1] = 0x000000 
tilegrid_mock = displayio.TileGrid(mock_bitmap, pixel_shader=mock_palette)
group.append(tilegrid_mock)

# DummyBitmap for our unit tests (so we can check pixel values)
class DummyBitmap:
    def __init__(self, width, height, colors=16):
        self.width = width
        self.height = height
        self.colors = colors
        self.data = [[0 for _ in range(width)] for _ in range(height)]
    
    def __getitem__(self, pos):
        x, y = pos
        return self.data[y][x]
    
    def __setitem__(self, pos, value):
        x, y = pos
        self.data[y][x] = value

# -------------------------------
# Test Classes
# -------------------------------

class TestTeamCreation(unittest.TestCase):
    def test_team_creation(self):
        test_bitmap = DummyBitmap(10, 10)
        test_palette = "dummy_palette"
        test_pattern = mock_pattern
        test_team = nba_team(test_bitmap, test_palette, test_pattern)
        self.assertEqual(test_team.bitmap, test_bitmap)
        self.assertEqual(test_team.palette, test_palette)
        self.assertEqual(test_team.pattern, test_pattern)

class TestDrawPixel(unittest.TestCase):
    def setUp(self):
        self.bitmap = DummyBitmap(width=10, height=10)
    
    def test_draw_pixel(self):
        draw_pixel(self.bitmap, 3, 4, 5)
        self.assertEqual(self.bitmap[3, 4], 5)

class TestDrawRowSingular(unittest.TestCase):
    def setUp(self):
        self.bitmap = DummyBitmap(width=10, height=10)
    
    def test_draw_row_singular(self):
        draw_row_singular(self.bitmap, length=5, y=2, my_color=7)
        for x in range(5):
            self.assertEqual(self.bitmap[x, 2], 7)
        for x in range(5, self.bitmap.width):
            self.assertEqual(self.bitmap[x, 2], 0)

class TestDrawRows(unittest.TestCase):
    def setUp(self):
        self.bitmap = DummyBitmap(width=10, height=10)
    
    def test_draw_rows(self):
        draw_rows(self.bitmap, start_loc=1, num_rows=3, length=4, my_color=3)
        for y in range(1, 4):
            for x in range(4):
                self.assertEqual(self.bitmap[x, y], 3)
            for x in range(4, self.bitmap.width):
                self.assertEqual(self.bitmap[x, y], 0)

class TestDrawColumnSingular(unittest.TestCase):
    def setUp(self):
        self.bitmap = DummyBitmap(width=10, height=10)
    
    def test_draw_column_singular(self):
        draw_column_singular(self.bitmap, length=4, x=2, my_color=8)
        for y in range(4):
            self.assertEqual(self.bitmap[2, y], 8)
        for y in range(4, self.bitmap.height):
            self.assertEqual(self.bitmap[2, y], 0)

class TestDrawColumns(unittest.TestCase):
    def setUp(self):
        self.bitmap = DummyBitmap(width=10, height=10)
    
    def test_draw_columns(self):
        draw_columns(self.bitmap, start_loc=2, num_columns=3, length=5, my_color=9)
        for x in range(2, 5):
            for y in range(5):
                self.assertEqual(self.bitmap[x, y], 9)

class TestScalePattern(unittest.TestCase):
    def test_scale_pattern(self):
        pattern = [1, 0, 0, 1]  # 2x2 pattern
        new_pattern, new_width, new_height = scale_pattern(pattern, original_width=2, original_height=2, scale=2)
        expected = [
            1, 1, 0, 0,
            1, 1, 0, 0,
            0, 0, 1, 1,
            0, 0, 1, 1
        ]
        self.assertEqual(new_pattern, expected)
        self.assertEqual(new_width, 4)
        self.assertEqual(new_height, 4)

class TestDrawSprite(unittest.TestCase):
    def setUp(self):
        self.bitmap = DummyBitmap(width=10, height=10, colors=16)
    
    def test_draw_sprite_valid(self):
        pattern = [0, 1, 1, 0]  # 2x2 sprite pattern
        draw_sprite(self.bitmap, x=1, y=1, width=2, height=2, size=1, pattern=pattern, palette=None)
        self.assertEqual(self.bitmap[1, 1], 0)  # 0 value: pixel not drawn
        self.assertEqual(self.bitmap[2, 1], 1)
        self.assertEqual(self.bitmap[1, 2], 1)
        self.assertEqual(self.bitmap[2, 2], 0)
    
    def test_draw_sprite_invalid_length(self):
        pattern = [1, 1]  # Invalid for 2x2 sprite
        with self.assertRaises(ValueError):
            draw_sprite(self.bitmap, x=0, y=0, width=2, height=2, size=1, pattern=pattern, palette=None)
    
    def test_draw_sprite_negative_value(self):
        pattern = [0, -1, 1, 0]  # Contains negative value
        with self.assertRaises(ValueError):
            draw_sprite(self.bitmap, x=0, y=0, width=2, height=2, size=1, pattern=pattern, palette=None)

class TestDrawCube(unittest.TestCase):
    def setUp(self):
        self.bitmap = DummyBitmap(width=10, height=10, colors=16)
    
    def test_draw_cube(self):
        draw_cube(self.bitmap, x=2, y=2, width=3, height=3, size=1, palette=None)
        for x in range(2, 5):
            for y in range(2, 5):
                self.assertEqual(self.bitmap[x, y], 1)

class TestDrawTriangle(unittest.TestCase):
    def setUp(self):
        self.bitmap = DummyBitmap(width=10, height=10, colors=16)
    
    def test_draw_triangle_reflection1(self):
        draw_triangle(self.bitmap, x=0, y=0, width=4, height=4, size=1, reflection=1, palette=None)
        for x in range(4):
            self.assertEqual(self.bitmap[x, 3], 1)
    
    def test_draw_triangle_reflection0(self):
        with self.assertRaises(TypeError):
            draw_triangle(self.bitmap, x=0, y=0, width=4, height=4, size=1, reflection=0, palette=None)

class TestDrawZero(unittest.TestCase):
    def setUp(self):
        self.bitmap = decal_bitmap  # Use the global dummy decal_bitmap
    
    def test_draw_zero(self):
        draw_zero(5, 5, 1)
        self.assertNotEqual(self.bitmap[5, 5], 0)
        # You can add more assertions based on the expected pattern.

if __name__ == '__main__':
    unittest.main()
