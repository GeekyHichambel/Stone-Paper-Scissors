import pygame
import sys
import random
from pygame.locals import *
from pygame import mixer
from game_func import bg
from game_func import stone_button
from game_func import scissor_button
from game_func import paper_button
from game_func import Score
from music_loader import *

#------------- Initialization ----------#
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial',32)
fps = pygame.time.Clock()

#-------------  ATTRIBUTES ----------#

screen_width = 600
screen_height = 600
pygame.display.set_caption('S.P.S')
screen = pygame.display.set_mode((screen_width,screen_height))

#-------------  MUSIC ----------#
stone_sound.set_volume(0.1)
paper_sound.set_volume(0.1)
scissor_sound.set_volume(0.1)

#------------- DATA ----------#

choices = ["Stone", "Paper", "Scissor"]
player = ""
computer_score = 0
player_score = 0

#-------------  TEXT ----------#

choice_txt = font.render('YOUR CHOICE',True,(255,255,255))

#-------------  MAIN LOOP ----------#

working = True

while working:   

    screen.fill('black')
        
    for event in pygame.event.get():            
            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            pygame.quit()
            sys.exit()  

    screen.blit(bg,(0,0))
    screen.blit(choice_txt,(200,200))
    
    if stone_button.place(screen):
        computer = random.choice(choices)
        print('The computer choses: '+computer)
        player = "Stone"
        if computer == player:
            stone_sound.play()
            print('The rocks collide hence a tie')
        elif computer == "Scissor":
            stone_sound.play()
            print('Hard hit of stone makes the scissor break hence u win')
            player_score+=1
        elif computer == "Paper":
            paper_sound.play()
            print('Oops! The rock got caught by the paper hence u lose')
            computer_score+=1 

    if scissor_button.place(screen):
        computer = random.choice(choices)
        print('The computer choses: '+computer)
        player = "Scissor"
        if computer == player:
            scissor_sound.play()
            print('Oops! The scissors got stuck hence a tie')
        elif computer == "Stone":
            stone_sound.play()
            print('Scissor got rammed by the stone hence u lose')
            computer_score+=1
        elif computer == "Paper":
            scissor_sound.play()
            print('You cut the paper into pieces hence u win')
            player_score+=1

    if paper_button.place(screen):
        computer = random.choice(choices)
        print('The computer choses: '+computer)
        player = "Paper"
        if computer == player:
            paper_sound.play()
            print('Two lame papers cannot do much hence a tie')
        elif computer == "Scissor":
            scissor_sound.play()
            print('Paper got torn in halves hence u lose')
            computer_score+=1
        elif computer == "Stone":
            paper_sound.play()
            print('You trapped the stone like a bait hence u win')
            player_score+=1
    
    Score.show_pscore(50,530,player_score,screen)
    Score.show_cscore(320,530,computer_score,screen)
    pygame.display.update()
    fps.tick(60)