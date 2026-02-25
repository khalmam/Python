def twosums(num,target):
    seen = {}
    for i, n in enumerate(num):
        complement = target - n
        if complement in seen:
            return (seen[complement], i)
        seen[n] = i
    return None



def twosums(num, target):
    seen = { }
    for i, n in enumerate(num):
        complement = target - n
        if complement in seen:
            return([seen[complement], i])
        seen[n] = i
    return None


    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] == num[j]:
                return [i, j]
        
    return None