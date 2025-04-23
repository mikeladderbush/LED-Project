"""
Library for interpreting logic and presenting it on the display using Adafruit libraries
=======================================================================================

Author(s): Michael Ladderbush
"""

from adafruit_matrixportal.matrix import Matrix
import displayio
import board
import time
from logo_bitmaps import *
from logos import *
import re

class nba_team:
    def __init__(self, bitmap, palette, pattern):
        self.bitmap = bitmap
        self.palette = palette
        self.pattern = pattern

# Eastern Conference teams
hawks = nba_team(hawks_logo_bitmap, hawks_logo_palette, hawks_pattern)
celtics = nba_team(celtics_logo_bitmap, celtics_logo_palette, celtics_pattern)
nets = nba_team(nets_logo_bitmap, nets_logo_palette, nets_pattern)
hornets = nba_team(hornets_logo_bitmap, hornets_logo_palette, hornets_pattern)
bulls = nba_team(bulls_logo_bitmap, bulls_logo_palette, bulls_pattern)
cavs = nba_team(cavs_logo_bitmap, cavs_logo_palette, cavs_pattern)
pistons = nba_team(pistons_logo_bitmap, pistons_logo_palette, pistons_pattern)
pacers = nba_team(pacers_logo_bitmap, pacers_logo_palette, pacers_pattern)
heat = nba_team(heat_logo_bitmap, heat_logo_palette, heat_pattern)
bucks = nba_team(bucks_logo_bitmap, bucks_logo_palette, bucks_pattern)
knicks = nba_team(knicks_logo_bitmap, knicks_logo_palette, knicks_pattern)
magic = nba_team(magic_logo_bitmap, magic_logo_palette, magic_pattern)
sixers = nba_team(sixers_logo_bitmap, sixers_logo_palette, sixers_pattern)
raptors = nba_team(raptors_logo_bitmap, raptors_logo_palette, raptors_pattern)
wizards = nba_team(wizards_logo_bitmap, wizards_logo_palette, wizards_pattern)

# Western Conference teams
mavericks = nba_team(mavericks_logo_bitmap, mavericks_logo_palette, mavericks_pattern)
nuggets = nba_team(nuggets_logo_bitmap, nuggets_logo_palette, nuggets_pattern)
warriors = nba_team(warriors_logo_bitmap, warriors_logo_palette, warriors_pattern)
rockets = nba_team(rockets_logo_bitmap, rockets_logo_palette, rockets_pattern)
clippers = nba_team(clippers_logo_bitmap, clippers_logo_palette, clippers_pattern)
lakers = nba_team(lakers_logo_bitmap, lakers_logo_palette, lakers_pattern)
grizzlies = nba_team(grizzlies_logo_bitmap, grizzlies_logo_palette, grizzlies_pattern)
timberwolves = nba_team(timberwolves_logo_bitmap, timberwolves_logo_palette, timberwolves_pattern)
pelicans = nba_team(pelicans_logo_bitmap, pelicans_logo_palette, pelicans_pattern)
thunder = nba_team(thunder_logo_bitmap, thunder_logo_palette, thunder_pattern)
suns = nba_team(suns_logo_bitmap, suns_logo_palette, suns_pattern)
trail_blazers = nba_team(trail_blazers_logo_bitmap, trail_blazers_logo_palette, trail_blazers_pattern)
kings = nba_team(kings_logo_bitmap, kings_logo_palette, kings_pattern)
spurs = nba_team(spurs_logo_bitmap, spurs_logo_palette, spurs_pattern)
jazz = nba_team(jazz_logo_bitmap, jazz_logo_palette, jazz_pattern)

# Helper to assign team with just a name.
def team_from_string(team_name) -> nba_team:
    teams = {
        "hawks": hawks,
        "celtics": celtics,
        "nets": nets,
        "hornets": hornets,
        "bulls": bulls,
        "cavaliers": cavs,
        "mavericks": mavericks,
        "nuggets": nuggets,
        "pistons": pistons,
        "warriors": warriors,
        "rockets": rockets,
        "pacers": pacers,
        "lakers": lakers,
        "clippers": clippers,
        "grizzlies": grizzlies,
        "heat": heat,
        "bucks": bucks,
        "timberwolves": timberwolves,
        "pelicans": pelicans,
        "knicks": knicks,
        "thunder": thunder,
        "magic": magic,
        "sixers": sixers,
        "suns": suns,
        "blazers": trail_blazers,
        "kings": kings,
        "spurs": spurs,
        "raptors": raptors,
        "jazz": jazz,
        "wizards": wizards
    }

    opponent_team = teams.get(team_name)

    return opponent_team

