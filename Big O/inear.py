def(arr,x):
    n = len(arr)

    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1

    if __name__ = "__main__":

        arr = [10.20,30,40,80]
        x = 30

        result = search(arr,x)

        if result == -1:
            print("Element not found in array")
        else:
            print("Element found at index", str(result))