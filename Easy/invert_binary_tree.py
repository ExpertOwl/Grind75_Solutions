# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:29:57 2023

@author: Zanon
"""

class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def invertTree(tree):
    if tree == None:
        return(None)
    else:
        invertTree(tree.left)
        invertTree(tree.right)
        tree.left, tree.right = tree.right, tree.left
        return(tree)