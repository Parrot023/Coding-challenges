# Conways famous game of life
# The rules are simple
# Any live cell with 2 or 3 live neighbours survive to the next generation
# Any dead cell with exactly 3 live neighbours are born into the next generation
# Under all other circumstances the cells either die or is not born
# Lets the games begin

# By the way:
# You could probably how done this in some smarter or more efficient way
# Bot yolo i got it done

import random
import time
import os

height = 20
width = 20
spawnrate = 20

# Fnuction used to generate the play board
def generate_board(rows, cols):

    board = []
    board2 = []

    for y in range(rows):
        board.append([])
        board2.append([])
        for x in range(cols):
            if random.randint(0,100) < spawnrate:
                board[y].append(1)
                board2[y].append(1)

            else:
                board[y].append(0)
                board2[y].append(1)



    return board, board2

# Return a cells live neighbours
def live_neighbours(x,y):

    live_neighbours = 0

    for x2 in range(x-1, x+2):
        for y2 in range(y-1, y+2):
            try:
                live_neighbours += current_gen[y2][x2]
            except Exception as e:
                pass


    live_neighbours -= current_gen[y][x]

    return live_neighbours

# Prints the board in the terminal
def print_board(board):
    os.system("clear")
    for y in range(len(board)):
        for x in range(len(board[1])):
            if board[y][x] == 0:
                print("□", end = " ")
            else:
                print("■", end = " ")

        print("")

# In python if you says list1 = list2
# you do whats called copy by reference.
# meaning that if you change one the other will change to.
# To avoid this you could say list1 = list2[:].
# But this wont work with a 2d array like i use for the board.
# This function will therefore go through every index in the
# 2d list and copy it over to the other lis
def copy_2d_list(list1, list2):
    for y in range(len(list1)):
        for x in range(len(list1[1])):
            list2[y][x] = list1[y][x]

# Generating the current and next gen 2d arrays
current_gen, next_gen = generate_board(height,width)

# Main loop
while True:
    # Printing the board
    print_board(current_gen)

    # Going through every cell
    for y in range(height):
        for x in range(width):
            neighbours = 0
            # Checks if it at the borders. if at the border DIE
            if (y == 0 or y == height-1 or x == 0 or x == width-1):
                next_gen[y][x] = 0
            else:


                # Get number of live neighbours
                neighbours = live_neighbours(x,y)

                # Going over the rules find the cells state in the next gen
                if (current_gen[y][x] == 1):
                    if neighbours == 2 or neighbours == 3:
                        next_gen[y][x] = 1
                    else:
                        next_gen[y][x] = 0
                else:
                    if neighbours == 3:
                        next_gen[y][x] = 1
                    else:
                        next_gen[y][x] = 0

    # Sets current gen to next gen
    copy_2d_list(next_gen, current_gen)

    # A little delay to controle how fast the hole shabam goes
    time.sleep(0.1)
