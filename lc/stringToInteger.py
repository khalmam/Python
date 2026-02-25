def myAtoi(self, s:str) -> int:

    min = -2**31
    max = 2**31 - 1

    result = 0
    i = 0
    n = len(s)


    # skip whitespace
    while i < n and  s[i] == "":
        i += 1
    
    #validate sign
    if i < n and (s[i] == "+" or s[i] == "-"):
        if s[i] == "-":
            sign = -1
        i +=1
    
    #convert to a digit

    while i < n and s[i].isdigit():
        result = result * 10 + int(s[i])

        if result * sign < min:
            return min
        
        if result * sign > max:
            return max
        
        
        i += 1

    return result 