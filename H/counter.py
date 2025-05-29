# You are given a lowercase string (company name). You need to:

# Find the top three most common characters.

# Print each character along with its occurrence count.

# Sort by:

# Highest count first

# If counts are equal, then alphabetically

from collections import Counter

if __name__ == '__main__':
    s = input()
    
    # Count character frequencies
    counter = Counter(s)
    
    # Sort by: (-count, character)
    sorted_chars = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    
    # Print top 3
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")
