# Python Games

Just some simple python games I created to learn how to use Pygame. All games need the [Pygame Module](https://www.pygame.org/wiki/GettingStarted) to be used. Additional modules will be stated under the respective games.

### Sudoku

The Sudoku is fully finished. 
You can play normal sudoku, with all the same game functions, except indexing squares (Small notes).
Additionally by pressing "spacebar" the program will show you a visualization of the [Backtracking Algorithm](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms)

You can see my own code of the backtracking algorithm [here](https://github.com/igorvanloo/Project-Euler-Explained/blob/main/Finished%20Problems/pe00096%20-%20Sudoku.py), it is a part of my Project Euler Repository. This is much more technically difficult than creating the game in my opinion.

### Mr Pong

Mr Pong is fully finished.
You can play normal Mr Pong, with all the same game functions. Future project will be to create an AI to play against.

### Snake

Snake is fully finished. *Requires random, and time module*

You can play normal snake, with all the same game functions.
Additionally by pressing "spacebar" the program will begin auto "solving" the snake game, that is it will perform the guarenteed winning strategy using a [Hamiltonian Circuit](https://en.wikipedia.org/wiki/Hamiltonian_path). This is absoulutely not the most efficient strategy, perhaps a future project?

### Tic-Tac-Toe

Not fully complete.

You can play regularly however it is not very pretty. I have plans to make an AI so that you will never be able to win against the computer, this is a future project.

## What I learnt/Recommended Order

1. **Tic-Tac-Toe**
  * Good beginner project to learn how PyGame works, initializing some shapes, and how to put them on the board.
  * Teachs you how to use the mouse position
2. **Sudoku**
  * Simple as well to create the game, in a sense a more complex version of Tic-Tac-Toe
  * How to delete numbers(Shapes) that you have added to the screen (Not as easy as it sounds!)
  * If you are going to do the backtracking visualization this project will be much harder
3. **Snake**
  * There is now constant movement of your shapes, which is a step up from Sudoku
  * Requires some collision mechanics to eat food, and grow the snake.
  * If you want to make the optimal strategy as well, it is not much more difficult and I recommend it as it is the simplest AI I can think of
5. **Mr Pong**
  * Many shapes that require movement from command, and constant movement of ball, a step up from Snake
  * Requires harder collision mechanics between the ball and wall/paddles
