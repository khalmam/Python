#  Problem Summary
# You're given a string of digits (e.g., "1222311"). 
# Consecutive repeating characters need to be replaced by a tuple showing the count 
# and the character, like:

# python
# Copy
# Edit
# Input:  "1222311"
# Output: (1, 1) (3, 2) (1, 3) (2, 1)
# 💡 Why use groupby()?
# groupby() groups consecutive identical elements together, which is perfect for this task.




from itertools import groupby

s = input()

for key, group in groupby(s):
    count = len(list(group))
    print((count, int(key)), end=' ')
