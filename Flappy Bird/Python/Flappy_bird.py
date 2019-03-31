#1. install pygame ✔️
#2. import pygame ✔️
#3. make square appear on screen. ✔️
#4. make square react to player hitting space bar. ✔️
#5. make moving obstacles. ✔️
#6. make player die when hitting obstacle ✔️
#7. make everything look pretty.
#8. upload to github


#pygame introduction
#https://www.pygame.org/docs/tut/PygameIntro.html


import pygame

import Objects

pygame.init()

width = 400
height = 600
count = 0

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
info = pygame.display.Info()

bird = Objects.Bird(200, 200, 20, 20, screen)
obstacle = Objects.Obstacle(width-50,height-250, 250, 50, screen)

gamestate = 1

def game(gamestate):

    score = 0

    while gamestate == 1:

        screen.fill((44, 108, 238))

        bird.show()
        bird.update()
        gamestate = bird.encounter(obstacle)

        obstacle.show()
        score = score + obstacle.update()


        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gamestate = 0

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_SPACE:

                    bird.jump()

        print(score)
        clock.tick(60)


game(gamestate)






pygame.quit()
quit()
