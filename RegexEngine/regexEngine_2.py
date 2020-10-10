def regex_engine(input_string) -> bool:
    slist = input_string.split("|")
    regex = slist[0]
    string_ = slist[1]
    result = None

    if len(regex) == 0:
        result = True
    else:
        if len(string_) == 0:
            result = False
        else:
            if regex[0] == '.' or (regex[0] == string_[0]):
                result = regex_engine(regex[1:] + "|" + string_[1:])
            else:
                result = False

    return result

in_string = input()
print(regex_engine(in_string))
