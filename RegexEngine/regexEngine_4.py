import sys

sys.setrecursionlimit(10000)


def regex_engine(regex_p, string_p) -> bool:

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


def check_meta(regex, string_):
    reg_beg = '^' in regex
    reg_end = '$' in regex
    i = 0
    result = False

    if reg_beg and reg_end:
        # return regex[1:-1] == string_
        if len(regex[1:-1]) == len(string_):
            return regex_engine(regex[1:-1], string_)
        else:
            return False
    elif reg_beg:
        # return regex[1:] == string_[:(len(regex[1:]))]
        return regex_engine(regex[1:], string_[:(len(regex[1:]))])

    elif reg_end:
        # return regex[:-1] == string_[-(len(regex[:-1])):]
        return regex_engine(regex[:-1], string_[-(len(regex[:-1])):])


def entry_point(input_string):
    slist = input_string.split("|")
    regex = slist[0]
    string_ = slist[1]
    result_e = False
    has_meta = False
    meta_chars = '^$'

    for c in regex:
        for mc in meta_chars:
            if c == mc:
                has_meta = True

    if regex == '':
        result_e = True
    elif string_ == '':
        result_e = False
    elif has_meta:
        result_e = check_meta(regex, string_)
    else:
        i = 0
        while (result_e == False) and (len(string_[i:i + len(regex)]) != 0):
            result_e = regex_engine(regex, string_[i:i + len(regex)])
            i += 1
    return result_e


# in_string = input()
# print(entry_point(in_string))

print(f'Expected: True, returned: {entry_point("app|apple")}')
print(f'Expected: True, returned: {entry_point("le$|apple")}')
print(f'Expected: True, returned: {entry_point("^a|apple")}')
print(f'Expected: True, returned: {entry_point(".$|apple")}')
print(f'Expected: True, returned: {entry_point("apple$|tasty apple")}')
print(f'Expected: True, returned: {entry_point("^apple|apple pie")}')
print(f'Expected: True, returned: {entry_point("^apple$|apple")}')
print(f'Expected: False, returned: {entry_point("^apple$|tasty apple")}')
print(f'Expected: False, returned: {entry_point("^apple$|apple pie")}')
print(f'Expected: False, returned: {entry_point("^app$|apple")}')
print(f'Expected: False, returned: {entry_point("^le|apple")}')
