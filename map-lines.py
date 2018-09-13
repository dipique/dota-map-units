from PIL import Image, ImageDraw # python -m pip install pillow

input_file = "mini.bmp"
output_file = "mini_output.bmp"

MAP_WIDTH = 15000 # in units
MAP_HEIGHT = 15000

LINE_DISTANCE_W = 500 # in units
LINE_DISTANCE_H = 500 # in units

MAJOR_LINE_INC_W = 1500 # these needs to be a multiple of the line distance or they'll never appear
MAJOR_LINE_INC_H = 1500

MINOR_UNIT_FILL = 1   # width of the lines drawn, in pixels
MAJOR_UNIT_FILL = 2

line_count_w = int(MAP_WIDTH / LINE_DISTANCE_W)
line_count_h = int(MAP_HEIGHT / LINE_DISTANCE_H)

im = Image.open(input_file)
draw = ImageDraw.Draw(im)
img_width = im.size[0]
img_height = im.size[1]
line_color = (0,0,0,255)  # RGBA

units_per_pixel_width = int(MAP_WIDTH / img_width)
units_per_pixel_height = int(MAP_HEIGHT / img_height)

# draw the lines from top to bottom
for l in range(line_count_w):
    units = (l + 1) * LINE_DISTANCE_W
    fill = MAJOR_UNIT_FILL if units % MAJOR_LINE_INC_W == 0 else MINOR_UNIT_FILL
    x = int(units / units_per_pixel_width)
    draw.line([(x, 1), (x, img_height)], line_color, fill)

# draw the lines from left to right
for l in range(line_count_h):
    units = (l + 1) * LINE_DISTANCE_H
    fill = MAJOR_UNIT_FILL if units % MAJOR_LINE_INC_H == 0 else MINOR_UNIT_FILL
    y = int(units / units_per_pixel_height)
    draw.line([(1, y), (img_width, y)], line_color, fill)

# save img
im.save(output_file)