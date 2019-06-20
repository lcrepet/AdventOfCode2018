with open('input.txt') as input:
    frequencies = map(int, input.read().split())

total = sum(frequencies)
print(total)
