import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((200, 200, 200))
circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, width=2)

circle(screen, (255, 0, 0), (200-50, 175-20), 20)
circle(screen, (0, 0, 0), (200-50, 175-20), 20, width=1)
circle(screen, (0, 0, 0), (200-50, 175-20), 10)

circle(screen, (255, 0, 0), (200+50, 175-20), 15)
circle(screen, (0, 0, 0), (200+50, 175-20), 15, width=1)
circle(screen, (0, 0, 0), (200+50, 175-20), 7)

polygon(screen, (0, 0, 0), [(150,200), (150+100,200),
                               (150+100,200 +20), (150,200+20), (150,200)])

polygon(screen, (0, 0, 0), [(110,90), (103,103),
                               (183,153), (190,140), (110,90)])

polygon(screen, (0, 0, 0), [(300,90), (307,103),
                               (227,153), (220,140), (300,90)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()