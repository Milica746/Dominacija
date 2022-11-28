import pygame
from .piece import Piece
from .constants import *

class Board():
    def __init__(self):
        self.board=[]
        self.selected=None
        self.player=0
        self.num=1
        self.create_board()
    
    def draw_squares(self, win):
        win.fill(WHITE)
        pygame.draw.rect(win, GRAY, (FRAME, 0, WIDTH-FRAME, HEIGHT-FRAME), 2)
        for row in range(ROWS):
            for col in range(row%2, ROWS, 2): #da li red krece belom ili crnoom bojom
                pygame.draw.rect(win, GRAY, (row*SquareSize+FRAME, col*SquareSize, SquareSize, SquareSize))
       
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        textFont=pygame.font.SysFont("consolas", 15)
        for i in range(ROWS):
            text=textFont.render(str(ROWS-i), 1, BLACK)
            textRect = text.get_rect()
            textRect.center = ((FRAME//2), i*SquareSize+SquareSize//2)
            win.blit(text,textRect)
        for i in range(COLS):
            text=textFont.render(chr(97+i), 1, BLACK)
            textRect = text.get_rect()
            textRect.center = (FRAME+i*SquareSize+SquareSize//2, HEIGHT-FRAME//2)
            win.blit(text, textRect)
          
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 and piece!=1:
                    piece.draw(win)

    def play(self, row, col):
        # provera za van table
        if(row == -1 or row >= ROWS or col == -1 or col >= COLS-1): # ovo ce se promeniti kad se dodaju oznake, iz -1 u 0, iz rows u rows+1
            return
        if self.player==0 and self.board[row][col]==0 and self.board[row-1][col]==0:
            # provera za vertikalno
            if row==0:
                return
            piece=Piece(row-1, col, RED, self.num)
            self.num+=1
            self.board[row][col]=piece
            self.board[row-1][col]=1
            self.player=1
        elif self.player==1 and self.board[row][col]==0 and self.board[row][col+1]==0:
            # provera za horizontalno
            if col==COLS-1:
                return
            piece=Piece(row, col, LIGHTBLACK, self.num)
            self.num+=1
            self.board[row][col]=1
            self.board[row][col+1]=piece
            self.player=0
