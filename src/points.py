import pygame

def points(score,gameSpeed):
    score += 1
    if score % 50 == 0:
        gameSpeed += 1
    return [score,gameSpeed]