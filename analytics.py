import errors
import instruction


# Python class for a test
class Instruction:
    pass
    # TO DO: instruction from a line


# Class to represent the queue
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, test):
        self.queue.append(test)

    def run(self):
        for test in self.queue:
            test.run()
        # TO DO
        self.queue.clear()
