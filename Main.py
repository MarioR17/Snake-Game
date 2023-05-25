import pygame
import random

from sys import exit
pygame.init()
## 500x500 for checkerboard background 
score = 0;
HighScore = 0;
screen = pygame.display.set_mode((650, 650))
pygame.display.set_caption("Snake Game")
game_surface = pygame.image.load("BackGrounds/CheckerBoard.png").convert()
Font = pygame.font.SysFont("comicsansms", 30)
Outer1_Surface = pygame.Surface((650, 100))
Outer2_Surface = pygame.Surface((650, 650))
Outer1_Surface.fill((20, 170, 245))
Outer2_Surface.fill((150, 195, 235))
clock = pygame.time.Clock()
Font_surface = Font.render(f"Score: {score}", True, "black")
Highscore_surface = Font.render(f"High Score: {HighScore}", True, "black")

coordinates = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450]

rect_width = 50
rect_height = 50
rect_color = (255, 0, 0)  # Red color represented by RGB values
rect_x = random.choice(coordinates)
rect_y = random.choice(coordinates)
x_cor = 250
y_cor = 250
space = 50

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x_cor -= space

    if keys[pygame.K_RIGHT]:
        x_cor += space

    if keys[pygame.K_UP]:
        y_cor -= space

    if keys[pygame.K_DOWN]:
        y_cor += space

    screen.fill([255,255,255])
    screen.blit(Outer2_Surface,(0,0))
    screen.blit(Outer1_Surface,(0,0))
    screen.blit(game_surface,(75, 125))
    screen.blit(Font_surface,(10,10))
    screen.blit(Highscore_surface,(270, 10))
    pygame.draw.rect(game_surface, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect(game_surface, (0, 0, 255), (x_cor, y_cor, rect_width, rect_height))
    pygame.display.update()
    clock.tick(16)

