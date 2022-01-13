# a2z2b4 translates to aaazzzbbbbb

def translate(string):
    newString = ""
    hold = []
    for i in range(0, len(string), 2):
        hold = [string[i]] * (int(string[i + 1]) + 1)
        newString += ''.join(hold)
    return newString


print(translate("a2z2b4c3"))
