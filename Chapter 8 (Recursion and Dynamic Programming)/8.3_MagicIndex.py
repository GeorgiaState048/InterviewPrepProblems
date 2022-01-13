import math


def magicIndex(nums):
    if not nums:
        return -1
    else:
        return findIndex(nums, 0, len(nums) - 1)


def findIndex(nums, start, end):
    if end < start:
        return -1

    mid = math.floor((end + start) / 2)
    if nums[mid] == mid:
        return mid
    if nums[mid] > mid:
        return findIndex(nums, start, mid - 1)
    if nums[mid] < mid:
        return findIndex(nums, mid + 1, end)


nums = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(magicIndex(nums))
