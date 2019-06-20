def compute_frequencies_history(frequencies):
    history = [0]
    index = 0

    for frequency in frequencies:
        history.append(history[index] + frequency)
        index += 1

    return history


def find_duplicate_frequency_from(history):
    step = history.pop()

    if step == 0:
        return history[0]

    c_index = 0
    f_index = 0
    duplicate_frequency = None
    candidate = None

    for c_index in range(0, len(history) - 1):
        for f_index in range(c_index + 1, len(history)):
            if history[c_index] == history[f_index]:
                duplicate_frequency = history[c_index]
                break

            diff = history[c_index] - history[f_index]
            if diff % step == 0:
                potential_candidate = select_best_potential_candidate(c_index, f_index, diff, step, history)
                candidate = select_best_candidate(candidate, potential_candidate)

    if not(duplicate_frequency) and candidate:
        duplicate_frequency = history[candidate[1]] + candidate[0] * step

    return duplicate_frequency


def select_best_potential_candidate(first_potential, second_potential, difference, step, history):
    quotient = int(abs(difference/step))

    if step > 0:
        return (quotient, min(first_potential, second_potential, key=lambda index: frequencies_history[index]))
    else:
        return (quotient, max(first_potential, first_potential, key= lambda index: frequencies_history[index]))


def select_best_candidate(current_best, potential):
    if current_best:
        return min(current_best, potential)

    return potential


# MAIN SCRIPT
with open('input.txt') as input:
    frequencies = map(int, input.read().split())

frequencies_history = compute_frequencies_history(frequencies)

print(find_duplicate_frequency_from(frequencies_history))
