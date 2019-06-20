with open('input.txt') as input:
    ids = input.read().split()

twice_counter = 0
thrice_counter = 0

for id in ids:
    once_set = set()
    twice_set = set()
    thrice_set = set()
    too_many_set = set()

    for char in id:
        if char in twice_set:
            thrice_set.add(char)
            twice_set.remove(char)
        elif char in once_set:
            twice_set.add(char)
            once_set.remove(char)
        elif char in thrice_set:
            too_many_set.add(char)
            thrice_set.remove(char)
        elif char not in too_many_set:
            once_set.add(char)

    if len(twice_set) > 0:
        twice_counter += 1

    if len(thrice_set) > 0:
        thrice_counter += 1

print(twice_counter * thrice_counter)

