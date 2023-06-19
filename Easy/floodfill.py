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
    pixels_to_recolor = []
    image = BFS_fill(image, sr, sc, color, visited, origional_color)
    return(image)


def BFS_fill(image, i, j, new_color, visited, origional_color):
    
    print(f'visiting {i}, {j}')
    if i == 0 and j == 1 :
        pass
    if visited[(i,j)]:
        print(f"alreadt visited {i},{j}")
        return(None)
    if not 0 <= i <= len(image)-1:
        print('invalid i')
        return(None)
    elif not  0 <= j <= len(image[0])-1:
        print('invalid j')
        return(None)
    elif image[i][j] != origional_color:
        print('color does not match')
        return(None)
    else:
        visited[i,j] = True
        print('fill criteria met')
        image[i][j] = new_color
        BFS_fill(image, i-1, j, new_color, visited, origional_color)
        BFS_fill(image, i+1, j, new_color, visited, origional_color)
        BFS_fill(image, i, j-1, new_color, visited, origional_color)
        BFS_fill(image, i, j+1, new_color, visited, origional_color)
    return(image)
    
    
image = [[1,1,1],[1,1,0],[1,0,1]]
expected = [[2,2,2],[2,2,0],[2,0,1]]
sr = 1
sc = 1
color = 2

test = floodfill(image, sr, sc, color)

visited = [[False] * len(image)] * len(image[sr])
print(test == expected)