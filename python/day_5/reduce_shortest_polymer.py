import lab

with open('input.txt') as input_file:
    polymer = lab.Polymer(input_file.read().strip())

tested_units = set()
shortest_polymer = polymer.units

for unit in polymer.units:
    if not(unit in tested_units):
        tested_units.add(unit)
        reduced_polymer = polymer.reduce(avoided_type=unit)

        if len(reduced_polymer) < len(shortest_polymer):
            shortest_polymer = reduced_polymer

print(len(shortest_polymer))



