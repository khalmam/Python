# Enter your code here. Read input from STDIN. Print output to STDOUT

#finite number of guests visited an infinite hotel
#Guests: Captain and families consisting of K numbers where K !=1
#0(n**2)
# K = int(input())
# rooms = list(map(int, input().split()))

# for room in set(rooms):
#     if rooms.count(room)==1:
#         print(room)
#         break

K = int(input())
rooms = list(map(int,input().split()))

urooms = set(rooms)

captain = (sum(urooms)* K - sum(rooms)) // (K-1)

print(captain)