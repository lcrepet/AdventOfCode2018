import collections
import heapq

class Manual:
    def __init__(self):
        self.instructions = collections.defaultdict(list)
        self.first_steps = set()
        self.following_steps = set()


    def add_instruction(self, step, following):
        self.instructions[step].append(following)

        self.following_steps.add(following)
        if following in self.first_steps:
            self.first_steps.remove(following)
        if step not in self.following_steps:
            self.first_steps.add(step)


class Assembly:
    def __init__(self, manual):
        self.manual = manual


    def run_instructions(self, nb_workers = 1):
        self.init_helpers_structures(nb_workers)

        while self.steps_heap or self.processed_steps:
            self.nb_steps += 1

            for worker in range(0, nb_workers):
                self.work(worker)

            while self.steps_to_process:
                heapq.heappush(self.steps_heap, self.steps_to_process.pop())

        print(self.nb_steps)
        print(''.join(self.done_steps))


    def work(self, worker):
        steps_to_process = []

        if not(self.workers_steps[worker]):
            if self.steps_heap:
                self.workers_steps[worker] = heapq.heappop(self.steps_heap)
            else:
                return

        step = self.workers_steps[worker]

        if step in self.processed_steps:
            self.processed_steps[step] -= 1
        else:
            self.processed_steps[step] = self.duration(step) - 1

        if self.processed_steps[step] == 0:
            del(self.processed_steps[step])
            self.workers_steps[worker] = None

            for following in self.manual.instructions[step]:
                self.steps_levels[following] -= 1
                if self.steps_levels[following] == 0:
                    self.steps_to_process.append(following)

            self.done_steps.append(step)


    def init_helpers_structures(self, nb_workers):
        self.init_steps_levels()
        self.init_steps_heap()

        self.processed_steps = {}
        self.steps_to_process = []
        self.done_steps = []
        self.workers_steps = [None] * nb_workers
        self.nb_steps = 0


    def init_steps_levels(self):
        self.steps_levels = collections.defaultdict(int)

        for step, followings in self.manual.instructions.items():
            for following in followings:
                self.steps_levels[following] += 1


    def init_steps_heap(self):
        self.steps_heap = list(self.manual.first_steps)
        heapq.heapify(self.steps_heap)


    def duration(self, step):
        return ord(step) - 4



