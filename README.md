# ReinforcmentLearning
All relevant code description for project

# Week 1 and 2 work
For the code written for frozen lake the description of how the code works is written step by step below:
Frozen Lake's Q-learning Implementation
This project we use OpenAI's Gym library's Frozen Lake environment to solve a Q-learning algorithm. A detail description of each step in the implementation is provided below:

Bringing Libraries in
To begin with, we import the required libraries: random to help with the exploration-exploitation tradeoff, gym to access the Frozen Lake environment, and numpy for numerical calculations.

Establishing the Scene
We set is_slippery to False in order to generate the Frozen Lake environment. As a result, the environment becomes deterministic, which makes learning easier because the agent's actions always have predictable results.

Setting up the Q-table 
We then calculate the dimensions of the state and action spaces. We begin a Q-table as a matrix of zeros using these sizes. Each state-action pair's Q-values will be kept in this table. The projected future benefit of performing a certain action in a specific condition is represented by the Q-value. 
Configuring Hyperparameters 
Several hyperparameters are defined by us namely: 
-The quantity of training episodes is indicated by the variable total_episodes. 
-The agent's learning_rate controls how quickly it acquires new information. 
The maximum steps in each episode is specified by the value max_steps. 
-Gamma, the discount factor, strikes a balance between benefits now and in the future. 
-Epsilon sets the exploration rate, which starts at 1 to permit complete exploration at first. 
-The limitations for epsilon are specified by max_epsilon and min_epsilon.
-The amount of time that epsilon declines, or decay_rate, limits the amount of exploration. In addition, we establish a list to hold the total prizes earned for each episode. 

Training the Agent 
The training loop is the main component of the implementation and it lasts for a predetermined number of episodes which are mentioned below: 
-Every episode begins with the environment being reset to its initial condition. We set total rewards to 0 and done to False in the beginning.
-The agent chooses whether to explore new actions (by selecting a random action) or exploit its present knowledge (by selecting the action with the greatest Q-value) for each step in an episode.
-Epsilon, which gradually reduces to favor exploitation as learning advances, serves as the basis for this choice.

Finally we evaluate the Agent 
We conduct many test events to assess the agent's performance following training. The agent chooses actions in each test episode based on the learnt Q-values. We publish the steps the agent took and the overall number of steps needed to fall into a pit or achieve the goal. This aids in our comprehension of the agent's level of learning the best course of action.

# Week 3
I tried to write a code where AI uses best possible stratagies to play game 2048.
Here below is the step by step explaination of code written for game 2048.
 - Two starting tiles (either two or four) are placed at random vacant spots on a 4x4 game board by the `Game2048` class, which initializes the board with zeros. 
 -With a 90% probability of being a 2 and a 10% chance of being a 4, the `_add_new_tile` function finds vacant spots on the board and adds a new tile. 
 -The `_merge} method updates the score with the value of the combined tiles and compresses a row by deleting zeros and combining adjacent equal tiles.
 -If the board changes, the move_left function inserts a new tile and moves all of the tiles to the left, merging them together.
 -The move_right function rotates the board in a horizontal direction, then uses the move_left method to move the tiles to the left before flipping it back to its initial position.
 -The move_up function shifts tiles left, transposes the board (switching rows and columns), and then transposes it back.
 -The move_down function flips the board, moves the tiles to the left, transposes it, flips it back, and then flips it again.
 -The get_possible_moves function generates a list of movements that alter the state of the board by simulating every move that might be made (left, right, up, and down).
 -The is_game_over function determines whether the game is over when there are no more moves that can be made.
 -The board's condition and the current score are printed using the display method.
 -A Game2048 instance is used to initialize the AI2048 class, providing AI the ability to play the game.
 -Based on the amount of vacant tiles and the greatest tile value on the board, the heuristic -technique determines a heuristic value for the AI.
 -The move with the greatest heuristic value is determined by the get best move method, which simulates all possible movements and assesses them using the heuristic function.
 -The AI class's play function keeps trying to make the best move until there are none left. It displays the board following each move and declares "Game Over!" when the round is over.
 -A Game2048 instance is generated in the main execution, and then an AI2048 play method is called to play the game automatically.

