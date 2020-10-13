import sys

sys.setrecursionlimit(10000)


def single_char_regex(regex, char):
    # . matches any single char
    return True if regex == "" or regex == "." or regex == char else False


def equal_pair_regex(regex, string):
    if len(regex) == 0:
        return True
        # $ matches only in the end of the string
    if len(string) == 0 and regex == "$":
        return True
    if len(string) == 0:
        return False
    if len(regex) >= 2 and regex[1] in "?*+":  # checked twice
        return repetition(regex, string)
    if single_char_regex(regex[0], string[0]) == False:
        return False
    return equal_pair_regex(regex[1:], string[1:])


def repetition(regex, string):
    # ? means that preceding char is repeated zero or one times
    if regex[1] == "?":
        if single_char_regex(regex[0], string[0]):
            return equal_pair_regex(regex[2:], string[1:]) or \
                   equal_pair_regex(regex[2:], string)
        else:
            return equal_pair_regex(regex[2:], string)
            # * means that preceding char is repeated zero or more times
    if regex[1] == "*":
        if single_char_regex(regex[0], string[0]):
            if len(string) == 1:
                return True if len(regex) == 2 else False
            return equal_pair_regex(regex, string[1:]) or \
                   equal_pair_regex(regex[2:], string[1:]) or \
                   equal_pair_regex(regex[2:], string)
        else:
            return equal_pair_regex(regex[2:], string)
            # + means that preceding char is repeated one or more times
    if regex[1] == "+":
        if single_char_regex(regex[0], string[0]):
            if len(string) == 1:
                return True if len(regex) == 2 else False
            if single_char_regex(regex[0], string[1]):
                return equal_pair_regex(regex, string[1:]) or \
                       equal_pair_regex(regex[2:], string[1:])
            else:
                return equal_pair_regex(regex[2:], string[1:])
        else:
            return False


def diff_len_regex(regex, string):
    # ^ matches only in the beginning of the string
    if regex.startswith("^"):
        return equal_pair_regex(regex[1:], string)
    if equal_pair_regex(regex, string):
        return True
    if len(string) == 0:
        return False
    return diff_len_regex(regex, string[1:])


regex, string = input().split("|")
print(diff_len_regex(regex, string))


print(f'Expected: True, returned: {diff_len_regex("colou?r|color")}')
print(f'Expected: True, returned: {diff_len_regex("colou?r|colour")}')
print(f'Expected: False, returned: {diff_len_regex("colou?r|colouur")}')
print(f'Expected: True, returned: {diff_len_regex("colou*r|color")}')
print(f'Expected: True, returned: {diff_len_regex("colou*r|colour")}')
print(f'Expected: True, returned: {diff_len_regex("colou*r|colouur")}')
print(f'Expected: True, returned: {diff_len_regex("col.*r|color")}')
print(f'Expected: True, returned: {diff_len_regex("col.*r|colour")}')
print(f'Expected: True, returned: {diff_len_regex("col.*r|colr")}')
print(f'Expected: True, returned: {diff_len_regex("col.*r|collar")}')
print(f'Expected: False, returned: {diff_len_regex("col.*r$|colors")}')
