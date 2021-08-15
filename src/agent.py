import torch,random
import numpy as np
from collections import deque
from main import game

MAX_MEMORY = 100000
BATCH_SIZE = 1000
LR = 0.01

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0.9  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)