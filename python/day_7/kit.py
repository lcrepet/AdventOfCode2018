import collections
import heapq

class Manual:
    """
    Store a sleigh's instructions for assembly.
    """

    def __init__(self):
        self.instructions = collections.defaultdict(list)
        self.first_steps = set()
        self.following_steps = set()


    def add_instruction(self, step, following):
        """
        Add one instruction to the manual

        An instruction describes in which order two steps should be run.
        Each time an instruction is added, first_steps set is updated to keep
        trace of all steps that can be run first (without another step run
        before).

        :param step: a given step of assembly
        :param following: step that can be run after "step"
        :rtype: None
        """


        self.instructions[step].append(following)

        self.following_steps.add(following)
        if following in self.first_steps:
            self.first_steps.remove(following)
        if step not in self.following_steps:
            self.first_steps.add(step)


class Assembly:
    """
    Allow to "assemble" a sleigh.
    """

    def __init__(self, manual):
        """
        :param manual: sleigh's manual
        :type manual: Manual
        """

        self.manual = manual


    def run_instructions(self, nb_workers=1):
        """
        Run the manual's instructions with a given number of workers

        Print the number and the sequence of done steps

        :param nb_workers: number of workers assembling the sleigh
        :type nb_workers: int
        :rtype: None
        """

        self.__init_helpers_structures(nb_workers)

        while self.__steps_heap or self.__processed_steps:
            self.__nb_steps += 1

            for worker in range(0, nb_workers):
                self.__work(worker)

            while self.__steps_to_process:
                heapq.heappush(self.__steps_heap, self.__steps_to_process.pop())

        print(self.__nb_steps)
        print(''.join(self.__done_steps))


    def __work(self, worker):
        steps_to_process = []

        if not(self.__workers_steps[worker]):
            if self.__steps_heap:
                self.__workers_steps[worker] = heapq.heappop(self.__steps_heap)
            else:
                return

        step = self.__workers_steps[worker]

        if step in self.__processed_steps:
            self.__processed_steps[step] -= 1
        else:
            self.__processed_steps[step] = self.__duration(step) - 1

        if self.__processed_steps[step] == 0:
            del(self.__processed_steps[step])
            self.__workers_steps[worker] = None

            for following in self.manual.instructions[step]:
                self.__steps_levels[following] -= 1
                if self.__steps_levels[following] == 0:
                    self.__steps_to_process.append(following)

            self.__done_steps.append(step)


    def __init_helpers_structures(self, nb_workers):
        self.__init_steps_levels()
        self.__init_steps_heap()

        self.__processed_steps = {}
        self.__steps_to_process = []
        self.__done_steps = []
        self.__workers_steps = [None] * nb_workers
        self.__nb_steps = 0


    def __init_steps_levels(self):
        self.__steps_levels = collections.defaultdict(int)

        for step, followings in self.manual.instructions.items():
            for following in followings:
                self.__steps_levels[following] += 1


    def __init_steps_heap(self):
        self.__steps_heap = list(self.manual.first_steps)
        heapq.heapify(self.__steps_heap)


    def __duration(self, step):
        return ord(step) - 4



