# Mazer

A fun little maze based game where the player has to navigate their way around a maze and visit every blank space on the game board in order to complete a level. The player can only choose the direction in which they wish to travel, they will continue to travel in this direction continuously until they hit an edge, this is where the challenge in the game stems. 

I have constructed a total of 5 levels in varying difficulty for the user to play through. I would like to build an in-game level creator so the user can make their own new levels but before I can do that I would prefer to learn enough to be able to make it a GUI rather than command lines.

Creating new levels for the game still remains relatively easy by altering the code:
Simply fork the repo,
add new entries to the set_level method in the game class,
the dictionaries in this method store the co-ordinates of both the obstacles positions and the player's start position and also the estimated minimum number of moves (to generate a score for the user) it takes to beat the level, also remember to change line 210 to match the total number of levels you have if you've added more.

My main reason for creating the game was to try to learn more about object-oriented structure. The key objects of the program are seperated into classes and the classes are stored in individual .py files since refactor.

## Quick-Start Guide

1. Clone the repository

    `https://github.com/Tomgarh/MAZER-GAME.git`

3. Install the requirements

    `pip install -r requirements.txt`

4. Run the main file

    `python3 main.py`

![Mazer](https://github.com/MfonUdoh/Mazer/assets/48888128/cbab65ae-1b89-4618-aa33-0643e792368a)
