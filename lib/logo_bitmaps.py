"""
Library for defining bitmaps and palettes
=======================================================================================

Author(s): Michael Ladderbush
"""

from adafruit_matrixportal.matrix import Matrix
import displayio

# Create the Matrix object (this handles all the pin setup)
matrix = Matrix(width=64, height=64, bit_depth=5)

# Create a display from the matrix
display = matrix.display
color_convertor = displayio.ColorConverter(input_colorspace=displayio.Colorspace.RGB565)
group = displayio.Group()

# Create a bitmap and palette
background_bitmap = displayio.Bitmap(display.width, display.height, 16)
background_palette = displayio.Palette(6)
background_palette[1] = 0x000000  # black
background_palette[2] = 0x000000  # red
background_palette[3] = 0x000000  # blue
background_palette[4] = 0x000000  # green
background_palette[5] = 0x000000  # white

tilegrid_background = displayio.TileGrid(background_bitmap, pixel_shader=background_palette)
group.append(tilegrid_background)

decal_bitmap = displayio.Bitmap(display.width, display.height, 16)
decal_palette = displayio.Palette(3)
decal_palette.make_transparent(0)
decal_palette[1] = 0x000000  # black
decal_palette[2] = 0xFFFFFF  # white

tilegrid_decals = displayio.TileGrid(decal_bitmap, pixel_shader=decal_palette)
group.append(tilegrid_decals)




# CELTICS
celtics_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
celtics_logo_palette = displayio.Palette(6)
celtics_logo_palette.make_transparent(0)
celtics_logo_palette[1] = 0xffffff  # White
celtics_logo_palette[2] = 0xBA9653  # gold
celtics_logo_palette[3] = 0x963821  # brown
celtics_logo_palette[4] = 0x007A33  # Green
celtics_logo_palette[5] = 0xffffff  # White
tilegrid_celtics = displayio.TileGrid(celtics_logo_bitmap, pixel_shader=celtics_logo_palette)
group.append(tilegrid_celtics)




# CAVS
cavs_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
cavs_logo_palette = displayio.Palette(5)
cavs_logo_palette.make_transparent(0)
cavs_logo_palette[1] = 0x000033 #wine red
cavs_logo_palette[2] = 0x0099CC #gold
cavs_logo_palette[3] = 0x041E42 #navy
cavs_logo_palette[4] = 0x000000 #black
tilegrid_cavs = displayio.TileGrid(cavs_logo_bitmap, pixel_shader=cavs_logo_palette)
group.append(tilegrid_cavs)




# TRAIL BLAZERS
trail_blazers_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
trail_blazers_logo_palette = displayio.Palette(4)
trail_blazers_logo_palette.make_transparent(0)
trail_blazers_logo_palette[2] = 0x000000 # Black
trail_blazers_logo_palette[1] = 0x000033 # Red
trail_blazers_logo_palette[3] = 0xffffff # White
tilegrid_trail_blazers = displayio.TileGrid(trail_blazers_logo_bitmap, pixel_shader=trail_blazers_logo_palette)
group.append(tilegrid_trail_blazers)




# THUNDER
thunder_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
thunder_logo_palette = displayio.Palette(6)
thunder_logo_palette.make_transparent(0)
thunder_logo_palette[1] = 0xffffff
thunder_logo_palette[2] = 0xcc0000
thunder_logo_palette[3] = 0xffcc00
thunder_logo_palette[4] = 0x0033ff
thunder_logo_palette[5] = 0x0099ff
tilegrid_thunder = displayio.TileGrid(thunder_logo_bitmap, pixel_shader=thunder_logo_palette)
group.append(tilegrid_thunder)

# NETS
nets_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
nets_logo_palette = displayio.Palette(4)
nets_logo_palette.make_transparent(0)
nets_logo_palette[1] = 0xffffff
nets_logo_palette[2] = 0x000000
nets_logo_palette[3] = 0xff0000
tilegrid_nets = displayio.TileGrid(nets_logo_bitmap, pixel_shader=nets_logo_palette)
group.append(tilegrid_nets)

# KNICKS
knicks_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
knicks_logo_palette = displayio.Palette(6)
knicks_logo_palette.make_transparent(0)
knicks_logo_palette[1] = 0x000000
knicks_logo_palette[2] = 0x0033ff
knicks_logo_palette[3] = 0xff0000
knicks_logo_palette[4] = 0xffffff
knicks_logo_palette[5] = 0x000000
tilegrid_knicks = displayio.TileGrid(knicks_logo_bitmap, pixel_shader=knicks_logo_palette)
group.append(tilegrid_knicks)

# SIXERS
sixers_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
sixers_logo_palette = displayio.Palette(3)
sixers_logo_palette.make_transparent(0)
sixers_logo_palette[1] = 0x0000ff
sixers_logo_palette[2] = 0xff0000
tilegrid_sixers = displayio.TileGrid(sixers_logo_bitmap, pixel_shader=sixers_logo_palette)
group.append(tilegrid_sixers)

