import sys

sys.setrecursionlimit(100)


def regex_engine(regex_p, string_p) -> bool:
    result = None

    if len(regex_p) == 0:
        result = True
    else:
        if len(string_p) == 0:
            result = False
        else:
            if regex_p[0] == '.' or (regex_p[0] == string_p[0]):
                result = regex_engine(regex_p[1:], string_p[1:])
            else:
                result = False
    return result


def entry_point(input_string):
    slist = input_string.split("|")
    regex = slist[0]
    string_ = slist[1]
    result_e = False
    if regex == '':
        result_e = True
    elif string_ == '':
        result_e = False
    else:
        i = 0
        while (result_e == False) and (len(string_[i:i + len(regex)]) != 0):
            result_e = regex_engine(regex, string_[i:i + len(regex)])
            i += 1
    return result_e


# in_string = input()
# print(entry_point(in_string))

print(f'Expected: True, returned: {entry_point("apple|apple")}')
print(f'Expected: True, returned: {entry_point("ap|apple")}')
print(f'Expected: True, returned: {entry_point("le|apple")}')
print(f'Expected: True, returned: {entry_point("a|apple")}')
print(f'Expected: True, returned: {entry_point(".|apple")}')
print(f'Expected: False, returned: {entry_point("apwle|apple")}')
print(f'Expected: False, returned: {entry_point("peach|apple")}')
