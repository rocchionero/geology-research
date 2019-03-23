class Counter:
    def __init__(self):
        self.data = {}

    def add(self, element):
        element = str(element)
        if element in self.data.keys():
            self.data[element] += 1
        else:
            self.data[element] = 1