# RAPTORS
raptors_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
raptors_logo_palette = displayio.Palette(2)
raptors_logo_palette.make_transparent(0)
raptors_logo_palette[1] = 0x0000ff
tilegrid_raptors = displayio.TileGrid(raptors_logo_bitmap, pixel_shader=raptors_logo_palette)
group.append(tilegrid_raptors)

# BULLS
bulls_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
bulls_logo_palette = displayio.Palette(4)
bulls_logo_palette.make_transparent(0)
bulls_logo_palette[1] = 0x0000ff
bulls_logo_palette[2] = 0xffffff
bulls_logo_palette[3] = 0x000000
tilegrid_bulls = displayio.TileGrid(bulls_logo_bitmap, pixel_shader=bulls_logo_palette)
group.append(tilegrid_bulls)

# PISTONS
pistons_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
pistons_logo_palette = displayio.Palette(4)
pistons_logo_palette.make_transparent(0)
pistons_logo_palette[1] = 0xff0000
pistons_logo_palette[2] = 0x0000ff
pistons_logo_palette[3] = 0xffffff
tilegrid_pistons = displayio.TileGrid(pistons_logo_bitmap, pixel_shader=pistons_logo_palette)
group.append(tilegrid_pistons)

# PACERS
pacers_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
pacers_logo_palette = displayio.Palette(4)
pacers_logo_palette.make_transparent(0)
pacers_logo_palette[1] = 0x999999
pacers_logo_palette[2] = 0xff0000
pacers_logo_palette[3] = 0x00ccff
tilegrid_pacers = displayio.TileGrid(pacers_logo_bitmap, pixel_shader=pacers_logo_palette)
group.append(tilegrid_pacers)

# BUCKS
bucks_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
bucks_logo_palette = displayio.Palette(3)
bucks_logo_palette.make_transparent(0)
bucks_logo_palette[1] = 0x006600
bucks_logo_palette[2] = 0xffffff
tilegrid_bucks = displayio.TileGrid(bucks_logo_bitmap, pixel_shader=bucks_logo_palette)
group.append(tilegrid_bucks)

# HAWKS
hawks_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
hawks_logo_palette = displayio.Palette(3)
hawks_logo_palette.make_transparent(0)
hawks_logo_palette[1] = 0x0000ff
hawks_logo_palette[2] = 0xffffff
tilegrid_hawks = displayio.TileGrid(hawks_logo_bitmap, pixel_shader=hawks_logo_palette)
group.append(tilegrid_hawks)

# HORNETS
hornets_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
hornets_logo_palette = displayio.Palette(3)
hornets_logo_palette.make_transparent(0)
hornets_logo_palette[1] = 0xff0000
hornets_logo_palette[2] = 0xffffff
tilegrid_hornets = displayio.TileGrid(hornets_logo_bitmap, pixel_shader=hornets_logo_palette)
group.append(tilegrid_hornets)

# HEAT
heat_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
heat_logo_palette = displayio.Palette(6)
heat_logo_palette.make_transparent(0)
heat_logo_palette[1] = 0x0000ff
heat_logo_palette[2] = 0x0099ff
heat_logo_palette[3] = 0x000000
heat_logo_palette[4] = 0x0000ff
heat_logo_palette[5] = 0xffffff
tilegrid_heat = displayio.TileGrid(heat_logo_bitmap, pixel_shader=heat_logo_palette)
group.append(tilegrid_heat)

# MAGIC
magic_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
magic_logo_palette = displayio.Palette(4)
magic_logo_palette.make_transparent(0)
magic_logo_palette[1] = 0x888888
magic_logo_palette[2] = 0xff0000
magic_logo_palette[3] = 0xff9900
tilegrid_magic = displayio.TileGrid(magic_logo_bitmap, pixel_shader=magic_logo_palette)
group.append(tilegrid_magic)

# WIZARDS
wizards_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
wizards_logo_palette = displayio.Palette(4)
wizards_logo_palette.make_transparent(0)
wizards_logo_palette[1] = 0xff0000
wizards_logo_palette[2] = 0x0000ff
wizards_logo_palette[3] = 0x888888
tilegrid_wizards = displayio.TileGrid(wizards_logo_bitmap, pixel_shader=wizards_logo_palette)
group.append(tilegrid_wizards)

# NUGGETS
nuggets_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
nuggets_logo_palette = displayio.Palette(5)
nuggets_logo_palette.make_transparent(0)
nuggets_logo_palette[1] = 0xff0000
nuggets_logo_palette[2] = 0x0088ff
nuggets_logo_palette[3] = 0x0000ff
nuggets_logo_palette[4] = 0xffffff
tilegrid_nuggets = displayio.TileGrid(nuggets_logo_bitmap, pixel_shader=nuggets_logo_palette)
group.append(tilegrid_nuggets)

# TIMBERWOLVES
timberwolves_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
timberwolves_logo_palette = displayio.Palette(5)
timberwolves_logo_palette.make_transparent(0)
timberwolves_logo_palette[1] = 0xff0000
timberwolves_logo_palette[2] = 0x888888
timberwolves_logo_palette[3] = 0x00ff00
timberwolves_logo_palette[4] = 0x660000
tilegrid_timberwolves = displayio.TileGrid(timberwolves_logo_bitmap, pixel_shader=timberwolves_logo_palette)
group.append(tilegrid_timberwolves)

