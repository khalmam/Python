# The last question you provided is a programming task that asks you to write a function to display the same number in four different numerical bases—Decimal, Octal, Hexadecimal, and Binary—for a range of integers.

# 🎯 Task Breakdown
# Your goal is to write a function, print_formatted(number), that iterates through every integer i from 1 up to and including the input number (N).

# For each integer i, you must print four values on a single line:

# Decimal (Base 10)

# Octal (Base 8)

# Hexadecimal (Base 16, using capital letters)

# Binary (Base 2)

# 📏 The Key Challenge: Formatting and Alignment
# The hardest part of the question is the specific formatting requirement:

# Determine Width: You must first find the maximum width needed for padding. This width is defined by the length of the Binary representation of the largest number, N (the input number).

# Padding and Alignment: Every single output value (Decimal, Octal, Hex, and Binary for every number from 1 to N) must be right-justified and padded with spaces to match that maximum width.

# Separation: The four padded values on each line must be separated by a single space.

# Example (If N=17)

# Binary for 17 is 10001, which has a length of 5. The required padding width is 5.

# For the number 10, the output would look like this (where _ represents a space):

# Decimal (10): ___10 (Padded to width 5)

# Octal (12): ___12 (Padded to width 5)

# Hex (A): ____A (Padded to width 5)

# Binary (1010): _1010 (Padded to width 5)

# The final line printed for i=10 would be: 10 12 A 1010 (Note: Hexadecimal must be capitalized 'A').



def print_formatted(number):
    """
    Prints the Decimal, Octal, Hexadecimal, and Binary representations 
    for each integer from 1 to 'number', right-aligned to the width 
    of the binary representation of 'number'.
    """
    
    # 1. Determine the maximum width for padding
    # len(bin(number)[2:]) gives the length of the binary string without the '0b' prefix.
    width = len(bin(number)[2:])

    # 2. Loop through each integer from 1 to N (inclusive)
    for i in range(1, number + 1):
        
        # Get the string representations, removing prefixes where necessary
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        # 3. Print the formatted line
        # Use str.rjust(width) to right-justify and space-pad each value.
        print(
            decimal.rjust(width) + " " +
            octal.rjust(width) + " " +
            hexadecimal.rjust(width) + " " +
            binary.rjust(width)
        )

if __name__ == '__main__':
    # Reads the single integer N from the input
    try:
        n = int(input())
        print_formatted(n)
    except EOFError:
        # Gracefully handle end-of-file for automated testing environments
        pass
    except ValueError:
        # Handle case where input is not a valid integer
        print("Invalid input. Please enter a positive integer.")