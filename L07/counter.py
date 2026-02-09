class Counter():

    def __init__ (self):
        self._limit = 0
        self._value = 0
        self._strokes = ""

    def getValue(self):
        return self._value, self._strokes
    
    def click(self):
        self._value += 1
        self._strokes += "|"

        if self._value > self._limit:
            print("Limit Exceeded")

    def reset(self):
        self._value = 0

    def setLimit(self, maximum):
        self._limit = maximum

    