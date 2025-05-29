# Baseball Game

# You are keeping score for a baseball game with strange rules. The game consists of several rounds,

#  where the scores of past rounds may affect future rounds' scores.

# At the beginning of the game, you start with an empty record. You are given a list of strings ops.

# where ops [1] is the ith operation you must apply to the record and is one of the following:

# 1. An integer x Record a new score of x.

# 2.Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.

# 3. "o" Record a new score that is double the previous score. It is guaranteed there will always be a previous score.

# 4. "c" Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.

# Return the sum of all the scores on the record.

def calculate_baseball_score(ops):
    """
    Calculates the total score of a baseball game with unusual rules.

    Args:
        ops: A list of strings representing the operations.

    Returns:
        The sum of all the scores in the record.
    """
    record = []  # Initialize an empty list called 'record' to store the scores.  This list will hold the valid scores.

    for op in ops:  # Start a loop that iterates through each operation 'op' in the input list 'ops'.
        if op.isdigit() or (op.startswith('-') and op[1:].isdigit()):
            # Check if the operation 'op' is a digit (or a negative number).
            # op.isdigit() checks if all characters in 'op' are digits.
            # (op.startswith('-') and op[1:].isdigit()) checks if 'op' starts with a '-' and the rest of the characters are digits.
            record.append(int(op))
            # If 'op' is a number, convert it to an integer using int(op) and append it to the 'record' list.
        elif op == "+":
            record.append(record[-1] + record[-2])
            # If the operation 'op' is "+", add the last two numbers in the 'record' list
            # (record[-1] is the last element, record[-2] is the second to last) and append the sum to the 'record' list.
        elif op == "D":
            record.append(record[-1] * 2)
            # If the operation 'op' is "D", double the last number in the 'record' list (record[-1])
            # and append the result to the 'record' list.
        elif op == "C":
            record.pop()
            # If the operation 'op' is "C", remove the last element from the 'record' list using record.pop().
            # This simulates invalidating the previous score.

    return sum(record)  # After processing all operations, calculate the sum of all the numbers in the 'record' list
    # using the sum() function and return the total sum.

if __name__ == "__main__":
    # This block of code is executed only when the script is run directly (not when imported as a module).
    ops_input = input("Enter the list of operations separated by spaces: ")
    # Prompt the user to enter the operations, separated by spaces.  The input is stored as a string in 'ops_input'.
    ops = ops_input.split()
    # Split the input string 'ops_input' into a list of individual operations, using spaces as the delimiter.
    # The resulting list of operations is stored in the 'ops' variable.
    result = calculate_baseball_score(ops)
    # Call the 'calculate_baseball_score' function with the list of operations 'ops' to calculate the total score.
    # The result is stored in the 'result' variable.
    print(f"Total score: {result}")
    # Print the final result (the total score) to the console, using an f-string to embed the value of 'result'.





# feat: Implement baseball score calculator with user input

# This commit implements a Python function, `calculate_baseball_score`, to compute the total score of a modified baseball game.

# Changes:
# - Implemented the `calculate_baseball_score` function.
# - Added user input for the operations list.
# - Included a main execution block.