import math
from random import randint

from classes.board import Board
from classes.player import Player

class Game():
    def __init__ (self, list_of_strategies, num_sticks):
        num_players = len(list_of_strategies)
        sticks_per_player = math.floor(num_sticks/num_players)
        num_sticks = sticks_per_player * num_players

        self.board = Board(num_sticks)
        self.players = [Player(f'Player {i+1}', sticks_per_player, list_of_strategies[i]) for i in range(num_players)]


        
    
    def roll_die(self, player_num):

        active_player = self.players[player_num]
        active_player.go_on = True

        while active_player.go_on:


            face = randint(1,6)

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