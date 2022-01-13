def cleanString(word):
    newWord = ""
    word = word.lower()
    for i in word:
        if i.isalnum():
            newWord += i
    return newWord


def palindromePermutation(word):
    #newWord = cleanString(word)
    unpaired = set()
    for i in word:
        if ord(i) in unpaired: #can use ascii value or just char by itself. Use ascii value if case matters
            unpaired.remove(ord(i))
        else:
            unpaired.add(ord(i))
    if len(unpaired) > 1:
        return False
    else:
        return True


print(palindromePermutation("taCocat"))

