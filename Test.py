text = 'Raz dwa Trzy CzterY'
words = text.split()
result = ''
i = 1
for word in words:
    print(i)
    print(word)
    if i == 1:
        words[i-1] = word.lower()
    else:
        words[i-1] = word.title()
    i += 1
print(''.join(words))
