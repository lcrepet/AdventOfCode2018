def sum_frequencies(frequencies):
    return sum(frequencies)


# MAIN SCRIPT

with open('input.txt') as input:
    frequencies = map(int, input.read().split())

print(sum_frequencies(frequencies))
