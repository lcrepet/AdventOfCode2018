def find_uniq_difference_between(first_id, second_id):
    difference_index = None
    nb_differences = 0

    for k in range(0, len(first_id)):
        if first_id[k] != second_id[k]:
            nb_differences += 1
            difference_index = k

        if nb_differences > 1:
            difference_index = None
            break

    return difference_index

# MAIN SCRIPT
with open('input.txt') as input:
    ids = input.read().split()

common_characters = None

for i in range(0, len(ids) - 1):
    for j in range(i + 1, len(ids)):
        difference_index = find_uniq_difference_between(ids[i], ids[j])

        if difference_index:
            common_characters = ids[j][:difference_index] + ids[j][difference_index + 1:]
            break

    if difference_index:
        break

print(common_characters)

