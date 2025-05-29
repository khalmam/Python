# Problem Summary
# You're given:

# A number N representing the number of commands to run.

# N lines, each containing one of these commands:

# Command	Description
# insert i e	Insert e at index i
# print	Print the current list
# remove e	Remove first occurrence of e
# append e	Add e to the end
# sort	Sort the list in ascending order
# pop	Remove last element
# reverse	Reverse the list

# Your task is to:

# Initialize an empty list, and

# Execute all the commands in the given order.


N = int(input())  # Number of commands
lst = []  # Start with an empty list

for _ in range(N):
    command = input().split()  # Split command into parts
    action = command[0]        # First word is the action
    
    if action == 'insert':
        i = int(command[1])
        e = int(command[2])
        lst.insert(i, e)
    elif action == 'print':
        print(lst)
    elif action == 'remove':
        e = int(command[1])
        lst.remove(e)
    elif action == 'append':
        e = int(command[1])
        lst.append(e)
    elif action == 'sort':
        lst.sort()
    elif action == 'pop':
        lst.pop()
    elif action == 'reverse':
        lst.reverse()