# Draws a pixel on the given bitmap at the specified (x, y) coordinate using the provided color.
def draw_pixel(bitmap, x, y, my_color):
    bitmap[x, y] = my_color

# Draws a horizontal row of pixels on the given bitmap.
# The row starts at the left edge and spans 'length' pixels at the specified y coordinate using the given color.
def draw_row_singular(bitmap, length, y, my_color):
    for x in range(length):
        draw_pixel(bitmap, x, y, my_color)

# Draws multiple horizontal rows on the given bitmap.
# Starting at 'start_loc', 'num_rows' rows are drawn, each spanning 'length' pixels, in the specified color.
def draw_rows(bitmap, start_loc, num_rows, length, my_color):
    for row in range(start_loc, start_loc + num_rows):
        draw_row_singular(bitmap, length, row, my_color)

# Draws a vertical column of pixels on the given bitmap.
# The column spans 'length' pixels at the specified x coordinate using the provided color.
def draw_column_singular(bitmap, length, x, my_color):
    for y in range(length):
        draw_pixel(bitmap, x, y, my_color)

# Draws multiple vertical columns on the given bitmap.
# Starting at 'start_loc', 'num_columns' columns are drawn, each spanning 'length' pixels, in the specified color.
def draw_columns(bitmap, start_loc, num_columns, length, my_color):
    for column in range(start_loc, start_loc + num_columns):
        draw_column_singular(bitmap, length, column, my_color)

# Scales a flat pattern by repeating each pixel value according to the specified scale factor.
# Returns the scaled pattern along with the new width and height.
def scale_pattern(pattern, original_width, original_height, scale):
    new_pattern = []
    for row in range(original_height):
        scaled_row = []
        for column in range(original_width):
            pixel = pattern[row * original_width + column]
            scaled_row.extend([pixel] * scale)
        for value in range(scale):
            new_pattern.extend(scaled_row)
    
    new_width = original_width * scale
    new_height = original_height * scale
    return new_pattern, new_width, new_height

# Draws a sprite on the given bitmap.
# The sprite is defined by its width, height, scale (size), pattern, and palette.
# The pattern is first scaled; then each non-zero value in the scaled pattern is drawn on the bitmap.
def draw_sprite(bitmap, x, y, width, height, size, pattern, palette):
    scaled_pattern, new_width, new_height = scale_pattern(pattern, width, height, size)

    if len(pattern) != width * height:
        raise ValueError("Pattern length doesn't match sprite dimensions")

    for row in range(new_height):
        for col in range(new_width):
            index = row * new_width + col
            pattern_index_value = scaled_pattern[index]

            if 0 == pattern_index_value:
                continue
            if 0 < pattern_index_value:
                bitmap[x + col, y + row] = pattern_index_value  # Assign index, not hex color
            else:
                raise ValueError(f"Pattern index {pattern_index_value} out of range (0-{bitmap.colors - 1})")

# Draws a cube on the given bitmap by creating a pattern filled with ones and then calling draw_sprite.
def draw_cube(bitmap, x, y, width, height, size, palette):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    cube_pattern = [1] * (width * height)
    draw_sprite(bitmap, x, y, width, height, size, cube_pattern, palette)

# Draws a triangle on the given bitmap.
# The triangle can be rendered with two different reflections, controlled by the 'reflection' parameter.
def draw_triangle(bitmap, x, y, width, height, size, reflection, palette):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    triangle_pattern = []
    if reflection == 0:
        for row in range(height):
            pixels = (row + 1) * width // height
            if pixels < 1:
                pixels = 1
            row_pattern = [1] * pixels + [0] * (width - pixels)
            triangle_pattern.extend(row_pattern)
        
        draw_sprite(bitmap, x, y, width, height, triangle_pattern, palette)
    if reflection == 1:
        for row in range(height):
            pixels = (row + 1) * width // height
            if pixels < 1:
                pixels = 1
            row_pattern = [0] * (width - pixels) + [1] * pixels
            triangle_pattern.extend(row_pattern)
        
        draw_sprite(bitmap, x, y, width, height, size, triangle_pattern, palette)

