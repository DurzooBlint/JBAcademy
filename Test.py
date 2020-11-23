import itertools

flower_names = ['rose', 'tulip', 'sunflower', 'daisy']
bouquet = []

for i in range(1, 4):
    bouquet += itertools.combinations(flower_names, i)

for el in bouquet:
    print(el)

