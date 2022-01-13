def getPerms(remainder):
    length = len(remainder)
    result = []
    if length == 0:
        result.append("")
        return result

    for i in range(length):
        before = remainder[0:i]
        after = remainder[i + 1:length]
        partial = getPerms(before + after)

        for s in partial:
            result.append(remainder[i] + s)

    return result


test = [1, 3, 4]
empty = []
empty.append(test + [1, 2, 3])
print(empty)
