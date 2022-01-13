#  see which version is higher.
#  1.0.1 is lower than 1.3

def checkVersion(a, b):
    numA = a.split('.')
    numB = b.split('.')
    if len(numA) > len(numB):
        diff = len(numA) - len(numB)
        numB += ['0']*diff
    elif len(numB) > len(numA):
        diff = len(numB) - len(numA)
        numA += ['0']*diff

    numA = ''.join(numA)
    numB = ''.join(numB)

    if int(numA) > int(numB):
        return a
    elif int(numB) > int(numA):
        return b
    else:
        return 1


print(checkVersion("1.0.1", "1.3"))