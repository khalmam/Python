def solution(numbers):
    result = []
    for i in range(len(numbers) -2):
        a,b,c = numbers[i], numbers[i - 1], numbers[i -2]
        if a<b>c or a >b < c:
            result.appen(1)
        else:
            result.append(0)
    return result