# Draws a number on the display by mapping the digit to its corresponding drawing function.
def draw_number(number, x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    def get_number(number):
        return {
            1: lambda: draw_one(x, y, size),
            2: lambda: draw_two(x, y, size),
            3: lambda: draw_three(x, y, size),
            4: lambda: draw_four(x, y, size),
            5: lambda: draw_five(x, y, size),
            6: lambda: draw_six(x, y, size),
            7: lambda: draw_seven(x, y, size),
            8: lambda: draw_eight(x, y, size),
            9: lambda: draw_nine(x, y, size)
        }.get(number, lambda: draw_zero(x, y, size))()
    
    get_number(number)

# Draws a colon on the display using a predefined pattern.
def draw_colon(x, y, size):
    pattern = (
        0, 0, 0,
        0, 2, 0,
        0, 0, 0,
        0, 2, 0,
        0, 0, 0,
    )

    draw_sprite(decal_bitmap, x, y, 3, 5, size, pattern, decal_palette)

# Draws a dash on the display using a predefined pattern.
def draw_dash(x, y, size):
    pattern = (
        0, 0, 0,
        0, 0, 2,
        0, 2, 0,
        2, 0, 0,
        0, 0, 0,
    )

    draw_sprite(decal_bitmap, x, y, 3, 5, size, pattern, decal_palette)

# Draws the digit '0' on the display using a predefined pattern.
def draw_zero(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 2, 0, 2,
        0, 2, 0, 2,
        0, 2, 0, 2,
        0, 2, 2, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the digit '1' on the display using a predefined pattern.
def draw_one(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 0, 2, 0,
        0, 2, 2, 0,
        0, 0, 2, 0,
        0, 0, 2, 0,
        0, 2, 2, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the digit '2' on the display using a predefined pattern.
def draw_two(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 0, 0, 2,
        0, 2, 2, 2,
        0, 2, 0, 0,
        0, 2, 2, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the digit '3' on the display using a predefined pattern.
def draw_three(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 0, 0, 2,
        0, 0, 2, 2,
        0, 0, 0, 2,
        0, 2, 2, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the digit '4' on the display using a predefined pattern.
def draw_four(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 0, 2,
        0, 2, 0, 2,
        0, 2, 2, 2,
        0, 0, 0, 2,
        0, 0, 0, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the digit '5' on the display using a predefined pattern.
def draw_five(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 2, 0, 0,
        0, 2, 2, 2,
        0, 0, 0, 2,
        0, 2, 2, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the digit '6' on the display using a predefined pattern.
def draw_six(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 2, 0, 0,
        0, 2, 2, 2,
        0, 2, 0, 2,
        0, 2, 2, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the digit '7' on the display using a predefined pattern.
def draw_seven(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 0, 0, 2,
        0, 0, 2, 0,
        0, 0, 2, 0,
        0, 0, 2, 0,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the digit '8' on the display using a predefined pattern.
def draw_eight(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 2, 0, 2,
        0, 2, 2, 2,
        0, 2, 0, 2,
        0, 2, 2, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the digit '9' on the display using a predefined pattern.
def draw_nine(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 2, 0, 2,
        0, 2, 2, 2,
        0, 0, 0, 2,
        0, 0, 0, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the letter 'A' on the display using a predefined pattern.
def draw_a(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 2, 0, 2,
        0, 2, 2, 2,
        0, 2, 0, 2,
        0, 2, 0, 2,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the letter 'P' on the display using a predefined pattern.
def draw_p(x, y, size):
    clear_area(decal_bitmap, x, y, 4 * size, 5 * size)
    pattern = (
        0, 2, 2, 2,
        0, 2, 0, 2,
        0, 2, 2, 2,
        0, 2, 0, 0,
        0, 2, 0, 0,
    )

    draw_sprite(decal_bitmap, x, y, 4, 5, size, pattern, decal_palette)

# Draws the team logos on the display.
# The 'home_or_away' parameter determines the logo position on the bitmap.
def draw_logo(team, x, y, home_or_away):

    width = 32
    height = 32
    size = 1

    if home_or_away == 0:
        draw_sprite(team.bitmap, x, y, width, height, size, team.pattern, team.palette)
    if home_or_away == 1:
        draw_sprite(team.bitmap, x + 32, y, width, height, size, team.pattern, team.palette)

# Draws the game score on the display.
# The score is split into hundreds, tens, and ones and drawn separately.
def draw_score(home_score, away_score):
    # Home team
    home_score_hundreds = (home_score // 100) % 10
    home_score_tens = (home_score // 10) % 10
    home_score_ones = home_score % 10

    if home_score_hundreds > 0:
        draw_number(home_score_hundreds, 4, 48, 2)
        draw_number(home_score_tens, 12, 48, 2)
        draw_number(home_score_ones, 20, 48, 2)
    else:
        draw_number(home_score_tens, 12, 48, 2)
        draw_number(home_score_ones, 20, 48, 2)

    # Away team
    away_score_hundreds = (away_score // 100) % 10
    away_score_tens = (away_score // 10) % 10
    away_score_ones = away_score % 10

    if away_score_hundreds > 0:
        draw_number(away_score_hundreds, 36, 48, 2)
        draw_number(away_score_tens, 44, 48, 2)
        draw_number(away_score_ones, 52, 48, 2)
    else:
        draw_number(away_score_tens, 44, 48, 2)
        draw_number(away_score_ones, 52, 48, 2)


def format_clock(clock_str):
    if not clock_str:
        return "00:00"

    match = re.match(r"PT(?:(\d+)M)?(?:(\d+)(?:\.\d+)?S)?", clock_str)
    if match:
        minutes = int(match.group(1) or 0)
        seconds = int(match.group(2) or 0)
        return f"{minutes:02d}:{seconds:02d}"

    return clock_str  # Assume it's already in MM:SS or HH:MM format


def draw_clock(clock_str):
    if not isinstance(clock_str, str) or not clock_str:
        clock_str = "12:00"  # Default fallback
    
    # Case 1: Format is PT-style (NBA game clock)
    if "PT" in clock_str:
        clock_str = format_clock(clock_str)

    # Case 2: AM/PM Clock
    if "AM" in clock_str or "PM" in clock_str:
        try:
            time, am_pm = clock_str.split()
            hours, minutes = map(int, time.split(":"))

            draw_number(hours // 10, 15, 31, 2) if hours >= 10 else None
            draw_number(hours % 10, 21, 31, 2)
            draw_colon(29, 31, 2)
            draw_number(minutes // 10, 33, 31, 2)
            draw_number(minutes % 10, 40, 31, 2)
            
            if am_pm == "AM":
                draw_a(48, 36, 1)
            else:
                draw_p(48, 36, 1)
        except ValueError as e:
            print("AM/PM time format error:", e)

    # Case 3: MM:SS Clock
    else:
        try:
            minutes, seconds = map(int, clock_str.split(":"))
            draw_number(minutes // 10, 15, 31, 2) if minutes >= 10 else None
            draw_number(minutes % 10, 21, 31, 2)
            draw_colon(29, 31, 2)
            draw_number(seconds // 10, 32, 31, 2)
            draw_number(seconds % 10, 40, 31, 2)
        except ValueError as e:
            print("MM:SS time format error:", e)
            # Draw fallback clock
            draw_number(1, 18, 30, 2)
            draw_number(2, 24, 30, 2)
            draw_colon(31, 30, 2)
            draw_number(0, 34, 30, 2)
            draw_number(0, 42, 30, 2)


# Draws the game date on the display.
# The game date is converted into individual digits and separated by dashes.
def draw_date(game_date):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    game_year = 25
    game_month = 1
    game_day = 1

    for days in days_in_month:
        if game_date < days:
            game_day = game_date
            break
        game_date = game_date - days
        game_month = game_month + 1
    game_month = game_month - 1

    game_month_tens = game_month // 10
    game_month_ones = game_month % 10
    game_day_tens = game_day // 10
    game_day_ones = (game_day % 10)
    game_year_tens = game_year // 10
    game_year_ones = game_year % 10

    if game_month_tens > 0:
        draw_number(game_month_tens, 1, 50, 2)
    draw_number(game_month_ones, 7, 50, 2)
    draw_dash(16, 50, 2)
    if game_day_tens > 0:
        draw_number(game_day_tens, 21, 50, 2)
    draw_number(game_day_ones, 28, 50, 2)
    draw_dash(37, 50, 2)
    if game_year_tens > 0:
        draw_number(game_year_tens, 42, 50, 2)
    draw_number(game_year_ones, 49, 50, 2)

# Draws a future game on the display by selecting team logos, game time, and date.
def draw_future_game(game_date, game_time, game_location, game_opponent):
    teams = {
        "Atlanta": hawks,
        "Boston": celtics,
        "Brooklyn": nets,
        "Charlotte": hornets,
        "Chicago": bulls,
        "Cleveland": cavs,
        "Dallas": mavericks,
        "Denver": nuggets,
        "Detroit": pistons,
        "Golden State": warriors,
        "Houston": rockets,
        "Indiana": pacers,
        "Los Angeles Lakers": lakers,
        "Los Angeles Clippers": clippers,
        "Memphis": grizzlies,
        "Miami": heat,
        "Milwaukee": bucks,
        "Minnesota": timberwolves,
        "New Orleans": pelicans,
        "New York": knicks,
        "Oklahoma City": thunder,
        "Orlando": magic,
        "Philadelphia": sixers,
        "Phoenix": suns,
        "Portland": trail_blazers,
        "Sacramento": kings,
        "San Antonio": spurs,
        "Toronto": raptors,
        "Utah": jazz,
        "Washington": wizards
    }

    opponent_team = teams.get(game_opponent)

    draw_logo(celtics, 0, 0, 0)
    draw_logo(opponent_team, 0, 0, 1)
    draw_clock(game_time)
    draw_date(game_date)

def clear_area(bitmap, x, y, width, height):
    for i in range(x, x + width):
        for j in range(y, y + height):
            bitmap[i, j] = 0

