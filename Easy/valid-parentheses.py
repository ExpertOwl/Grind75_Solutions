"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""
bracket_pairs = {"(":")",
                 "[":"]",
                 "{":"}"}

closing_brackets = list(bracket_pairs.values()) 
opening_brackets = list(bracket_pairs.keys())

def isValid(bracket_string):
    ordered_opening_brackets, ordered_closing_brackets = separate_brackets(bracket_string)  
    if not all_brackets_are_paired(ordered_opening_brackets, ordered_closing_brackets):
        return(False)
    if not all_pairs_are_valid(ordered_opening_brackets, ordered_closing_brackets):
        return(False)
    return(True)

def separate_brackets(bracket_string):
    ordered_opening_brackets = []
    ordered_closing_brackets = []
    for bracket in bracket_string:
        if bracket in opening_brackets:
            ordered_opening_brackets.append(bracket)
        else:
            ordered_closing_brackets.append(bracket)
    ordered_closing_brackets = reverse_list(ordered_closing_brackets)
    return(ordered_opening_brackets, ordered_closing_brackets)

def all_brackets_are_paired(opening, closing):
    result = len(opening) == len(closing)
    return(result)

def all_pairs_are_valid(opening, closing):
    for index in range(len(opening)): 
        if not is_valid_bracket_pair(opening.pop(), closing.pop()):
            return(False)
    return(True)

def is_valid_bracket_pair(open_bracket, close_bracket):
    if bracket_pairs[open_bracket] == close_bracket:
        return(True)
    return(False)

def reverse_list(list_to_reverse):
    reversed_list = list(reversed(list_to_reverse))
    return(reversed_list)
print(isValid("([)]"))