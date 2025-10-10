import math
import os

def getTotalX(a, b):
    """
    Determines the number of integers that are between two sets (arrays).

    This solution uses the mathematical concepts of LCM (Least Common Multiple) 
    and GCD (Greatest Common Divisor) to efficiently narrow the search space.

    Args:
        a: The first array (integers must be multiples of all elements in 'a').
        b: The second array (integers must be factors of all elements in 'b').

    Returns:
        The count of integers satisfying both conditions.
    """
    
    # 1. Helper function for LCM (Least Common Multiple) of two numbers
    # LCM(x, y) = (|x * y|) / GCD(x, y)
    def lcm(x, y):
        return x * y // math.gcd(x, y)
    
    # --- Step 1: Calculate LCM of Array 'a' ---
    # The smallest number that every element in 'a' divides is LCM(a).
    lcm_a = a[0]
    for i in a[1:]:
        lcm_a = lcm(lcm_a, i)
    
    # --- Step 2: Calculate GCD of Array 'b' ---
    # The largest number that divides every element in 'b' is GCD(b).
    gcd_b = b[0]
    for j in b[1:]:
        gcd_b = math.gcd(gcd_b, j)
    
    # --- Step 3: Count Multiples of LCM(a) that divide GCD(b) ---
    count = 0
    multiple = lcm_a # Start checking from the LCM itself
    
    # Iterate through every multiple of LCM(a) up to GCD(b).
    # We can skip checking all numbers and just check the multiples.
    while multiple <= gcd_b:
        
        # Condition 2: Check if the candidate number (which is already a multiple of all of 'a') 
        # is also a factor of all of 'b' (by checking if it divides GCD(b)).
        if gcd_b % multiple == 0:
            count += 1
            
        # Move to the next multiple of lcm_a (this is the most efficient part)
        multiple += lcm_a
        
    return count


if __name__ == '__main__':
    # Standard setup for reading input
    try:
        n, m = map(int, input().rstrip().split())
        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
    except Exception:
        # Handle case where input might be missing or malformed
        # Using placeholder values for demonstration if input fails
        n, m = 2, 3
        a = [2, 4]
        b = [16, 32, 96]


    totalX = getTotalX(a, b)
    print(totalX)
