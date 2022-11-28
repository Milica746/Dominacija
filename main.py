import pygame
from dominacija.constants import *
from dominacija.board import Board
import PySimpleGUI as sg
#sg.theme('Default1')  
sg.theme('Default2')  

layout = [
    [sg.Text('Please enter the number of rows and columns!')],
    [sg.Text('Rows', size =(15, 1)), sg.InputText()],
    [sg.Text('Columns', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Settings', layout)
event, values = window.read()
window.close()
print(event, values[0], values[1])  


#FPS=60


WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Dominacija')


def getRowColFromMouse(pos):
    x,y=pos
    if x>FRAME and y<HEIGHT-FRAME//2-FRAME: 
        row=int(y//SquareSize)
        col=int((x-FRAME)//SquareSize)
    else:
        row=-1
        col=-1
    return row, col

def main():
    run=True
    #clock=pygame.time.Clock()
    board = Board()
    pygame.font.init()
    while run:
       # clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                row, col=getRowColFromMouse(pos)
                if row!=-1 and col!=-1:
                    board.play(row, col)
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

#main()

if values[0]==None or values[1]==None:
    pygame.quit() # ??? poenta da se ne pokrene igrica

#ROWS= values[0], COLS=values[1]
#SquareSize=WIDTH//ROWS
#PieceSize=WIDTH//ROWS-15

if event.__eq__('Submit'):
    main()