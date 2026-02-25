    # <!-- You are given two sets, A and  B.
    # Your job is to find whether set A is a subset of set B. -->

T= int(input())

for _ in range(T):
    n = int(input())
    A = set(map(int, input().split()))
    
    m = int(input())
    B = set(map(int, input().split()))
    
    print(A.issubset(B))