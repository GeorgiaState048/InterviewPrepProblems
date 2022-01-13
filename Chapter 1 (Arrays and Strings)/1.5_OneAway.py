def oneAway(a, b):
    if len(a) == len(b):
        return checkRepl(a, b)
    elif len(a) > len(b):
        return checkDel(a, b)
    else:
        return checkDel(b, a)


def checkRepl(a, b):
    foundDiff = None
    for i in range(len(a)):
        if a[i] != b[i]:
            if foundDiff:
                foundDiff = False
            else:
                foundDiff = True
    return foundDiff

def checkDel(a, b):
    if len(a) - len(b) > 1:
        return False
    b_pointer = 0
    a_pointer = 0
    while b_pointer < len(b):
        if b[b_pointer] == a[a_pointer]:
            a_pointer += 1
            b_pointer += 1
        else:
            a_pointer += 1
            if b[b_pointer] == a[a_pointer]:
                b_pointer += 1
                a_pointer += 1
            else:
                return False
    return True

def checkDel(a, b):
    if len(a) - len(b) > 1:
        return False
    b_pointer = 0
    a_pointer = 0
    while b_pointer < len(b):
        if b[b_pointer] == a[a_pointer]:
            a_pointer += 1
            b_pointer += 1
        else:
            a_pointer += 1
            if b[b_pointer] == a[a_pointer]:
                b_pointer += 1
                a_pointer += 1
            else:
                return False
    return True


print(oneAway("four", "fourts"))
