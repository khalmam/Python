# Step 1: Read number of elements
n = int(input())

# Step 2: Read set elements
s = set(map(int, input().split()))

# Step 3: Read number of commands
num_commands = int(input())

# Step 4: Execute commands
for _ in range(num_commands):
    command = input().split()
    cmd = command[0]
    
    if cmd == "pop":
        s.pop()
    elif cmd == "remove":
        s.remove(int(command[1]))
    elif cmd == "discard":
        s.discard(int(command[1]))

# Step 5: Print the sum of remaining elements
print(sum(s))
