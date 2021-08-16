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

    def get_State(self,game):
        pass

    def remember(self,state,action,reward,nextState,gameOver):
        pass

    def trainLongMemory(self):
        pass

    def traingShortMemory(self,state,action,reward,nextState,gameOver):
        pass

    def getAction(self,state):
        pass

def train():
    scores = []
    meanScores = []
    total = 0
    highScore = 0
    agent = Agent()
    newGame = game()
    while True:
        oldState = agent.get_State(newGame)

        lastMove = agent.getAction(oldState)

        reward, gameOver, score = newGame.playing(lastMove)

        newState = agent.get_State(newGame)

        agent.traingShortMemory(oldState,lastMove,reward,newState,gameOver)

        agent.remember(oldState,lastMove,reward,newState,gameOver)

        if gameOver:
            newGame.reset()
            agent.n_games += 1
            agent.trainLongMemory()

            if score > highScore:
                highScore = score
            print(f'Game {agent.n_games} score {score} High Score {highScore}')
if __name__ == '__main__':
    train()