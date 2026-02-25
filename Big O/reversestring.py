def reverse(s:list[str])-> None:
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]

        i += 1
        j -= 1
   
   def reverse(s):
    i = 0
    j = lens(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]

        i+ = 1 
        j -= 1
        