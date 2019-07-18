def find_frequency_duplicate(frequencies):
    while not(frequencies):
        return

    computed_frequencies = set([0])
    runner = 0
    last_frequency = 0
    duplicate_frequency = None

    while not(duplicate_frequency):
        try:
            frequency = frequencies[runner]
        except IndexError:
            runner = 0
            frequency = frequencies[runner]

        last_frequency += frequency
        if last_frequency in computed_frequencies:
            duplicate_frequency = last_frequency

        computed_frequencies.add(last_frequency)
        runner += 1

    return duplicate_frequency


# MAIN SCRIPT

with open('input.txt') as input:
    frequencies = list(map(int, input.read().split()))

print(find_frequency_duplicate(frequencies))
