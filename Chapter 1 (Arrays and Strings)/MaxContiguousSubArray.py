"""Given an integer array nums and two integers left and right
   return the number of contiguous non-empty subarrays such that
   the value of the maximum array element in that sub array is in
   the range [left, right]"""
from collections import deque

"""Approach 1:
        use sliding window approach. Create two pointers that start on first value, one pointer will expand the
        window, one pointer will go through each element sequentially. create a set that holds the current window, 
        if you come across a value that is between the range and is the max of the current window, increment count, 
        and incrememnt the b pointer. the a pointer will increase when b pointer reaches the end or the b pointer 
        reaches a value that is greater than the range"""


def getNumSubArrays(nums, left, right):
    start = 0
    end = 0
    subArrays = deque()
    count = 0
    while end < len(nums):
        if nums[end] not in subArrays:
            subArrays.append(nums[end])
        print(subArrays)
        if right >= max(subArrays) >= left:
            count += 1
            end += 1
        else:
            subArrays.popleft()
            start += 1
        if start == end:
            subArrays.popleft()
            end += 1
    return count


test = set()
test.add(2)
test.add(1)
test.add(4)
test.add(3)
print(getNumSubArrays([2, 1, 4, 3], 2, 3))
