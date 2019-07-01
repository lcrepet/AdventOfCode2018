import parser

with open('input.txt') as input_file:
    guards = parser.parse_all(input_file.read().split('\n'))

most_slept_minute_asleep_time = {}
for guard in guards:
    most_slept_minute_asleep_time[guard] = guard.nb_sleeps_by_minute[guard.most_slept_minute()]

most_frequently_asleep_guard = max(guards, key=lambda guard: guard.nb_sleeps_by_minute[guard.most_slept_minute()])

print(int(most_frequently_asleep_guard.id) * most_frequently_asleep_guard.most_slept_minute())
