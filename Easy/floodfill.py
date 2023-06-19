# -*- coding: utf-8 -*-
"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""


from collections import defaultdict 

def floodfill(image, sr, sc, color):
    visited = defaultdict(bool)
    origional_color = image[sr][sc]
    image = BFS_fill(image, (sr, sc), color, visited, origional_color)
    return(image)


def BFS_fill(image, pixel, new_color, visited, origional_color):
    i, j = pixel
    if not pixel_is_valid(pixel, visited, image, origional_color):
        return(None)
    else:
        visited[pixel] = True
        image[i][j] = new_color
        neighbors = get_adjacent_pixels(i,j)
        for adjacent_pixel in neighbors:
            BFS_fill(image, adjacent_pixel, new_color, visited, origional_color)
    return(image)

def pixel_is_valid(pixel, visited, image, origional_color):
    if pixel_visited(pixel, visited) or pixel_outside_of_image(pixel, image) or pixel_does_not_match_origional_color(pixel, image, origional_color):
           return(False)
    else:
        return(True)
    
def pixel_visited(pixel, visited):
    return(visited[pixel])

def pixel_outside_of_image(pixel, image):
    image_height = len(image)
    image_width = len(image[0]) 
    i,j = pixel
    if 0 <= i < image_height and 0 <= j < image_width:
        return(False)
    else:
        return(True)

def pixel_does_not_match_origional_color(pixel, image, origional_color):
    i,j = pixel
    return(image[i][j] != origional_color)

def get_adjacent_pixels(i,j): 
    adjacent_pixels = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] 
    return(adjacent_pixels)
