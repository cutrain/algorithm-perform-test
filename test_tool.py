import time

class Timer:
    def __init__(self):
        self.__total = 0.
        self.__count = 0
    def __call__(self, func, *args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        self.__total += end - start
        self.__count += 1

    @property
    def total_cost(self):
        return self.__total

    @property
    def avg_cost(self):
        return self.__total / self.__count