# JAZZ
jazz_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
jazz_logo_palette = displayio.Palette(5)
jazz_logo_palette.make_transparent(0)
jazz_logo_palette[1] = 0xffffff
tilegrid_jazz = displayio.TileGrid(jazz_logo_bitmap, pixel_shader=jazz_logo_palette)
group.append(tilegrid_jazz)

# WARRIORS
warriors_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
warriors_logo_palette = displayio.Palette(3)
warriors_logo_palette.make_transparent(0)
warriors_logo_palette[2] = 0xff0000
warriors_logo_palette[1] = 0x00ffff
tilegrid_warriors = displayio.TileGrid(warriors_logo_bitmap, pixel_shader=warriors_logo_palette)
group.append(tilegrid_warriors)

# CLIPPERS
clippers_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
clippers_logo_palette = displayio.Palette(5)
clippers_logo_palette.make_transparent(0)
clippers_logo_palette[1] = 0xff0000
clippers_logo_palette[2] = 0xffffff
clippers_logo_palette[3] = 0xff0000
clippers_logo_palette[4] = 0x0000ff
tilegrid_clippers = displayio.TileGrid(clippers_logo_bitmap, pixel_shader=clippers_logo_palette)
group.append(tilegrid_clippers)

# LAKERS
lakers_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
lakers_logo_palette = displayio.Palette(3)
lakers_logo_palette.make_transparent(0)
lakers_logo_palette[1] = 0x0088ff
lakers_logo_palette[2] = 0x660033
tilegrid_lakers = displayio.TileGrid(lakers_logo_bitmap, pixel_shader=lakers_logo_palette)
group.append(tilegrid_lakers)


# SUNS
suns_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
suns_logo_palette = displayio.Palette(5)
suns_logo_palette.make_transparent(0)
suns_logo_palette[1] = 0x000000
suns_logo_palette[2] = 0x0055ff
suns_logo_palette[3] = 0x00ccff
suns_logo_palette[4] = 0x00ccff
tilegrid_suns = displayio.TileGrid(suns_logo_bitmap, pixel_shader=suns_logo_palette)
group.append(tilegrid_suns)

# KINGS
kings_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
kings_logo_palette = displayio.Palette(3)
kings_logo_palette.make_transparent(0)
kings_logo_palette[1] = 0x660033
kings_logo_palette[2] = 0x888888
tilegrid_kings = displayio.TileGrid(kings_logo_bitmap, pixel_shader=kings_logo_palette)
group.append(tilegrid_kings)

# MAVERICKS
mavericks_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
mavericks_logo_palette = displayio.Palette(4)
mavericks_logo_palette.make_transparent(0)
mavericks_logo_palette[1] = 0xff0000
mavericks_logo_palette[2] = 0x000000
mavericks_logo_palette[3] = 0xffffff
tilegrid_mavericks = displayio.TileGrid(mavericks_logo_bitmap, pixel_shader=mavericks_logo_palette)
group.append(tilegrid_mavericks)

# ROCKETS
rockets_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
rockets_logo_palette = displayio.Palette(2)
rockets_logo_palette.make_transparent(0)
rockets_logo_palette[1] = 0x0000ff
tilegrid_rockets = displayio.TileGrid(rockets_logo_bitmap, pixel_shader=rockets_logo_palette)
group.append(tilegrid_rockets)

# GRIZZLIES
grizzlies_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
grizzlies_logo_palette = displayio.Palette(5)
grizzlies_logo_palette.make_transparent(0)
grizzlies_logo_palette[1] = 0xcc9999
grizzlies_logo_palette[2] = 0x0099ff
grizzlies_logo_palette[3] = 0x663300
grizzlies_logo_palette[4] = 0xffffff
tilegrid_grizzlies = displayio.TileGrid(grizzlies_logo_bitmap, pixel_shader=grizzlies_logo_palette)
group.append(tilegrid_grizzlies)

# PELICANS
pelicans_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
pelicans_logo_palette = displayio.Palette(5)
pelicans_logo_palette.make_transparent(0)
pelicans_logo_palette[1] = 0x0000ff
pelicans_logo_palette[2] = 0x0099cc
pelicans_logo_palette[3] = 0x330000
pelicans_logo_palette[4] = 0xff0000
tilegrid_pelicans = displayio.TileGrid(pelicans_logo_bitmap, pixel_shader=pelicans_logo_palette)
group.append(tilegrid_pelicans)

# SPURS
spurs_logo_bitmap = displayio.Bitmap(display.width, display.height, 16)
spurs_logo_palette = displayio.Palette(3)
spurs_logo_palette.make_transparent(0)
spurs_logo_palette[1] = 0x888888
spurs_logo_palette[2] = 0x111111
tilegrid_spurs = displayio.TileGrid(spurs_logo_bitmap, pixel_shader=spurs_logo_palette)
group.append(tilegrid_spurs)

display.root_group = group
