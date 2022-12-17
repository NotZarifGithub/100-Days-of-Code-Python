import colorgram

colors = colorgram.extract("spot_painting.jpg", 34)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)

print(rgb_colors)