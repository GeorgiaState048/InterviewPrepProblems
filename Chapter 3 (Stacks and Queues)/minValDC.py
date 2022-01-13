import math

maxVal = 0
minVal = 9999999


def minMax(array, start, end):
    global maxVal
    global minVal
    mid = math.floor((start + end) / 2)
    if end - start > 2:
        minMax(array, start, mid)
        minMax(array, mid, end)
    else:
        array = array[start:end]
        if end - start == 1:
            array.append(array[0])
        else:
            maxVal = max(maxVal, max(array[0], array[1]))
            minVal = min(minVal, min(array[0], array[1]))


nums = [4, 2, 5, 6, 78, 3, 5, 7, 0, 3]
minMax(nums, 0, len(nums) - 1)

print(minVal)
print(maxVal)
