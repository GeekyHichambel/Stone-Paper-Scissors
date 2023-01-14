import pygame
import sys
from images import *

pygame.font.init()
font = pygame.font.SysFont('Arial',32)
#-------------  CLASSES ----------#
class buttons():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.pressed = False

    def place(self,screen):
        click = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                click = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.pressed = False                

        screen.blit(self.image,(self.rect.x,self.rect.y))

        return click

class score():
    def show_pscore(self, x, y, score, screen):
        self.player_score = score
        self.player_score_txt = font.render("PLAYER : "+str(self.player_score),True,(255,255,255))
        screen.blit(self.player_score_txt,(x,y))

    def show_cscore(self, x, y, score, screen):
        self.computer_score = score
        self.computer_score_txt = font.render("COMPUTER : "+str(self.computer_score),True,(255,255,255))
        screen.blit(self.computer_score_txt,(x,y))

#------------- BUTTONS ----------#

stone_button = buttons(100,280,stone)
scissor_button = buttons(240,280,scissor)
paper_button = buttons(380,280,paper)

#------------- SCORE ----------#
Score = score() 