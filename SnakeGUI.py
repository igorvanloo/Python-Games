#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:39:19 2021

@author: igorvanloo
"""

import pygame as pg
import random, time

def draw_score(screen, score):
    pg.draw.rect(screen, (255,255,255), pg.Rect(0, 0, 540, 30), 0)
    fnt = pg.font.SysFont("comicsans", 40)
    text = fnt.render("Score: " + str(score), True, (255, 0, 0))
    screen.blit(text, (0, 0))
    
def draw_gameover(screen):
    fnt = pg.font.SysFont("comicsans", 40)
    text = fnt.render("Game over", True, (255, 0, 0))
    screen.blit(text, (200, 0))
    
def draw_screen(screen):
    
    gap = 18
    for i in range(0,30):
        thickness = 1
        pg.draw.line(screen, pg.Color(0,0,0), (0, 30 + i*gap), (540, 30 +i*gap), thickness)
        pg.draw.line(screen, pg.Color(0,0,0), (i * gap, 30), (i * gap, 570), thickness)
        
def food(screen, snake_pixels):
    gap = 18
    while True:
        x = random.randint(0, 29)
        y = random.randint(0, 29)
        
        if [x,y] not in snake_pixels:
            break
        
    pg.draw.rect(screen, (255,0,0), pg.Rect(x*gap + 1, 31 + y*gap, gap-1, gap-1), 0)
    
    print(x,y)
    print(snake_pixels)
    return [x,y]
    
def snake(screen, snake_pixels):
    gap = 18
    
    for pixel in snake_pixels:
        pg.draw.rect(screen, (0,128,0), pg.Rect(pixel[0]*gap + 1, pixel[1]*gap + 31, gap-1, gap-1), 0) 
    
def main():
    
    pg.init()
    screen_size = 540, 570
    
    gameover = False
    score = 0
    x_pos = 0
    y_pos = 0
    snake_pixels = [[15,15]]
    screen = pg.display.set_mode(screen_size)
     
    screen.fill(pg.Color("white"))
    draw_screen(screen)
    draw_score(screen, score)
    food_pos = food(screen, snake_pixels)
    snake(screen, snake_pixels)
    pg.display.update()
    game_running = True
    
    while game_running:
        
        while gameover:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameover = False
                    game_running = False
                
                if event.type == pg.KEYDOWN: 
                    if event.key == pg.K_1: 
                        main()
                        
                    if event.key == pg.K_2:
                        game_running = False
                        gameover = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False
            
            if event.type == pg.KEYDOWN:  
                if event.key == pg.K_UP:
                    x_pos = -1
                    y_pos = 0
                if event.key == pg.K_DOWN:
                    x_pos = 1
                    y_pos = 0
                if event.key == pg.K_LEFT:
                    x_pos = 0
                    y_pos = -1
                if event.key == pg.K_RIGHT:
                    x_pos = 0
                    y_pos = 1
                if event.key == pg.K_SPACE:
                    print("Optimal strategy will procede")
                    optimal_path = [[0,0]]
                    
                    forward = True
                    y = 0
                    while True:
                        
                        if forward:
                            for x in range(1,30):
                                optimal_path.append([x,y])
                                forward = False
                        else:
                            for x in range(29,0,-1):
                                optimal_path.append([x,y])
                                forward = True
                        y += 1
                        
                        if y == 30:
                            for y in range(29, 0, -1):
                                
                                optimal_path.append([0,y])
                            break
                    
                    starting_index = optimal_path.index(snake_pixels[0])
                    
                    while True:
                        time.sleep(0.005)
                        
                        current_pixel = optimal_path[(starting_index) % len(optimal_path)]
                        
                        if current_pixel != food_pos:
                            cst = snake_pixels.pop(0)
                            pg.draw.rect(screen, (255,255,255), pg.Rect(cst[0]*18 + 1, cst[1]*18 + 31, 18-1, 18-1), 0)
                            snake_pixels.append(current_pixel)
                        else:
                            score += 1 
                            draw_score(screen, score)
                            snake_pixels.append(current_pixel)
                            food_pos = food(screen, snake_pixels)
                     
                        snake(screen, snake_pixels)
                        draw_screen(screen)
                        pg.display.update()
                        
                        starting_index += 1
                        
                        if starting_index % 10000 == 0:
                            userinput = input("Would you like to continue? y or n ")
                            if userinput == "n":
                                break
                            else:
                                continue
        
        csh = snake_pixels[-1] #current snake head
        cst = snake_pixels[0] #current snake tail
        x = csh[0] + y_pos
        y = csh[1] + x_pos
        
        if x > 30 or y > 30 or x < 0 or y < 0:
            draw_gameover(screen)
            pg.display.update()
            gameover = True
    
        if x != food_pos[0] or y != food_pos[1]:
            pg.draw.rect(screen, (255,255,255), pg.Rect(cst[0]*18 + 1, cst[1]*18 + 31, 18-1, 18-1), 0)
            snake_pixels.pop(0)
            
            if [x, y] in snake_pixels:
                draw_gameover(screen)
                pg.display.update()
                gameover = True
            
            snake_pixels.append([x, y])
        else:
            score += 1 
            draw_score(screen, score)
            snake_pixels.append([x, y])
            food_pos = food(screen, snake_pixels)

        time.sleep(0.1)
        
        snake(screen, snake_pixels)
        draw_screen(screen)
        pg.display.update()
    
main()
pg.quit()