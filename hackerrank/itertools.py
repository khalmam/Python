#permutations

from itertools import permutations
s,n = input().split()
for p in permutations(sorted(s),int(n)):
    print(''.join(p))# <!-- You are given two sets, A and  B.
    # Your job is to find whether set A is a subset of set B. -->