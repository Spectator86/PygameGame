class Timer:
    def __init__(self, t):
        self.maxt = t
        self.t = t

    def update(self):
        self.t += 1

    def check(self):
        if self.t >= self.maxt:
            return True
        else:
            return False