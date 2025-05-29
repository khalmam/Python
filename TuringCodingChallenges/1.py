# Given a strings containing just the characters '(', ')' '{', '}', '[' and ']' , determine if the

# Input string is valid

# An input string is valid if

# 1. Open brackets must be closed by the same type of brackets.

# 2. Open brackets must be closed in the correct order.


def isValid(s: str) -> bool:
    """
    Determines if a string containing only '(', ')', '{', '}', '[' and ']' is valid
    based on bracket matching and order.

    Args:
        s: The input string.

    Returns:
        True if the string is valid, False otherwise.
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            # If it's a closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)

    # The string is valid if the stack is empty at the end
    return not stack

if __name__ == "__main__":
    input_string = input("Enter a string of brackets: ")
    if isValid(input_string):
        print("Valid")
    else:
        print("Invalid")




# Explanation:

# stack = []: We initialize an empty list called stack. This stack will be used to keep track of the opening brackets encountered.

# mapping = {")": "(", "}": "{", "]": "["}: We create a dictionary mapping to store the corresponding opening bracket for each closing bracket. This allows for quick lookups to check if a closing bracket matches the last opened one.

# for char in s:: We iterate through each character in the input string s.

# if char in mapping:: If the current character char is a closing bracket (i.e., it's a key in our mapping dictionary):

# top_element = stack.pop() if stack else '#': We attempt to pop the last added element from the stack.
# If the stack is not empty, stack.pop() retrieves and removes the most recent opening bracket.
# If the stack is empty when we encounter a closing bracket, it means there's no corresponding opening bracket, so we assign a special character '#' to top_element to indicate a mismatch.
# if mapping[char] != top_element:: We check if the corresponding opening bracket for the current closing bracket (obtained from the mapping) is the same as the top_element we just popped. If they don't match, it violates the "same type" rule, and the string is invalid, so we return False.
# else:: If the current character char is an opening bracket (i.e., it's not in the mapping dictionary):

# stack.append(char): We push the opening bracket onto the stack. This signifies that we've encountered an opening bracket that needs to be closed later. The order in which we push and pop from the stack ensures the "correct order" of closing.
# return not stack: After processing the entire string, if the stack is empty, it means all opened brackets have been correctly closed. An empty stack signifies a valid string, so we return True (because not [] evaluates to True). If the stack is not empty, it means there are unclosed opening brackets, making the string invalid, and we return False.


# feat: Implement interactive bracket validity check

# The isValid function remains the same, but the script now includes
# a main execution block (`if __name__ == "__main__":`) that:

# - Prompts the user to enter a string of brackets using `input()`.
# - Calls the `isValid()` function with the user's input.
# - Prints "Valid" or "Invalid" to the console based on the function's return value.

# This change makes the script directly executable for testing and demonstration.