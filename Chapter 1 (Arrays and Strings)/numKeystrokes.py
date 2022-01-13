"""number of total keystrokes to make a word
orange = 6
Orange = 7 (caps)
ORANGE = 7 (caps)
ORAnGE = 8 (caps then shift n)
Orange* = 9 (shift 8)"""


def keystrokes(word):
    count = 0
    isCaps = None
    for i in range(len(word)):
        print(count)
        if word[i].islower():
            if i - 1 >= 0 and word[i - 1].isupper():
                count += 2
            else:
                count += 1
        elif word[i].isupper():
            if i - 1 >= 0 and word[i - 1].isupper() and isCaps:
                count += 1
            elif isCaps:
                count += 1
            else:
                count += 2
                isCaps = True
        elif not word[i].isalnum():
            count += 2
    return count


print(keystrokes("Orange*"))
