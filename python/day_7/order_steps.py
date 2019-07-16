import kit

manual = kit.Manual()
assembly = kit.Assembly(manual)

with open('input.txt') as input_file:
    for line in input_file:
        dirty_current, dirty_following = line.split(' must be finished before step ')
        manual.add_instruction(dirty_current[-1], dirty_following[0])

assembly.run_instructions()
