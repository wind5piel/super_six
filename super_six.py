import math
from random import randint

from strategies import strat_list


class Player():
    def __init__(self, name, sticks_per_player, strategy):
        self.name = name
        self.num_sticks = sticks_per_player
        self.finished = False
        self.go_on = True
        self.strategy = strategy

    def drop_stick(self, die_face, board):
        self.num_sticks -= 1
        print('dropping a stick')
        self.go_on = self.strategy(die_face, board)
        if self.num_sticks <= 0:
            self.finished = True
            self.go_on = False
            print(f'{self.name}: I have no sticks left!')

    def take_stick(self):
        self.num_sticks += 1
        self.go_on = False
        print('taking a stick')



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
            print('game finished')
            self.finished = True

class Game():
    def __init__ (self, list_of_strategies, num_sticks):
        num_players = len(list_of_strategies)
        sticks_per_player = math.floor(num_sticks/num_players)
        num_sticks = sticks_per_player * num_players

        self.board = Board(num_sticks)
        self.players = [Player(f'Player {i+1}', sticks_per_player, strat_list[i]) for i in range(num_players)]


        
    
    def roll_die(self, player_num):

        active_player = self.players[player_num]
        active_player.go_on = True

        print(active_player.name)

        while active_player.go_on:


            face = randint(1,6)

            print(f'{face=}')

            if face == 6:
                self.board.insert_stick()
                active_player.drop_stick(face, self.board)
            else:
                hit = self.board.positions[face]
                if hit:
                    active_player.take_stick()
                else:
                    active_player.drop_stick(face, self.board)
                

                self.board.toggle_position(face)
                # active_player.go_on = False



        print(f'{active_player.name} has {active_player.num_sticks} sticks left')







game = Game(strat_list ,36)

for n in range(200):
    fin = False
    for i,s in enumerate(strat_list):
        game.roll_die(i)

        if game.players[i].finished:
            
            fin = True
            break
        elif game.board.finished:
            fin = True
            break

    if fin:
        print(game.board.content)
        for p in game.players:
            print(f'{p.name}: {p.num_sticks=} left')

        break


