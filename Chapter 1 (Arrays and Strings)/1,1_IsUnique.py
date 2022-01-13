"""string = "jonathan"
print(ord('j'))"""


def isUnique(word):
    charSet = [False] * 128
    for i in range(len(word)):
        val = ord(word[i])
        if charSet[val] is True:
            return False
        else:
            charSet[val] = True
    return True


print(isUnique("jonhk"))
