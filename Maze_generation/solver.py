

"""
Welcome to my I did not know how else to do it, and it works ALGORITHM
this algorithm will try to guide little billy (The black square) through the maze
the algorithm will every step of the way pick the unvisited neighbour that will get billy the closest to the target
kind of like always going north if you are lost

PLAN:
Start with upper left corner cell
will there is still unvisited neighbours
go to the one that will get you closer
in terms of distance to the target
keep  recusively till you have reach the target
"""

import random
import math
import sys

import pygame
import pickle

# Setting the recursion limit to handle the many recursions
sys.setrecursionlimit(10**6)

# Opening the file conatining the maze
file = open('maze.pickle', 'rb')

# Loading in the maze genrerating by maze.py
walls = pickle.load(file)

# Setting some parameters
WIDTH = len(walls[0])
HEIGHT = len(walls)
SCREEN_WIDTH = WIDTH*10
SCREEN_HEIGHT = HEIGHT*10
BLACK = (0,0,0)
WHITE = (255,255,255)

# y, x
TARGET = [HEIGHT - 1, WIDTH - 1]


# Player position
p_pos = [0,0]

# The players trail
trail = []

def generate_arrays(rows, cols):

    """
    Function to generate an array keeping track of visited cells
    """

    board = []

    for y in range(cols):
        board.append([])
        for x in range(rows):
            board[y].append(0)

    return board

board = generate_arrays(WIDTH, HEIGHT)


def draw_player(pos):

    """
    Function to draw the player and his trail
    """

    # Drawing trail
    for t in trail:

        pygame.draw.rect(
            screen,
            (255,0,0),
            [
                t[1]*int(SCREEN_WIDTH/WIDTH),
                t[0]*int(SCREEN_HEIGHT/HEIGHT),
                int(SCREEN_WIDTH/WIDTH),
                int(SCREEN_HEIGHT/HEIGHT)
            ]
        )

    # Drawing player
    pygame.draw.rect(
        screen,
        BLACK,
        [
            pos[1]*int(SCREEN_WIDTH/WIDTH),
            pos[0]*int(SCREEN_HEIGHT/HEIGHT),
            int(SCREEN_WIDTH/WIDTH),
            int(SCREEN_HEIGHT/HEIGHT)
        ]
    )

def draw_grid(walls):

    """
    Function to draw the walls using pygame
    """

    for y in range(HEIGHT):
        for x in range(WIDTH):

            top_corner = {
                "x": x*int(SCREEN_WIDTH/WIDTH),
                "y": y*int(SCREEN_HEIGHT/HEIGHT),
            }

            x_offset = int(SCREEN_WIDTH/WIDTH)
            y_offset = int(SCREEN_HEIGHT/HEIGHT)

            if walls[y][x][0]:
                pygame.draw.line(screen, BLACK, [top_corner["x"], top_corner["y"]], [top_corner["x"] + x_offset, top_corner["y"]])
            if walls[y][x][1]:
                pygame.draw.line(screen, BLACK, [top_corner["x"], top_corner["y"]], [top_corner["x"], top_corner["y"] + y_offset])

def get_neighbours(pos):

    """
    Function that returns a given cells number of non visited neighbours
    """

    final_neighbours = []

    # Going over all 9 cells around the cell including the cell itself
    # the cell itself wont be counted as it is visited
    for y2 in range(pos[0] - 1, pos[0] + 2):
        for x2 in range(pos[1] -1, pos[1] + 2):

            # Making sure that the cells is within the boundaries of the array
            if x2 >= 0 and x2 <= WIDTH - 1 and y2 >= 0 and y2 <= HEIGHT - 1:
                # Checking if the cell has been visited
                if board[y2][x2] != 1:
                    #checking if it is one of the 4 neighbours
                    if x2 == pos[1] or y2 == pos[0]:

                        # Checking if theres a wall between the cell and the neighbour
                        # Maybe this could be done smarter but i cant seem to find another solution
                        if x2 > pos[1] and walls[y2][x2][1] != 1:
                            final_neighbours.append((WIDTH*y2)+x2)

                        if x2 < pos[1] and walls[pos[0]][pos[1]][1] != 1:
                            final_neighbours.append((WIDTH*y2)+x2)

                        if y2 > pos[0] and walls[y2][x2][0]!= 1:
                            final_neighbours.append((WIDTH*y2)+x2)

                        if y2 < pos[0] and walls[pos[0]][pos[1]][0]!= 1:
                            final_neighbours.append((WIDTH*y2)+x2)

    return final_neighbours


def solve(n):

    """
    This is the function which will run recursively to find a path through the maze
    """

    # y and x
    pos = [int(n / WIDTH), int(n % WIDTH)]

    # Setting the cell as visited
    board[pos[0]][pos[1]] = 1

    # Setting the player pos to this cell
    p_pos[0], p_pos[1] = pos[0], pos[1]

    # Adding cell to trail
    trail.append(pos)

    #Updating screen
    screen.fill((255,255,255))

    draw_player(p_pos)
    draw_grid(walls)

    pygame.display.flip()

    # Check if cell is at target
    if pos[0] == TARGET[0] and pos[1] == TARGET[1]:
        print("Done")
        print("pos {}".format(pos))
        return 1

    # Otherwise go through all the neighbours choosing the one which will get you the closesst to the target
    while len(get_neighbours([pos[0], pos[1]])) > 0:

        smallest_d = 1000
        best_neighbour = 0

        for i in get_neighbours([pos[0], pos[1]]):

            i_pos = [int(n / WIDTH), int(n % WIDTH)]
            X,Y = abs(i_pos[1] - pos[1]), abs(i_pos[0] - pos[0])
            D = math.sqrt(X**2 + Y**2)

            if D < smallest_d:
                smallest_d = D
                best_neighbour = i

        if solve(i) == 1:
            return 1

    # Removing cell from trail if backtracking
    trail.pop(trail.index(pos))


# Initialyzing pygame
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("MAZE GENERATION ALGORITHM")

screen.fill((255,255,255))

print("You can do it billy")

solve(0)

print("Good job billy")

show = True

while show:

    """
    loop to show maze with path to target
    """

    screen.fill((255,255,255))

    draw_player(p_pos)
    draw_grid(walls)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close

            # Saves the maze with path
            pygame.image.save(screen, "path.png")

            # Stops the loop
            show = False

    # Updates screen
    pygame.display.flip()

pygame.quit()
