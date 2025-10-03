import os

def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Counts how many apples and oranges land on Sam's house.

    Args:
        s: Starting point of Sam's house (inclusive).
        t: Ending point of Sam's house (inclusive).
        a: Location of the Apple tree.
        b: Location of the Orange tree.
        apples: List of distances each apple falls from tree 'a'.
        oranges: List of distances each orange falls from tree 'b'.
    """
    
    # 1. Count Apples that land on the house
    apple_count = 0
    
    # Iterate through the distance each apple was thrown
    for d in apples:
        # Calculate the final landing position: Tree position (a) + distance (d)
        landing_position = a + d
        
        # Check if the landing position is within the house range [s, t]
        if s <= landing_position <= t:
            apple_count += 1
            
    # 2. Count Oranges that land on the house
    orange_count = 0
    
    # Iterate through the distance each orange was thrown
    for d in oranges:
        # Calculate the final landing position: Tree position (b) + distance (d)
        landing_position = b + d
        
        # Check if the landing position is within the house range [s, t]
        if s <= landing_position <= t:
            orange_count += 1
            
    # Print the final counts, each on a new line, as required
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    # Read s and t (house range)
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    # Read a and b (tree locations)
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    # Read m and n (number of apples and oranges - not directly used in the logic)
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0]) # Number of apples
    n = int(third_multiple_input[1]) # Number of oranges

    # Read apple distances
    apples = list(map(int, input().rstrip().split()))

    # Read orange distances
    oranges = list(map(int, input().rstrip().split()))

    # Call the main function to perform the calculation and printing
    countApplesAndOranges(s, t, a, b, apples, oranges)
