#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:01:04 2021

@author: igorvanloo
"""

import pygame as pg

def winning_position(ttt, symbol, screen):
    dim = 3
    gap = 200
    for x in range(dim):
        if ttt[0][x] == ttt[1][x] == ttt[2][x] == symbol:
            pg.draw.line(screen, (0,0,0), (97 + x*gap, 50), (97 + x*gap, 550), 10)
    for x in range(dim):
        if ttt[x][0] == ttt[x][1] == ttt[x][2] == symbol:
            pg.draw.line(screen, (0,0,0), (50, 97 + x*gap), (550, 97 + x*gap), 10)
    if ttt[0][0] == ttt[1][1] == ttt[2][2] == symbol:
        pg.draw.line(screen, (0,0,0), (50, 50), (550,550), 10)
    if ttt[2][0] == ttt[1][1] == ttt[0][2] == symbol:
        pg.draw.line(screen, (0,0,0), (50, 550), (550,50), 10) 
    
def valid_position(tictactoe, pos):
    if tictactoe[pos[0]][pos[1]] == 0:
        return True
    return False

def draw_screen(screen):
    
    gap = 600/3
    for i in range(0,3):
        if i % 3 == 0:
            thickness = 4

        pg.draw.line(screen, pg.Color(0,0,0), (0, i*gap), (600, i*gap), thickness)
        pg.draw.line(screen, pg.Color(0,0,0), (i * gap, 0), (i * gap, 600), thickness)

def draw_numbers(screen, tictactoe):
    font = pg.font.SysFont("comicsans", 40)
    
    for row in range(3):
        for col in range(3):
            output = tictactoe[row][col]
            if output == 0:
                output = " "
                
            text = font.render(str(output), True, pg.Color(0,0,0))
            screen.blit(text, (23 + col*200, 20 + row*200))
            
def main():
    tictactoe = [
        [0,0,0],
        [0,0,0],
        [0,0,0]]
    
    pg.init()
    screen_size = 600, 600
    
    running = True
    pos = None
    Player_1 = True
    Player_2 = False
    screen = pg.display.set_mode(screen_size)
    screen.fill(pg.Color("white"))
    draw_screen(screen)
    pg.display.flip()
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
            if event.type == pg.MOUSEBUTTONDOWN: #If mousedown, we get the position of the user
                mouse_pos = pg.mouse.get_pos()
                if mouse_pos[0] < 540 and mouse_pos[1] < 540:
                    gap = 600 / 3
                    x = mouse_pos[0] // gap
                    y = mouse_pos[1] // gap
                    pos = (int(y),int(x)) #Return top left co-ordinate
                    if Player_1 and valid_position(tictactoe, pos):
                        pg.draw.circle(screen, (0,0,0), (100 + pos[1]*200, 100 + pos[0]*200), 70, 2) 
                        tictactoe[pos[0]][pos[1]] = "O"
                        winning_position(tictactoe, "O", screen)
                        pg.display.update()
                        Player_1 = False
                        Player_2 = True
                        
                    if Player_2 and valid_position(tictactoe, pos):
                        pg.draw.rect(screen, (0,0,0), pg.Rect(30 + pos[1]*gap, 30 + pos[0]*gap, gap-60, gap-60), 2) 
                        tictactoe[pos[0]][pos[1]] = "X"
                        winning_position(tictactoe, "X", screen)
                        pg.display.update()
                        Player_1 = True
                        Player_2 = False
                else:
                    pos = None
                    
main()
pg.quit()