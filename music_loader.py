import pygame
import os
from pygame import mixer

pygame.init()
stone_sound = pygame.mixer.Sound(os.path.join("resources",'stone.mp3'))
paper_sound = pygame.mixer.Sound(os.path.join("resources",'paper.mp3'))
scissor_sound = pygame.mixer.Sound(os.path.join("resources",'scissor.mp3'))