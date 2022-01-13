def checkHeight(root):
    if not root:
        return -1
    leftHeight = checkHeight(root.left)
    rightHeight = checkHeight(root.left)

    if leftHeight == -999999:
        return -999999
    if rightHeight == -999999:
        return -999999

    heightDiff = leftHeight - rightHeight
    if abs(heightDiff) > 1:
        return -999999
    else:
        return max(rightHeight, leftHeight) + 1
