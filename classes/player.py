class Player():
    def __init__(self, name, sticks_per_player, strategy):
        self.name = name
        self.num_sticks = sticks_per_player
        self.finished = False
        self.go_on = True
        self.strategy = strategy

    def drop_stick(self, die_face, board):
        self.num_sticks -= 1
        self.go_on = self.strategy(die_face, board)
        if self.num_sticks <= 0:
            self.finished = True
            self.go_on = False

    def take_stick(self):
        self.num_sticks += 1
        self.go_on = False