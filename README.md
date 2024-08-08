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


# Week 4 till final project submission
worked upon 2048 game code tried to make it more accurate.
