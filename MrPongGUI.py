#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:53:25 2021

@author: igorvanloo
"""

import pygame as pg

def draw_score(screen, score_p1, score_p2):
    pg.draw.rect(screen, (0,0,0), pg.Rect(0, 0, 600, 30), 0)
    fnt = pg.font.SysFont("comicsans", 40)
    text = fnt.render(str(score_p1) + ":" + str(score_p2), True, (255, 255, 255))
    screen.blit(text, (280, 0))

def draw_screen(screen):
    pg.draw.rect(screen, (0,0,0), (0,31,600,330),0)
    pg.draw.line(screen, pg.Color(255,255,255), (0, 30), (600, 30), 1) #Top border Line
    pg.draw.line(screen, pg.Color(255,255,255), (20, 30), (20, 330), 1) #side Lines
    pg.draw.line(screen, pg.Color(255,255,255), (580, 30), (580, 330), 1) #side Lines
    pg.draw.line(screen, pg.Color(255,255,255), (300, 30), (300, 330), 2) #middle line

def draw_player_1_paddle(screen, p1yp):
    
    width = 10
    height = 40
    
    pg.draw.rect(screen, (0,0,0), pg.Rect(30, 31, width, 300), 0) #Draw black column
    pg.draw.rect(screen, (255,255,255), pg.Rect(30, p1yp, width, height), 0) #draw paddle

def draw_player_2_paddle(screen, p2yp):
    width = 10
    height = 40
    
    pg.draw.rect(screen, (0,0,0), pg.Rect(560, 31, width, 300), 0) #Draw black column
    pg.draw.rect(screen, (255,255,255), pg.Rect(560, p2yp, width, height), 0)

def draw_ball(screen, btl):
    
    x,y = btl
    width = 10
    height = 10
    
    pg.draw.rect(screen, (255,255,255), pg.Rect(x, y, width, height), 0) #Draw ball
    
def main():
    
    pg.init()
    screen_size = 600, 330
    screen = pg.display.set_mode(screen_size)
    
    score_p1 = 0
    score_p2 = 0
    
    screen.fill(pg.Color("black"))
    
    x_pos = 0
    y_pos = 0
    ball_x = 295
    ball_y = 170
    btl = [ball_x, ball_y]
    
    p1yp = 165 #Player 1 y position
    p2yp = 165 #Player 2 y position
    paddle_speed = 10
    
    draw_screen(screen)
    draw_score(screen, score_p1, score_p2)
    draw_player_1_paddle(screen, p1yp)
    draw_player_2_paddle(screen, p2yp)
    draw_ball(screen, btl)
    
    pg.display.update()
    game_running = True
    
    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False
                
            if event.type == pg.KEYDOWN:   #Player 1 commands
                if event.key == pg.K_w:
                    p1yp += -paddle_speed
                if event.key == pg.K_s:
                    p1yp += paddle_speed
                    
                if event.key == pg.K_UP: #Player 2 commands
                    p2yp += -paddle_speed
                if event.key == pg.K_DOWN:
                    p2yp += paddle_speed
                    
                if event.key == pg.K_p: #Start ball movement
                    
                    x_pos = 0.2
                    y_pos = 0.2
            
        if p1yp < 30:
            p1yp = 30
        if p1yp > 290:
            p1yp = 290
        
        if p2yp < 30:
            p2yp = 30
        if p2yp > 290:
            p2yp = 290
        
        ball_x += x_pos
        ball_y += y_pos
        
        if ball_x <= 40 and p1yp - 5 <= ball_y <= p1yp + 45: #Then the ball has collided with paddle 1
            x_pos *= -1.1
            
        if ball_x >= 550 and p2yp - 5 <= ball_y <= p2yp + 45: #Then the ball has collided with paddle 2
            x_pos *= -1.1
        
        if ball_y <= 31 or ball_y >= 325: #Wall collision
            y_pos *= -1
        
        if ball_x < 29 or ball_x > 551:
            
            if ball_x < 25:
                score_p2 += 1
                draw_score(screen, score_p1, score_p2)
                
                x_pos = 0
                y_pos = 0
                ball_x = 295
                ball_y = 170
                btl = [ball_x, ball_y]
                
                p1yp = 165
                p2yp = 165 
                paddle_speed = 10
                
            if ball_x > 555:
                score_p1 += 1
                draw_score(screen, score_p1, score_p2)
                
                x_pos = 0
                y_pos = 0
                ball_x = 295
                ball_y = 170
                btl = [ball_x, ball_y]
                
                p1yp = 165
                p2yp = 165 
                paddle_speed = 10            
        
        draw_screen(screen)
        draw_player_1_paddle(screen, p1yp)
        draw_player_2_paddle(screen, p2yp)
        draw_ball(screen, [ball_x, ball_y])
        pg.display.update()
                
main()
pg.quit()