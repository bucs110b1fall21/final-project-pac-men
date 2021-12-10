:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
### << 1, 2021 >>
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

<< [https://github.com/bucs110b1fall21/final-project-pac-men](#) >>

<< [link to demo presentation slides](#) >>

### Team: << Pac-Men >>
#### << Jason Lin, Axin Li, Nicholas Tavormina >>

***

## Project Description *(Software Lead)*
<< Give an overview of your project >>

***    

## User Interface Design *(Front End Specialist)*
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries 
    Pygame: https://www.pygame.org/docs/
    Set of modules to write, design, and display games within python. Backnbone of most of this project

    Pygame.math: https://www.pygame.org/docs/ref/math.html
    Pygame math is a vector module for pygame classes. I use in it this project in order to create position vectors (grid based and pixel based) for the ghosts and pacman.

    Sys: https://docs.python.org/3/library/sys.html
    Library of variuous functions and functions to use in python. Used only in this project to determine the font of the game text.

    Random: https://docs.python.org/3/library/random.html
    Library of pseudo-random number generators. Used for random Enemy Movement

* Class Interface Design
    * Class Diagram
        * ![class diagram](assets/class_diagram.jpg)
        
* Classes
    Ghosts: Handles the ghosts (pacman enemies). Contains methods to derive a random movement pattern, draw themselves, move (change direction), set color, check for collision, centers the movement on a gridpath, and handles the interchange of a grid positioning system (coordinates) and pixel positioning system on the screen.
    Pacman: Handles the player (pacman himself). Contains methods to move (change direction), draw pacman, check collision, centers the movement on a gridpath, handles the checking for and eating of coins, and handles the interchange of a grid positioning system (coordinates) and pixel positioning system on the screen.

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - << name >>

<< Worked as integration specialist by... >>

### Front End Specialist - << name >>

<< Front-end lead conducted significant research on... >>

### Back End Specialist - << name >>

<< The back end specialist... >>

## Testing *(Software Lead)*
* << Describe your testing strategy for your project. >>
    * << Example >>

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Counter Program  | GUI window appears with count = 0  |          |
|  2  | click count button  | display changes to count = 1 |                 |
etc...
