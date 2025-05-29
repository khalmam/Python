# Problem Summary:
# You are given n words (some may repeat).

# For each unique word, count how many times it occurs.

# Print two things:

# The number of unique words.

# The count of each word in the order it first appeared.


from collections import OrderedDict

n = int(input())
word_count = OrderedDict()

for _ in range(n):
    word = input().strip()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print number of unique words
print(len(word_count))

# Print counts in order of first appearance
print(' '.join(map(str, word_count.values())))
