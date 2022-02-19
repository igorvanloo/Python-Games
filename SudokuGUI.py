#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:57:04 2021

@author: igorvanloo
"""

import pygame as pg

def FindEmptySlot(sudoku): #Finds the empty slots of the sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i,j)
    return None

def IsPositionValid(sudoku, position, number): #Position = (i, j) = (row, column)
    
    for i in range(9): #Check if its in the same row
        if sudoku[position[0]][i] == number:
            if i != position[1]:
                return False
    
    for i in range(9): #Check if its in the same column
        if sudoku[i][position[1]] == number:
            if i != position[0]:
                return False 
    
    if position[0] < 3:
        start_x = 0
        end_x = 3
    elif position[0] >= 3 and position[0] < 6:
        start_x = 3
        end_x = 6
    elif position[0] >= 6:
        start_x = 6
        end_x = 9
        
    if position[1] < 3:
        start_y = 0
        end_y = 3
    elif position[1] >= 3 and position[1] < 6:
        start_y = 3
        end_y = 6
    elif position[1] >= 6:
        start_y = 6
        end_y = 9
        
    for i in range(start_x, end_x): #Check box
        for j in range(start_y, end_y):
            if sudoku[i][j] == number:
                if i != position[0] and j != position[1]:
                    return False
    return True
    
def SolveSudoku(sudoku, screen):
    fnt = pg.font.SysFont("comicsans", 40)
    gap = 60
    emptyslot = FindEmptySlot(sudoku)
    if emptyslot != None:
        row, column = emptyslot
    else:
        
        return True
    
    for i in range(1,10):
        if IsPositionValid(sudoku, (row, column), i):
            sudoku[row][column] = i
            
            text = fnt.render(str(i), True, pg.Color(0,0,0))
            pg.draw.rect(screen, (255,255,255), pg.Rect(column*gap, row*gap, gap, gap), 0)
            pg.draw.rect(screen, (0,255,0), pg.Rect(column*gap, row*gap, gap, gap), 3)
            screen.blit(text, (23 + column*60, row*60))
            pg.display.update()
            pg.time.delay(100)
            
            
            if SolveSudoku(sudoku, screen) == True:
                
                return True
            text = fnt.render(" ", True, pg.Color(0,0,0))
            pg.draw.rect(screen, (255,255,255), pg.Rect(column*gap, row*gap, gap, gap), 0)
            pg.draw.rect(screen, (255,0,0), pg.Rect(column*gap, row*gap, gap, gap), 3)
            screen.blit(text, (23 + column*60, row*60))
            pg.display.update()
            pg.time.delay(100)
            
            sudoku[row][column] = 0
    
    return False

def draw_screen(screen):
    
    gap = 540/9
    for i in range(0,10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pg.draw.line(screen, pg.Color(0,0,0), (0, i*gap), (540, i*gap), thickness)
        pg.draw.line(screen, pg.Color(0,0,0), (i * gap, 0), (i * gap, 540), thickness)

def draw_numbers(screen, sudoku):
    font = pg.font.SysFont("comicsans", 40)
    
    for row in range(9):
        for col in range(9):
            output = sudoku[row][col]
            if output == 0:
                output = " "
                
            text = font.render(str(output), True, pg.Color(0,0,0))
            screen.blit(text, (23 + col*60, row*60))
            
    
def draw_new_number(screen, pos, number):
    font = pg.font.SysFont("comicsans", 40)

    text = font.render(str(number), True, pg.Color("black"))
    screen.blit(text, (23 + pos[1]*60, pos[0]*60)) 

    
def draw_bottom_screen(screen, strikes):
    fnt = pg.font.SysFont("comicsans", 40)
    
    pg.draw.rect(screen, (255,255,255), pg.Rect(540, 0, 540, 110), 3) 
    
    text = fnt.render("Strikes:" + " X " * strikes, True, (255, 0, 0))
    screen.blit(text, (0, 580))
    
def main():
    sudoku = [
        [0, 0, 3, 0, 2, 0, 6, 0, 0], 
        [9, 0, 0, 3, 0, 5, 0, 0, 1], 
        [0, 0, 1, 8, 0, 6, 4, 0, 0], 
        [0, 0, 8, 1, 0, 2, 9, 0, 0], 
        [7, 0, 0, 0, 0, 0, 0, 0, 8], 
        [0, 0, 6, 7, 0, 8, 2, 0, 0], 
        [0, 0, 2, 6, 0, 9, 5, 0, 0], 
        [8, 0, 0, 2, 0, 3, 0, 0, 9], 
        [0, 0, 5, 0, 1, 0, 3, 0, 0]]
    
    new_sudoku = [
        [0, 0, 3, 0, 2, 0, 6, 0, 0], 
        [9, 0, 0, 3, 0, 5, 0, 0, 1], 
        [0, 0, 1, 8, 0, 6, 4, 0, 0], 
        [0, 0, 8, 1, 0, 2, 9, 0, 0], 
        [7, 0, 0, 0, 0, 0, 0, 0, 8], 
        [0, 0, 6, 7, 0, 8, 2, 0, 0], 
        [0, 0, 2, 6, 0, 9, 5, 0, 0], 
        [8, 0, 0, 2, 0, 3, 0, 0, 9], 
        [0, 0, 5, 0, 1, 0, 3, 0, 0]]
    
    pg.init()
    screen_size = 540, 650
    
    running = True
    key = None
    pos = None
    strikes = 0
    screen = pg.display.set_mode(screen_size)
    screen.fill(pg.Color("white"))
    draw_screen(screen)
    draw_numbers(screen, sudoku)
    draw_bottom_screen(screen, strikes)
    pg.display.flip()
    fnt = pg.font.SysFont("comicsans", 40)
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    key = 1
                if event.key == pg.K_2:
                    key = 2
                if event.key == pg.K_3:
                    key = 3
                if event.key == pg.K_4:
                    key = 4
                if event.key == pg.K_5:
                    key = 5
                if event.key == pg.K_6:
                    key = 6
                if event.key == pg.K_7:
                    key = 7
                if event.key == pg.K_8:
                    key = 8
                if event.key == pg.K_9:
                    key = 9
                if event.key == pg.K_BACKSPACE:
                    
                    if sudoku[pos[0]][pos[1]] == 0:
                        pg.draw.rect(screen, (255,255,255), pg.Rect(pos[1]*60, pos[0]*60, 60, 60), 0)
                        new_sudoku[pos[0]][pos[1]] = 0
                        draw_numbers(screen, new_sudoku)
                        draw_screen(screen)
                        pg.display.update()
                    else:
                        print("Can't remove this number!")
                    
                if event.key == pg.K_SPACE:
                    SolveSudoku(sudoku, screen)
                    print(sudoku)
                    draw_bottom_screen(screen, strikes)
                    text = fnt.render("Game Over", True, (0, 0, 0))
                    screen.blit(text, (270, 600))
                    
                    
            if event.type == pg.MOUSEBUTTONDOWN: #If mousedown, we get the position of the user
                mouse_pos = pg.mouse.get_pos()
                if mouse_pos[0] < 540 and mouse_pos[1] < 540:
                    gap = 540 / 9
                    x = mouse_pos[0] // gap
                    y = mouse_pos[1] // gap
                    pos = (int(y),int(x)) #Return top left co-ordinate
                    pg.draw.rect(screen, (255,0,0), pg.Rect(pos[1]*gap, pos[0]*gap, gap, gap), 3) #Draw red square around selected square
                    pg.display.update()
                else:
                    pos = None
                    
            if pos != None: #When we move square we remove the red square
                pg.draw.rect(screen, (255,255,255), pg.Rect(pos[1]*gap, pos[0]*gap, gap, gap), 3) 
                pg.draw.rect(screen, (0,0,0), pg.Rect(pos[1]*gap, pos[0]*gap, gap+1, gap+1), 1)
                draw_screen(screen)
            
            
        if key != None and pos != None:
            pg.draw.rect(screen, (255,255,255), pg.Rect(270, 600, 270, 50), 0)
            if new_sudoku[pos[0]][pos[1]] == 0:
                if IsPositionValid(new_sudoku, pos, key):
                    new_sudoku[pos[0]][pos[1]] = key
                    screen.fill(pg.Color("white"))
                    draw_screen(screen)
                    draw_bottom_screen(screen, strikes)
                    draw_numbers(screen, new_sudoku)

                else:
                    strikes += 1
                    if strikes == 3:
                        draw_bottom_screen(screen, strikes)
                        text = fnt.render("Game Over", True, (0, 0, 0))
                        screen.blit(text, (270, 600))
                        main()
                    else:
                        draw_bottom_screen(screen, strikes)
                        text = fnt.render("Wrong :(", True, (0, 0, 0))
                        screen.blit(text, (270, 580))
                    
                pg.display.update()
                key = None
            else:
                key = None

main()
pg.quit()
        