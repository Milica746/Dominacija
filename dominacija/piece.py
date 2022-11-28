import pygame
from .constants import *

class Piece():
    PADDING=(SquareSize-PieceSize)/2
    #PADDING2=(2*SquareSize-2*PieceSize)/2 =>padding*2
    OUTLINE=1
    def __init__(self, row, col, color, num):
        self.row=row
        self.col=col
        self.color=color
        self.num=num
        self.x=0
        self.y=0
        self.calc_position()

    def calc_position(self):
        self.x=SquareSize*self.col+FRAME
        self.y=SquareSize*self.row

    def draw(self, win):
        textFont=pygame.font.SysFont("consolas", 15)
        text=textFont.render(str(self.num), 5, WHITE)
        textRect = text.get_rect()
        if self.color==RED:
            pygame.draw.rect(win, self.color, (self.x+self.PADDING, self.y+self.PADDING*2, PieceSize, PieceSize*2), 0, 15)
            pygame.draw.rect(win, BLACK, (self.x+self.PADDING, self.y+self.PADDING*2, PieceSize, PieceSize*2), 2, 15)
            textRect.center = ((self.x+SquareSize//2), self.y+SquareSize)
            win.blit(text,textRect)
        else:
            pygame.draw.rect(win, self.color, (self.x+self.PADDING*2, self.y+self.PADDING, PieceSize*2, PieceSize), 0, 15)
            pygame.draw.rect(win, BLACK, (self.x+self.PADDING*2, self.y+self.PADDING, PieceSize*2, PieceSize), 2, 15)
            textRect.center = ((self.x+SquareSize), self.y+SquareSize//2)
            win.blit(text, textRect)
        

    def __repr__(self):
        return str(self.color)