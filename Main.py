import pygame
from sys import exit
<<<<<<< HEAD
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)
pygame.quit()
exit()
=======

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)


>>>>>>> f47d3c1b2af4ac9e9b716019e4b6ead8784277fb
