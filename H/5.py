# Given the participants score sheet for your University Sports Day,
# you are required to find the runner-up score. 
# You are given  scores. 
# Store them in a list and find the score of the runner-up.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = sorted(list(set(arr)), reverse=True)
    if len(unique_scores) >= 2:
        print(unique_scores[1])
    else:
        len(unique_scores) == 1
        print(unique_scores[0])