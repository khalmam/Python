# 🧠 Problem Statement
# You're given:

# An array of integers: arr

# Two disjoint sets:

# Set A → you like the elements in this set

# Set B → you dislike the elements in this set

# For each element x in arr:

# If x is in A: happiness += 1

# If x is in B: happiness -= 1

# If x is in neither: happiness += 0 (no change)

# Initial happiness is 0.

# You must output the final happiness value.


# Input
n, m = map(int, input().split())  # n = size of array, m = size of sets A and B
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Calculate happiness
happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

# Output the result
print(happiness)
