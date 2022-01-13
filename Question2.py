f = open('front.in', 'r')
contents = f.read()
if len(contents) == 0:
    print("this is an invalid file")
    exit(1)
keywords = ["auto", "break", "elif ch ==", "char", "const", "continue", "default", "do", "double", "else", "enum",
            "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof",
            "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]
usedIdent = []
charClass = 0
# lexeme = [' ']*100
lexeme = []
final = ""
allTokens = []
nextChar = contents[0]
i = 0
lexLen = 0
token = 0
nextToken = 0

EOF = -1
LETTER = 0
DIGIT = 1
SINGLEQUOTE = 2
DOUBLEQUOTE = 3
DECIMAL = 4
UNDERSCORE = 5
UNKNOWN = 99

# /* Token codes */
FLOAT_LIT = 9
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
DECIMAL_POINT = 27
EXCLAMATION = 28
NUMSIGN = 29
FOR_CODE = 30
IF_CODE = 31
ELSE_CODE = 32
WHILE_CODE = 33
DO_CODE = 34
INT_CODE = 35
FLOAT_CODE = 36
SWITCH_CODE = 37
VERT_BAR = 39
BACK_SLASH = 40
APOSTRO = 41
OPEN_BRACKET = 43
CLOSE_BRACKET = 44
QMARK = 45
LEFT_BRACE = 46
RIGHT_BRACE = 47
COLON = 48
QUOTATION_MARK = 49
SEMICOLON = 50
LEFT_BRACKET = 51
RIGHT_BRACKET = 52
DOLLSIGN = 53
PERCENT = 54
CARET = 55
AMPSAND = 56
ASTERICK = 57
COMMA = 58
TILDE = 59


# def addChar():
#   if lexLen <= 98:
#     lexeme[lexLen+1] = nextChar
#     lexeme[lexLen] = '\0'
#   else:
#     print("Error - lexeme is too long \n")
def addChar():
    if lexLen <= 98:
        lexeme.append(nextChar)
    else:
        print("Error - lexeme is too long \n")


def getChar(file):
    global i
    global nextChar
    global charClass
    if i < len(file):
        nextChar = file[i]
        if nextChar.isalpha():
            charClass = LETTER
        elif nextChar.isdigit():
            charClass = DIGIT
        elif nextChar == '_':
            charClass = UNDERSCORE
        else:
            charClass = UNKNOWN
    else:
        charClass = "EOF"
    i += 1


def getNonBlank(file):
    global nextChar
    while nextChar.isspace():
        getChar(file)


def lookup(ch):
    global nextToken
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    elif ch == '~':
        addChar()
        nextToken = TILDE
    elif ch == '#':
        addChar()
        nextToken = NUMSIGN
    elif ch == '!':
        addChar()
        nextToken = EXCLAMATION
    elif ch == '$':
        addChar()
        nextToken = DOLLSIGN
    elif ch == '^':
        addChar()
        nextToken = CARET
    elif ch == '&':
        addChar()
        nextToken = AMPSAND
    elif ch == '_':
        addChar()
        nextToken = UNDERSCORE
    elif ch == ',':
        addChar()
        nextToken = COMMA
    elif ch == '|':
        addChar()
        nextToken = VERT_BAR
    elif ch == '\\':
        addChar()
        nextToken = BACK_SLASH
    elif ch == '`':
        addChar()
        nextToken = APOSTRO
    elif ch == '<':
        addChar()
        nextToken = OPEN_BRACKET
    elif ch == '>':
        addChar()
        nextToken = CLOSE_BRACKET
    elif ch == '?':
        addChar()
        nextToken = QMARK
    elif ch == '{':
        addChar()
        nextToken = LEFT_BRACE
    elif ch == '}':
        addChar()
        nextToken = RIGHT_BRACE
    elif ch == '[':
        addChar()
        nextToken = LEFT_BRACKET
    elif ch == ']':
        addChar()
        nextToken = RIGHT_BRACKET
    elif ch == ':':
        addChar()
        nextToken = COLON
    elif ch == '"':
        addChar()
        nextToken = QUOTATION_MARK
    elif ch == '':
        addChar()
        nextToken = SEMICOLON
    else:
        addChar()
        nextToken = "EOF"
    return nextToken


def reserve(word):
    if word == "for":
        nextToken = FOR_CODE
    elif word == "if":
        nextToken = IF_CODE
    elif word == "else":
        nextToken = ELSE_CODE
    elif word == "while":
        nextToken = WHILE_CODE
    elif word == "do":
        nextToken = DO_CODE
    elif word == "int":
        nextToken = INT_CODE
    elif word == "float":
        nextToken = FLOAT_CODE
    elif word == "switch":
        nextToken = SWITCH_CODE
    else:
        nextToken = IDENT
    return nextToken


def lex(file):
    global lexLen
    global charClass
    global nextToken
    getNonBlank(file)
    lexLen = 0
    if charClass == LETTER:
        addChar()
        getChar(contents)
        while charClass == LETTER or charClass == DIGIT or charClass == UNDERSCORE:
            addChar()
            getChar(contents)
        nextToken = IDENT
    elif charClass == UNDERSCORE:
        addChar()
        getChar(contents)
        while charClass == LETTER or charClass == DIGIT or charClass == UNDERSCORE:
            addChar()
            getChar(contents)
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar(contents)
        while charClass == DIGIT:
            addChar()
            getChar(contents)
            if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                addChar()
                getChar(contents)
                nextToken = FLOAT_LIT
            if nextChar == 'E' or nextChar == 'e':
                addChar()
                getChar(contents)
                if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                    addChar()
                    getChar(contents)
                    nextToken = FLOAT_LIT
                if nextChar == '-':
                    addChar()
                    getChar(contents)
                    while charClass == DIGIT:
                        addChar()
                        getChar(contents)
                        if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                            addChar()
                            getChar(contents)
                            nextToken = FLOAT_LIT
                    nextToken = FLOAT_LIT
                elif charClass == DIGIT:
                    while charClass == DIGIT:
                        addChar()
                        getChar(contents)
                        if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                            addChar()
                            getChar(contents)
                            nextToken = FLOAT_LIT
                        nextToken = FLOAT_LIT
            if charClass == UNKNOWN and nextChar == '.':
                addChar()
                getChar(contents)
                while charClass == DIGIT:
                    addChar()
                    getChar(contents)
                    if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                        addChar()
                        getChar(contents)
                        nextToken = FLOAT_LIT
                    if nextChar == 'E' or nextChar == 'e':
                        addChar()
                        getChar(contents)
                        if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                            addChar()
                            getChar(contents)
                            nextToken = FLOAT_LIT
                        if nextChar == '-':
                            addChar()
                            getChar(contents)
                            while charClass == DIGIT:
                                addChar()
                                getChar(contents)
                                if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                                    addChar()
                                    getChar(contents)
                                    nextToken = FLOAT_LIT
                            nextToken = FLOAT_LIT
                        elif charClass == DIGIT:
                            while charClass == DIGIT:
                                addChar()
                                getChar(contents)
                                if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                                    addChar()
                                    getChar(contents)
                                    nextToken = FLOAT_LIT
                            nextToken = FLOAT_LIT
                nextToken = FLOAT_LIT
            else:
                nextToken = INT_LIT
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        if nextChar == '.':
            addChar()
            getChar(contents)
            if charClass == DIGIT:
                addChar()
                getChar(contents)
                while charClass == DIGIT:
                    addChar()
                    getChar(contents)
                    if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                        addChar()
                        getChar(contents)
                        nextToken = FLOAT_LIT
                    if nextChar == 'E' or nextChar == 'e':
                        addChar()
                        getChar(contents)
                        if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                            addChar()
                            getChar(contents)
                            nextToken = FLOAT_LIT
                        if nextChar == '-':
                            addChar()
                            getChar(contents)
                            while charClass == DIGIT:
                                addChar()
                                getChar(contents)
                                if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                                    addChar()
                                    getChar(contents)
                                    nextToken = FLOAT_LIT
                            nextToken = FLOAT_LIT
                        elif charClass == DIGIT:
                            while charClass == DIGIT:
                                addChar()
                                getChar(contents)
                                if nextChar == 'f' or nextChar == 'F' or nextChar == 'l' or nextChar == 'L':
                                    addChar()
                                    getChar(contents)
                                    nextToken = FLOAT_LIT
                            nextToken = FLOAT_LIT
                    nextToken = FLOAT_LIT
            else:
                nextToken = DECIMAL_POINT
        else:
            lookup(nextChar)
            getChar(contents)
    elif charClass == "EOF":
        nextToken = EOF
        lexeme.append('E')
        lexeme.append('O')
        lexeme.append('F')

    # for i in range(len(usedIdent)):
    #   if usedIdent[i] == lexeme:
    #     print(lexeme, " has already been used")
    #     return nextToken
    final = ''.join(lexeme)
    if nextToken == IDENT:
        nextToken = reserve(final)
    lexeme.clear()
    print("Next Token is", nextToken, "Next lexeme is", final)
    allTokens.append(nextToken)
    # return nextToken


def getNext(tokens):
    global j
    global curr
    j += 1
    if j < len(allTokens):
        curr = allTokens[j]
        print(curr)
    else:
        error()


def expr(tokens):
    global j
    global curr
    term(tokens)
    while curr == ADD_OP or curr == SUB_OP:
        getNext(allTokens)
        term(tokens)


def error():
    print("this is an invalid mathematical operation")
    exit()


def term(tokens):
    global j
    global curr
    factor(tokens)
    while curr == MULT_OP or curr == DIV_OP:
        getNext(allTokens)
        factor(tokens)


def factor(tokens):
    global j
    global curr
    if curr == IDENT or curr == INT_LIT or curr == FLOAT_LIT:
        getNext(allTokens)
    elif curr == LEFT_PAREN:
        getNext(allTokens)
        expr(tokens)
        if curr == RIGHT_PAREN:
            getNext(allTokens)
        else:
            error()
    else:
        error()
        print("Exit <factor>\n")


getChar(contents)
while nextToken != EOF:
    lex(contents)
j = 0
curr = allTokens[j]
expr(allTokens)
print("this is a valid mathematical operation")
