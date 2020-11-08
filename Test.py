line = 'a aa abC aa ac abc bcd a'
l_line = line.split()
l_line = [el.lower() for el in l_line]
d_dict = {word.lower(): l_line.count(word.lower()) for word in l_line}

for key, value in d_dict.items():
    print(f'{key} {value}')
