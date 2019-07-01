ID_MARKER = '#'
START_DATETIME_MARKER = '['
END_DATETIME_MARKER = ']'
HOURS_SEPARATOR = ':'
SIGNIFIANT_HOUR = '00'
GUARD_BEGINS = 'begins shift'
GUARD_ASLEEP = 'falls asleep'
GUARD_WAKES = 'wakes up'

def parse_all(inputs):
    guards = {}
    records = create_records(inputs)

    for record in records:
        if record.guard_id > 0:
            if not(record.guard_id in guards):
                guard = Guard(record.guard_id)
                guards[guard.id] = guard
            else:
                guard = guards[record.guard_id]

        if record.hour == SIGNIFIANT_HOUR:
            if record.action == GUARD_ASLEEP:
                first_minute_asleep = record.minute
            elif record.action == GUARD_WAKES:
                for minute in range(first_minute_asleep, record.minute):
                    guard.nb_sleeps_by_minute[minute] += 1
                    guard.total_minutes_asleep += 1

    return guards.values()


def create_records(inputs):
    records = filter(None, list(map(parse, inputs)))
    return sorted(records, key=lambda record: (record.date, record.hour, record.minute))



def parse(input):
    if not(END_DATETIME_MARKER in input):
        return

    guard_id = -1

    dirty_datetime, remaining_input = input.split(END_DATETIME_MARKER)
    dirty_date, time = dirty_datetime.split()
    hour, minute = time.split(HOURS_SEPARATOR)
    date = dirty_date.replace(START_DATETIME_MARKER, '')

    if ID_MARKER in remaining_input:
        guard_id = remaining_input.split(ID_MARKER)[-1].split()[0]
        action = GUARD_BEGINS
    elif GUARD_ASLEEP in remaining_input:
        action = GUARD_ASLEEP
    else:
        action = GUARD_WAKES

    return Record(date, hour, int(minute), int(guard_id), action)

class Record:
    def __init__(self, date, hour, minute, guard_id, action):
        self.date = date
        self.hour = hour
        self.minute = minute
        self.guard_id = guard_id
        self.action = action

class Guard:
    def __init__(self, id):
        self.id = id
        self.nb_sleeps_by_minute = [0] * 60
        self.total_minutes_asleep = 0

    def most_slept_minute(self):
        return self.nb_sleeps_by_minute.index(max(self.nb_sleeps_by_minute))

