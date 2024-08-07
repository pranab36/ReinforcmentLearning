# -*- coding: utf-8 -*-
"""2048Game_Final

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FRs0Y96kpxtFLWhfks6OJ_HGQsYhASWR
"""

import numpy as np
import random
from collections import defaultdict
import matplotlib.pyplot as plt

# Define the 2048 game environment
class Game2048:
    def __init__(self):
        self.reset()

    def reset(self):
        # Initialize the game board with zeros
        self.board = np.zeros((4, 4), dtype=int)
        # Add two random tiles to the board
        self.add_random_tile()
        self.add_random_tile()
        return self.board

    def add_random_tile(self):
        # Find empty positions on the board
        empty_positions = list(zip(*np.where(self.board == 0)))
        if empty_positions:
            # Randomly choose one empty position
            row, col = random.choice(empty_positions)
            # Add a 2 or 4 tile to the chosen position
            self.board[row, col] = 4 if random.random() < 0.1 else 2

    def move(self, direction):
        # Track if any tile has moved
        moved = False
        if direction == 0:  # Move Up
            for col in range(4):
                non_zero = [self.board[row, col] for row in range(4) if self.board[row, col] != 0]
                new_col = self.merge(non_zero)
                for row in range(4):
                    if self.board[row, col] != new_col[row]:
                        moved = True
                    self.board[row, col] = new_col[row]
        elif direction == 1:  # Move Right
            for row in range(4):
                non_zero = [self.board[row, col] for col in range(4) if self.board[row, col] != 0]
                new_row = self.merge(non_zero)
                for col in range(4):
                    if self.board[row, col] != new_row[col]:
                        moved = True
                    self.board[row, col] = new_row[col]
        elif direction == 2:  # Move Down
            for col in range(4):
                non_zero = [self.board[row, col] for row in range(3, -1, -1) if self.board[row, col] != 0]
                new_col = self.merge(non_zero)
                for row in range(3, -1, -1):
                    if self.board[row, col] != new_col[3 - row]:
                        moved = True
                    self.board[row, col] = new_col[3 - row]
        elif direction == 3:  # Move Left
            for row in range(4):
                non_zero = [self.board[row, col] for col in range(4) if self.board[row, col] != 0]
                new_row = self.merge(non_zero)
                for col in range(4):
                    if self.board[row, col] != new_row[col]:
                        moved = True
                    self.board[row, col] = new_row[col]

        if moved:
            self.add_random_tile()
        return moved

    def merge(self, line):
        # Merge tiles in a single row or column
        new_line = []
        skip = False
        for i in range(len(line)):
            if skip:
                skip = False
                continue
            if i + 1 < len(line) and line[i] == line[i + 1]:
                new_line.append(line[i] * 2)
                skip = True
            else:
                new_line.append(line[i])
        # Fill the rest of the line with zeros
        new_line.extend([0] * (4 - len(new_line)))
        return new_line

    def is_game_over(self):
        # Check if no more moves are possible
        for direction in range(4):
            temp_board = np.copy(self.board)
            if self.move(direction):
                self.board = temp_board
                return False
        return True

    def get_reward(self):
        # Reward is the sum of all tile values on the board
        return np.sum(self.board)

# Define the N-tuple network
class NtupleNetwork:
    def __init__(self, n_tuples):
        # Initialize n-tuple patterns and value tables
        self.n_tuples = n_tuples
        self.tables = [defaultdict(float) for _ in n_tuples]

    def get_value(self, board):
        # Calculate the value of a board state based on n-tuple patterns
        value = 0
        for i, n_tuple in enumerate(self.n_tuples):
            index = tuple(board.flatten()[n_tuple])
            value += self.tables[i][index]
        return value

    def update_value(self, board, delta):
        # Update value tables with the reward delta
        for i, n_tuple in enumerate(self.n_tuples):
            index = tuple(board.flatten()[n_tuple])
            self.tables[i][index] += delta

def generate_n_tuples():
    # Generate patterns for n-tuple evaluation
    n_tuples = [
        [0, 1, 2, 3],      # Rows
        [4, 5, 6, 7],      # Rows
        [8, 9, 10, 11],    # Rows
        [12, 13, 14, 15],  # Rows
        [0, 4, 8, 12],     # Columns
        [1, 5, 9, 13],     # Columns
        [2, 6, 10, 14],    # Columns
        [3, 7, 11, 15],    # Columns
        [0, 1, 4, 5],      # 2x2 Squares
        [2, 3, 6, 7],      # 2x2 Squares
        [8, 9, 12, 13],    # 2x2 Squares
        [10, 11, 14, 15],  # 2x2 Squares
    ]
    return n_tuples

def play_game(env, network, alpha=0.1):
    # Play a game and update the n-tuple network
    env.reset()
    done = False
    total_reward = 0
    while not done:
        board = env.board.copy()
        best_move, best_value = None, -float('inf')

        for move in range(4):
            temp_board = board.copy()
            moved = env.move(move)
            if moved:
                value = network.get_value(env.board)
                if value > best_value:
                    best_value = value
                    best_move = move
            env.board = temp_board

        if best_move is not None:
            moved = env.move(best_move)
            reward = env.get_reward()
            delta = alpha * (reward + network.get_value(env.board) - network.get_value(board))
            network.update_value(board, delta)
            total_reward += reward
        else:
            done = True

    return total_reward

# Initialize 2048 environment and N-tuple network
env = Game2048()
n_tuples = generate_n_tuples()
network = NtupleNetwork(n_tuples)

# Train the AI for a number of games
num_games = 500
for i in range(num_games):
    reward = play_game(env, network)
    if (i + 1) % 50 == 0:
        print(f'Game {i + 1}: Total Reward = {reward}')

# Display the final board state
plt.imshow(env.board, cmap='gray')
plt.title("Final Board State")
plt.colorbar()
plt.show()