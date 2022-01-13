import math


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None
    else:
        return createBST(nums, 0, len(nums) - 1)


def createBST(nums, start, end):
    if start > end:
        return None
    else:
        mid = math.floor(len(nums) / 2)
        root = TreeNode(nums[mid])
        root.left = createBST(nums, start, mid - 1)
        root.right = createBST(nums, mid + 1, end)
    return root
