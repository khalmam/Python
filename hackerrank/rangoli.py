import string

def print_rangoli(size):
    # 1. Prepare the alphabet list and determine the character set
    # The size determines the range of letters, e.g., size 3 uses 'a', 'b', 'c'
    # string.ascii_lowercase[size-1::-1] gives the letters in reverse: 'c', 'b', 'a' for size 3
    alpha = string.ascii_lowercase
    letters = alpha[:size] # e.g., 'abc' for size 3
    
    # 2. Determine the maximum width of the rangoli
    # The widest line is: (N-th letter) - (a) - (N-th letter)
    # The length of the widest line is: 2 * (size of the widest part) - 1
    # Widest part for size N is N letters long, and each letter is separated by a hyphen (-).
    # Part width = (2 * size - 1) * 2 - 1 = 4 * size - 3
    max_width = (size * 2 - 1) + (size * 2 - 2)
    # A simpler way to calculate: widest line is formed by N letters and N-1 separators on each side
    # (N * 2 - 1) letters, and (N * 2 - 2) hyphens -> N*4 - 3 total characters
    
    # The widest line has size letters on the left (e.g., c-b-a), size-1 separators, 
    # and size-1 letters on the right (e.g., b-c), size-1 separators.
    # Total chars = 2 * (size-1) + 1 letters + 2 * (size-1) separators = 4 * size - 3
    max_width = 4 * size - 3
    
    lines = []
    
    # 3. Generate the lines (Top half and center line)
    # i goes from 0 to size - 1 (e.g., 0, 1, 2 for size 3)
    for i in range(size):
        # Current letters for the line, from the N-th letter down to the (N-i)-th letter
        current_alpha = letters[:size-i] # e.g., size 3: i=0 -> 'abc', i=1 -> 'ab', i=2 -> 'a'
        
        # Build the left side in reverse (e.g., 'c', 'b', 'a')
        left_side = "-".join(current_alpha[::-1]) # e.g., 'c-b-a'
        
        # Build the right side (e.g., 'b-c')
        # We exclude the 'a' at the end of the left side (index 1 to the end)
        right_side = "-".join(current_alpha[::-1][1:]) # e.g., 'b-c'
        
        # Full center part of the line (e.g., 'c-b-a-b-c')
        line_content = f"{left_side}-{right_side}"
        
        # Special handling for the center line, where right_side is an empty string
        if not right_side:
            line_content = left_side # 'a'
        
        # Center and pad the line with hyphens based on the max_width
        formatted_line = line_content.center(max_width, '-')
        lines.append(formatted_line)
        
    # 4. Combine and Print
    # The entire rangoli is the top half, plus the reverse of the top half (excluding the center line)
    result = "\n".join(lines + lines[:-1][::-1])
    
    # The function is expected to print the result, but since the required return type is a string, 
    # we return the combined string. The prompt states "print the capitalized string, s", 
    # but based on the overall context, the requirement is to print the rangoli.
    # Since the sample output shows a large string, returning the final string is appropriate.
    print(result)
    # If the testing environment expects a returned string:
    # return result

# Example usage (as if run in the environment):
# size = int(input())
# print_rangoli(size)

# For your reference (Sample Input 5):
# print_rangoli(5)