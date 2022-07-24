from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utilsV2
import cv2
import webcolors
import os

import numpy as np
import sys
import collections


def convert_color(color_code):
    # Check color from web color : http://wow.in.th/PptJ
    color = color_code
    color_name = ''
    red_color = ['INDIANRED', 'LIGHTCORAL', 'SALMON', 'DARKSALMON', 'LIGHTSALMON', 'CRIMSON', 'RED', 'FIREBRICK',
                 'DARKRED']
    pink_color = ['PINK', 'LIGHTPINK', 'HOTPINK', 'DEEPPINK', 'MEDIUMVIOLETRED', 'PALEVIOLETRED']
    orenge_color = ['LIGHTSALMON', 'CORAL', 'TOMATO', 'ORANGERED', 'DARKORANGE', 'ORANGE']
    yellow_color = ['GOLD', 'YELLOW', 'LIGHTYELLOW', 'LEMONCHIFFON', 'LIGHTGOLDENRODYELLOW', 'PAPAYAWHIP', 'MOCCASIN',
                    'PEACHPUFF', 'PALEGOLDENROD', 'KHAKI', 'DARKKHAKI']
    purple_color = ['THISTLE', 'PLUM', 'VIOLET', 'ORCHID', 'FUCHSIA', 'MAGENTA', 'MEDIUMORCHID', 'MEDIUMPURPLE',
                    'REBECCAPURPLE', 'BLUEVIOLET', 'DARKVIOLET', 'DARKORCHID', 'DARKMAGENTA', 'PURPLE', 'INDIGO',
                    'SLATEBLUE', 'DARKSLATEBLUE', 'MEDIUMSLATEBLUE']
    green_color = ['GREENYELLOW', 'CHARTREUSE', 'LAWNGREEN', 'LIME', 'LIMEGREEN', 'PALEGREEN', 'LIGHTGREEN',
                   'MEDIUMSPRINGGREEN', 'SPRINGGREEN', 'MEDIUMSEAGREEN', 'SEAGREEN', 'FORESTGREEN', 'GREEN',
                   'DARKGREEN', 'YELLOWGREEN', 'OLIVEDRAB', 'OLIVE', 'DARKOLIVEGREEN', 'MEDIUMAQUAMARINE',
                   'DARKSEAGREEN', 'LIGHTSEAGREEN', 'DARKCYAN', 'TEAL']
    blue_color = ['AQUA', 'CYAN', 'LIGHTCYAN', 'PALETURQUOISE', 'AQUAMARINE', 'TURQUOISE', 'MEDIUMTURQUOISE',
                  'DARKTURQUOISE', 'CADETBLUE', 'STEELBLUE', 'LIGHTSTEELBLUE', 'POWDERBLUE', 'LIGHTBLUE', 'SKYBLUE',
                  'LIGHTSKYBLUE', 'DEEPSKYBLUE', 'DODGERBLUE', 'CORNFLOWERBLUE', 'MEDIUMSLATEBLUE', 'ROYALBLUE', 'BLUE',
                  'MEDIUMBLUE', 'DARKBLUE', 'NAVY', 'MIDNIGHTBLUE']
    brown_color = ['CORNSILK', 'BLANCHEDALMOND', 'BISQUE', 'NAVAJOWHITE', 'WHEAT', 'BURLYWOOD', 'TAN', 'ROSYBROWN',
                   'SANDYBROWN', 'GOLDENROD', 'DARKGOLDENROD', 'PERU', 'CHOCOLATE', 'SADDLEBROWN', 'SIENNA', 'BROWN',
                   'MAROON']
    white_color = ['LAVENDER', 'WHITE', 'SNOW', 'HONEYDEW', 'MINTCREAM', 'AZURE', 'ALICEBLUE', 'GHOSTWHITE',
                   'WHITESMOKE', 'SEASHELL', 'BEIGE', 'OLDLACE', 'FLORALWHITE', 'IVORY', 'ANTIQUEWHITE', 'LINEN',
                   'LAVENDERBLUSH', 'MISTYROSE']
    gray_color = ['GAINSBORO', 'LIGHTGRAY', 'SILVER', 'DARKGRAY', 'GRAY', 'DIMGRAY', 'LIGHTSLATEGRAY', 'SLATEGRAY',
                  'DARKSLATEGRAY', 'BLACK']

    if color.upper() in red_color:
        print('RED')
        color_name = 'RED'
        return color_name
    elif color.upper() in pink_color:
        print('PINK')
        color_name = 'PINK'
        return color_name
    elif color.upper() in orenge_color:
        print('ORANGE')
        color_name = 'ORANGE'
        return color_name
    elif color.upper() in yellow_color:
        print('YELLOW')
        color_name = 'YELLOW'
        return color_name
    elif color.upper() in purple_color:
        print('PURPLE')
        color_name = 'PURPLE'
        return color_name
    elif color.upper() in green_color:
        print('GREEN')
        color_name = 'GREEN'
        return color_name
    elif color.upper() in blue_color:
        print('BLUE')
        color_name = 'BLUE'
        return color_name
    elif color.upper() in brown_color:
        print('BROWN')
        color_name = 'BROWN'
        return color_name
    elif color.upper() in white_color:
        print('WHITE')
        color_name = 'WHITE'
        return color_name
    elif color.upper() in gray_color:
        print('GRAY')
        color_name = 'GRAY'
        return color_name
    else:
        print('ai cant find color ...')
        color_name = 'Unknown'
        return color_name


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

filename = "car.jpg"

Kcolors = cv2.imread(filename)
Kcolors = cv2.cvtColor(Kcolors, cv2.COLOR_BGR2RGB)
Kcolors = Kcolors.reshape((Kcolors.shape[0] * Kcolors.shape[1], 3))
clt = KMeans(n_clusters=2)
clt.fit(Kcolors)
hist = utilsV2.centroid_histogram(clt)
print("Histogram : ", hist)
bar = utilsV2.plot_colors(hist, clt.cluster_centers_)
requested_colour = (bar[1], bar[2], bar[3])
actual_name, closest_name = get_colour_name(requested_colour)
##self.label_color.setText('Color  : ' + closest_name)
# print("Actual colour name:", actual_name, " group color : ", closest_name)
convert_name_color = convert_color(closest_name)
