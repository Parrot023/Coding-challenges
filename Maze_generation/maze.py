
# DEPTH-FIRST SEARCH MAZE GENERATION

# ALGORITHM
# Choose a random cell mark this cell as having been visited
# Choose a random neighbouring cell that have not been visited
# If all neighbouring cells have been visited backtrack
# If not Remove the wall between these two cells and go on
# If we backtrack all the way to the begining cell we have visited every cell on the grid

# Refer to this wikipedia article for more detail on the algorithm
# Under Depth-first search
# https://en.wikipedia.org/wiki/Maze_generation_algorithm

import random
import os
import sys
import pygame

sys.setrecursionlimit(10**6)

WIDTH = 200
HEIGHT = 120
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)

def generate_arrays(rows, cols):

    """
    Function to generate arrays for visited cells and walls
    """

    board = []
    walls = []

    for y in range(cols):
        board.append([])
        walls.append([])
        for x in range(rows):
            board[y].append(0)
            walls[y].append([])
            for i in range(2):
                walls[y][x].append(1)

    return board, walls

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
                        final_neighbours.append((WIDTH*y2)+x2)

    return final_neighbours

def solve(n):

    # Calculates pos of cell by n
    # y and x
    pos = [int(n / WIDTH), int(n % WIDTH)]

    # Setting current cell as having been visited
    board[pos[0]][pos[1]] = 1


    # Looping as long as there is still unvisited neighbours
    while len(get_neighbours([pos[0],pos[1]])) > 0:

        # Choosing a random unvisited neighbour
        neighbour = random.choice(get_neighbours([pos[0],pos[1]]))

        # Chosen neighbours y and x
        # yes y and x because when iterating over a 2d
        # array y is the outer loop and therefore this order makes sense
        neighbour_pos = [int((neighbour) / WIDTH), int((neighbour) % WIDTH)]

        # if moving down upper wall of neighbour should be removed
        if neighbour_pos[0] > pos[0]:
            walls[neighbour_pos[0]][neighbour_pos[1]][0] = 0


        # If going left, right wall of cell should be removed
        if neighbour_pos[1] < pos[1]:
            walls[pos[0]][pos[1]][1] = 0


        # If going up top wall of cell should be removed
        if neighbour_pos[0] < pos[0]:
            walls[pos[0]][pos[1]][0] = 0

        # If going right, left wall of neighbour should be removed
        if neighbour_pos[1] > pos[1]:
            walls[neighbour_pos[0]][neighbour_pos[1]][1] = 0

        # Going to the neighbour
        solve(neighbour)

    # return 0 when no more neighbours
    return 0

board, walls = generate_arrays(WIDTH, HEIGHT)

# Starting at a random neighbour
solve(random.randint(0,8))

# Initialyzing pygame
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("MAZE GENERATION ALGORITHM")

show = True

while show:

    """
    loop to show generated maze
    """

    screen.fill((255,255,255))

    draw_grid(walls)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            pygame.image.save(screen, "maze.png")
            show = False

    pygame.display.flip()

pygame.quit()

print("Here you go i have saved the maze for you as: maze.png")
