class Board():
    def __init__(self, num_sticks):
        self.positions = {i: False for i in range(1,6)}
        self.content = 0
        self.max = num_sticks
        self.finished = False

    def toggle_position(self, n):
        self.positions[n] = not self.positions[n]

    def insert_stick(self):
        self.content += 1
        if self.content == self.max:
            self.finished = True