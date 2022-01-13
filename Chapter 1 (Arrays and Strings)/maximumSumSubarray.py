"""return range of numbers that gives the graetest sum"""
# [-2,1,-3,4,-1,2,1,-5,4]
"""Just use max sum subarray but every time a max sum stays as curSum, add to the set"""


def maxSubArray(nums):
    maxSum = nums[0]
    curSum = maxSum
    start = 0
    end = 0
    currStart = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i] + curSum:
            currStart = i
            curSum = nums[i]
        else:
            curSum = nums[i] + curSum
        if curSum > maxSum:
            end = i
            start = currStart
            maxSum = curSum
    return nums[start:end + 1]


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
