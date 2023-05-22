import pygame
from sys import exit
pygame.init()
## 500x500 for checkerboard background 
score = 0;
HighScore = 0;
screen = pygame.display.set_mode((650, 650))
pygame.display.set_caption("Snake Game")
game_surface = pygame.image.load("BackGrounds/CheckerBoard.png")
Font = pygame.font.SysFont("comicsansms", 30)
Outer1_Surface = pygame.Surface((650, 100))
Outer2_Surface = pygame.Surface((650, 650))
Outer1_Surface.fill((20, 170, 245))
Outer2_Surface.fill((150, 195, 235))
clock = pygame.time.Clock()
Font_surface = Font.render(f"Score: {score}", True, "black")
Highscore_surface = Font.render(f"High Score: {HighScore}", True, "black")
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(Outer2_Surface,(0,0))
    screen.blit(Outer1_Surface,(0,0))
    screen.blit(game_surface,(75, 125))
    screen.blit(Font_surface,(10,10))
    screen.blit(Highscore_surface,(270, 10))
    pygame.display.update()
    clock.tick(60)

