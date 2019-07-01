import parser

with open('input.txt') as input_file:
    guards = parser.parse_all(input_file.read().split('\n'))

most_asleep_guard = max(guards, key=lambda guard: guard.total_minutes_asleep)

print(int(most_asleep_guard.id) * most_asleep_guard.most_slept_minute())
