def binarysearch(array, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarysearch(array, x, low, mid - 1)
        else:
            return binarysearch(array, x, mid + 1, high)

    else:
        return - 1


array = [1, 4, 5, 6, 7, 8, 9]
x = 9

result = binarysearch(array, x, 0, len(array) - 1)

if result >= 0:
    print(str(result))
else:
    print("ERROR")


