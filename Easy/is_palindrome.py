# -*- coding: utf-8 -*-
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


#TO see if a phrase is a valid palindrome, we first remmove all non-alphanumeric characters, we then convert all letters to lower case, then see if it reads the same forwards and backwards s[i] = s[n-i] 
#To remove all non-alphanumeric characters, we use filter with  pythons str.is_alnum()
#TO convert all letters to lower case, we use pythons str.lower()
#To see if word reads the same front to back, we can do str == reversed(str)

def isPalindrome(s):
    s = remove_alphanum(s)
    s = convert_to_lowercase(s)
    return(check_palindrome(s))

def remove_alphanum(string):
    filtered_string = filter(str.isalnum, string)
    string = rejoin(filtered_string)
    return(string)
    
def char_is_alnum(char):
    return(char.isalnum())
    
def rejoin(s):
    return("".join(s))

def convert_to_lowercase(s):
    return(s.lower())    

def check_palindrome(s):
    return(s == rejoin(reversed(s)))

isPalindrome("A man, a plan, a canal: Panama")