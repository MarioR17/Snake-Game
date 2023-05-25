import pygame
import random

from sys import exit
pygame.init()
## 500x500 for checkerboard background 
score = 0;
HighScore = 0;
screen = pygame.display.set_mode((650, 650))
pygame.display.set_caption("Snake Game")
game_surface = pygame.image.load("BackGrounds/Checker.png").convert()
Font = pygame.font.SysFont("comicsansms", 30)
Outer1_Surface = pygame.Surface((650, 100))
Outer2_Surface = pygame.Surface((650, 650))
Outer1_Surface.fill((20, 170, 245))
Outer2_Surface.fill((150, 195, 235))
clock = pygame.time.Clock()
Font_surface = Font.render(f"Score: {score}", True, "black")
Highscore_surface = Font.render(f"High Score: {HighScore}", True, "black")

coordinates = []
for i in range(0, 480, 20):
    coordinates.append(i)

rect_width = 20
rect_height = 20
rect_color = (255, 0, 0)  # Red color represented by RGB values
rect_x = random.choice(coordinates)
rect_y = random.choice(coordinates)
x_cor = 240
y_cor = 240
space = 20

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
    pygame.draw.rect(screen, rect_color, (rect_x + 75, rect_y + 125, rect_width, rect_height))
    pygame.draw.rect(screen, (0, 0, 255), (x_cor + 75, y_cor + 125, rect_width, rect_height))
    pygame.display.update()
    clock.tick(7)

