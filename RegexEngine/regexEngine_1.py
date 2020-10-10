
def regexEngine(input_string):
    slist = input_string.split("|")
    regex = slist[0]
    string_ = slist[1]

    result = False
    if regex == '':
        result = True
    elif string_ == '':
        result = False
    elif regex == '.':
        result = True
    elif regex == string_:
        result = True
    else:
        result = False

    print(result)

print(f'expected: False, given:{regexEngine("c|a")}')
print(f'expected: True, given:{regexEngine("c|c")}')
print(f'expected: True, given:{regexEngine("a|a")}')
print(f'expected: True, given:{regexEngine(".|a")}')
print(f'expected: True, given:{regexEngine("|a")}')
print(f'expected: True, given:{regexEngine("|")}')
print(f'expected: False, given:{regexEngine("a|")}')
