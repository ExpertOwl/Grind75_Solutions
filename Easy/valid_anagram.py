# -*- coding: utf-8 -*-
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

@author: Zanon
"""

from collections import defaultdict

def isAnagram(s, t):
   if count_letters(s) == count_letters(t):
       return(True)
   else:
       return(False)
         
def count_letters(string):
    letters_count = defaultdict(int)
    for char in string:
        letters_count[char] += 1
    return(letters_count)



    
    
