"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

#to check if string is valid we check if each opening bracket is matched with a closing bracket
#to check if each opening bracket is matched with a closing bracket, iterate character by character. Reaching the end of the string means string is valid
#to iterate character by character, we add opening brackets to the queue, and check if closing brackters are valid given the queue
#to check if closing brackets are valid given the queue, we see if the queue is empty or if the latest bracket is matching
#to to check if the queue is empty, we check the length
#to check if the bracket is matching, we see if the valid_pairs[opening_bracket] matches the closing_bracket given 
#opening_bracket is the lastest bracket in the queue

opening_brackets = ['(',
                    '[',
                    '{']

closing_brackets = [')',
                    ']',
                    '}']

bracket_pairs = {"(":")",
                 "{":'}',
                 "[":']'}

def isValid(s):
    if not all_opening_brackets_match_closing_brackets(s):
        return(False)
    else:
        return(True)
    
def all_opening_brackets_match_closing_brackets(bracket_string):
    bracket_stack = []
    for bracket in bracket_string:
        if bracket_is_opening_bracket(bracket):
            bracket_stack.append(bracket)
        elif bracket_is_closing_bracket(bracket):
            if stack_is_empty(bracket_stack):
                return(False)
            previous_open_bracket = get_previous_open_bracket(bracket_stack)  
            if not bracket_closes_previous_open_bracket(bracket, previous_open_bracket):
                return(False)
    if not stack_is_empty(bracket_stack):
        return(False)
    return(True)

def bracket_closes_previous_open_bracket(closed_bracket, previous_open_bracket):
    return(bracket_pairs[previous_open_bracket] == closed_bracket)

def bracket_is_opening_bracket(bracket):
    return(bracket in opening_brackets)

def bracket_is_closing_bracket(bracket):
    return(bracket in closing_brackets)
def get_previous_open_bracket(bracket_stack):
    return(bracket_stack.pop())
    
def stack_is_empty(stack):
    return(not bool(stack))


