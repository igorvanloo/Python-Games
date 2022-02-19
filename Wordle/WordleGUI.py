#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:55:56 2022

@author: igorvanloo
"""

import pygame as pg
import random

def ReadFile(filename): #Create the inital list 
    file = open(filename)
    data = file.readlines()
    file.close()
    datalist = []
    for x in data:
        x = x.rstrip()
        datalist.append(x)
    return datalist

class InitBoard:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 106,169,100
    YELLOW = 210, 176, 55
    GREY = 58,58,60
    DARK_GREY = 105, 105, 105
    BACKGRD_CLR = BLACK
    SQUARE_SIZE = 50
    PADDING = 50
    NUMBER_PADDING = 60
    GAP = 5
    GAME_PADDING = PADDING + 2*(SQUARE_SIZE + GAP) + 25
    BOTTOM_GAP = PADDING + 6*(SQUARE_SIZE+GAP)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pg.font.SysFont("comicsans", 40)
        self.window = pg.display.set_mode((width, height))
        self.answers = ReadFile("possible answers.txt")
        self.guesses = ReadFile("possible guesses.txt")
        self.correct_pos_ltr = []
        self.correct_ltr = [] 
        self.wrong_ltr = []
        self.row = 0
        self.column = -1
        self.board_rep = [[" " for i in range(0,5)] for j in range(0,6)]
        pg.display.set_caption("Wordle Game")

def DrawBoard(board):
    board.window.fill(board.BACKGRD_CLR)
    for x in range(0,5):
        for y in range(0,6):
            pg.draw.rect(board.window, board.GREY, pg.Rect(board.GAME_PADDING + x*(board.SQUARE_SIZE + board.GAP), board.PADDING + y*(board.SQUARE_SIZE + board.GAP), 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 1)
    pg.display.update()

def DrawAlaphabet(board, correct_pos_ltr, correct_ltr, wrong_ltr):
    row1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
    row2 = ["a","s","d","f","g","h","j","k","l"]
    row3 = ["z","x","c","v","b","n","m"]
    for x in row1:
        if x in correct_pos_ltr:
            pg.draw.rect(board.window, board.GREEN, pg.Rect(board.PADDING + row1.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        elif x in correct_ltr:
            pg.draw.rect(board.window, board.YELLOW, pg.Rect(board.PADDING + row1.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        elif x in wrong_ltr:
            pg.draw.rect(board.window, board.GREY, pg.Rect(board.PADDING + row1.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING + board.BOTTOM_GAP, 
                                                     board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        else:
            pg.draw.rect(board.window, board.DARK_GREY, pg.Rect(board.PADDING + row1.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING + board.BOTTOM_GAP, 
                                                       board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        text = board.font.render(str(x), True, board.WHITE)
        board.window.blit(text, (board.NUMBER_PADDING + row1.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING - 10 + board.BOTTOM_GAP))

    for x in row2:
        if x in correct_pos_ltr:
            pg.draw.rect(board.window, board.GREEN, pg.Rect(board.PADDING + 25 + row2.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*2 + board.GAP + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        elif x in correct_ltr:
            pg.draw.rect(board.window, board.YELLOW, pg.Rect(board.PADDING + 25 + row2.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*2 + board.GAP + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        elif x in wrong_ltr:
            pg.draw.rect(board.window, board.GREY, pg.Rect(board.PADDING + 25 + row2.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*2 + board.GAP + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        else:
            pg.draw.rect(board.window, board.DARK_GREY, pg.Rect(board.PADDING + 25 + row2.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*2 + board.GAP + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        text = board.font.render(str(x), True, board.WHITE)
        board.window.blit(text, (board.NUMBER_PADDING + 25 + row2.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*2 - 10 + board.GAP + board.BOTTOM_GAP))
        
    for x in row3:
        if x in correct_pos_ltr:
            pg.draw.rect(board.window, board.GREEN, pg.Rect(board.PADDING*2 + 30 + row3.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*3 + board.GAP*2 + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        elif x in correct_ltr:
            pg.draw.rect(board.window, board.YELLOW, pg.Rect(board.PADDING*2 + 30 + row3.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*3 + board.GAP*2 + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        elif x in wrong_ltr:
            pg.draw.rect(board.window, board.GREY, pg.Rect(board.PADDING*2 + 30 + row3.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*3 + board.GAP*2 + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        else:
            pg.draw.rect(board.window, board.DARK_GREY, pg.Rect(board.PADDING*2 + 30 + row3.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*3 + board.GAP*2 + board.BOTTOM_GAP, 
                                                           board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
        text = board.font.render(str(x), True, board.WHITE)
        board.window.blit(text, (board.NUMBER_PADDING + board.PADDING + 30 + row3.index(x)*(board.SQUARE_SIZE + board.GAP), board.PADDING*3 - 10+ board.GAP*2 + board.BOTTOM_GAP))

            
def DrawGuess(board, letter, row, column):
    board.board_rep[row][column] = letter
    text = board.font.render(str(letter), True, board.WHITE)
    board.window.blit(text, (board.GAME_PADDING + 10 + column*(board.SQUARE_SIZE + board.GAP), board.PADDING - 10 + row*(board.SQUARE_SIZE + board.GAP)))
    pg.display.update()
    
def DeleteGuess(board, row, column):
    board.board_rep[row][column] = " "
    pg.draw.rect(board.window, board.BLACK, pg.Rect(board.GAME_PADDING + column*(board.SQUARE_SIZE + board.GAP), 
                board.PADDING + row*(board.SQUARE_SIZE + board.GAP), board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
    pg.display.update()
    pg.draw.rect(board.window, board.GREY, pg.Rect(board.GAME_PADDING + column*(board.SQUARE_SIZE + board.GAP), 
                board.PADDING + row*(board.SQUARE_SIZE + board.GAP), board.SQUARE_SIZE, board.SQUARE_SIZE), 1)
    pg.display.update()

def ProvideHint(board, answer, guess, row):
    temp_answer = [x for x in answer]
    for x in range(len(guess)):
        text = board.font.render(str(guess[x]), True, board.WHITE)
        if guess[x] == temp_answer[x]:
            board.correct_pos_ltr.append(guess[x])
            pos = temp_answer.index(guess[x])
            temp_answer.insert(pos, "-")
            temp_answer.pop(pos + 1)
            pg.draw.rect(board.window, board.GREEN, pg.Rect(board.GAME_PADDING + x*(board.SQUARE_SIZE + board.GAP), 
                        board.PADDING + row*(board.SQUARE_SIZE + board.GAP), board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
            board.window.blit(text, (board.GAME_PADDING + 10 + x*(board.SQUARE_SIZE + board.GAP), board.PADDING - 10 + row*(board.SQUARE_SIZE + board.GAP)))
            pg.display.update()
        elif guess[x] in temp_answer:
            board.correct_ltr.append(guess[x])
            pos = temp_answer.index(guess[x])
            if guess[pos] != temp_answer[pos]:
                temp_answer.insert(pos, "-")
                temp_answer.pop(pos + 1)
                pg.draw.rect(board.window, board.YELLOW, pg.Rect(board.GAME_PADDING + x*(board.SQUARE_SIZE + board.GAP), 
                            board.PADDING + row*(board.SQUARE_SIZE + board.GAP), board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
            else:
                pg.draw.rect(board.window, board.GREY, pg.Rect(board.GAME_PADDING + x*(board.SQUARE_SIZE + board.GAP), 
                            board.PADDING + row*(board.SQUARE_SIZE + board.GAP), board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
            board.window.blit(text, (board.GAME_PADDING + 10 + x*(board.SQUARE_SIZE + board.GAP), board.PADDING - 10 + row*(board.SQUARE_SIZE + board.GAP)))
            pg.display.update()
        else:
            board.wrong_ltr.append(guess[x])
            pg.draw.rect(board.window, board.GREY, pg.Rect(board.GAME_PADDING + x*(board.SQUARE_SIZE + board.GAP), 
                        board.PADDING + row*(board.SQUARE_SIZE + board.GAP), board.SQUARE_SIZE, board.SQUARE_SIZE), 0)
            board.window.blit(text, (board.GAME_PADDING + 10 + x*(board.SQUARE_SIZE + board.GAP), board.PADDING - 10 + row*(board.SQUARE_SIZE + board.GAP)))
            pg.display.update()
    if guess == answer and row!= 6:
        GameOver(board, guess, answer)
    pg.display.update()

def GameOver(board, guess, answer):
    if guess == answer:
        text = board.font.render("You Win!", True, board.WHITE)
        board.window.blit(text, (board.GAME_PADDING + (board.SQUARE_SIZE), board.BOTTOM_GAP - 5))
        print("You win!")
    else:
        text = board.font.render("You Lose :(", True, board.WHITE)
        board.window.blit(text, (board.GAME_PADDING + (board.SQUARE_SIZE), board.BOTTOM_GAP - 5))
        print("You lose, answer was", ''.join(answer))

def NextGuessAlgo():
    pass

def main():
    pg.init()
    running = True
    clock = pg.time.Clock()
    board = InitBoard(650, 600)
    answer = list(random.choice(board.answers))
    DrawBoard(board)
    DrawAlaphabet(board, board.correct_pos_ltr, board.correct_ltr, board.wrong_ltr)
    while running:
        clock.tick(60)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    guess = board.board_rep[board.row]
                    if (board.column == 4 and len(guess) == 5 and (''.join(guess) in board.guesses)):
                        ProvideHint(board, answer, guess, board.row)
                        DrawAlaphabet(board, board.correct_pos_ltr, board.correct_ltr, board.wrong_ltr)
                        board.row += 1
                        if board.row == 6:
                            GameOver(board, guess, answer)
                        board.column = -1
                        pg.display.update()
                    else:
                        print("Guess is not a word in allowable list")
                elif event.key == pg.K_BACKSPACE:
                    if board.column != -1:
                        DeleteGuess(board, board.row, board.column)
                        board.column -= 1
                        pg.display.update()
                elif pg.K_a <= event.key <= pg.K_z:
                    if board.column + 1 != 5:
                        board.column += 1
                        DrawGuess(board, pg.key.name(event.key), board.row, board.column)
                        pg.display.update()
                elif event.key == pg.SPACE:
                    NextGuessAlgo()
            
    pg.quit()

if __name__ == "__main__":
    main()