#  Step-by-step Breakdown
# 📥 Input
# First line: an integer n — number of elements in the tuple.

# Second line: n space-separated integers.

# 🧮 Output
# Print the result of hash(t) where t is the tuple of integers.

n = int(input())                  # Read number of elements
integer_list = map(int, input().split())  # Read integers and convert to int
t = tuple(integer_list)          # Create a tuple
print(hash(t))                   # Print the hash of the tuple
