def validateBST(root):
    return checkBST(root, None, None)


def checkBST(root, min_val, max_val):
    if not root:
        return True

    if max_val and root.val > max_val or min_val and root.val <= min_val:
        return False

    if not checkBST(root, min_val, root.val) or not checkBST(root, root.val, max_val):
        return False
    return True
