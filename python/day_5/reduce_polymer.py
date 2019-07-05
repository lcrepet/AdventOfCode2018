import lab

with open('input.txt') as input_file:
    polymer = lab.Polymer(input_file.read().strip())

print(len(polymer.reduce()))
