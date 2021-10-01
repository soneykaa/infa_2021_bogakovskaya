import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))
# закрашиваем фон
screen.fill((230, 230, 230))
rect(screen, (250, 250, 250), (0, 500, 794, 1123-500))
# Рисуем Иглу
ellipse(screen, (230, 230, 230), (50, 460, 400, 360))
ellipse(screen, (0, 0, 0), (50, 460, 400, 360), width=2)
# Вертикальные полосочки
ellipse(screen, (0, 0, 0), (50, 460, 400, 800), width=2)
ellipse(screen, (0, 0, 0), (50, 460, 400, 2400), width=2)
ellipse(screen, (0, 0, 0), (50, 460, 400, 7200), width=2)
# Горизонтальные полосочки
line(screen, (0, 0, 0), (50, 630), (450, 630), width=1)
line(screen, (0, 0, 0), (58, 590), (442, 590), width=1)
line(screen, (0, 0, 0), (80, 550), (420, 550), width=1)
line(screen, (0, 0, 0), (115, 510), (385, 510), width=1)
line(screen, (0, 0, 0), (185, 470), (315, 470), width=1)
# Скрашиваем уродство белым прямоугольником
rect(screen, (250, 250, 250), (0, 630, 794, 800))

# тело и голова
ellipse(screen, (227, 222, 219), (561, 603, 696-561, 692-603))
ellipse(screen, (145, 124, 111), (553, 652, 710-553, (806-652)*2))
rect(screen, (250, 250, 250), (550, 800, 200, 200))
ellipse(screen, (172, 157, 147), (577, 615, 679-577, 683-615))
ellipse(screen, (227, 219, 219), (595, 629, 664-595, 676-629))
# лицо
line(screen, (0, 0, 0), (602, 641), (618, 650), width=1)
line(screen, (0, 0, 0), (655, 646), (637, 650), width=1)
polygon(screen, (255, 0, 0), [(649, 668), (638, 663), (614, 664)])
# руки
ellipse(screen, (145, 124, 111), (520, 696, 600-520, 723-696))
ellipse(screen, (145, 124, 111), (668, 696, 600-520, 723-696))
# ноги
ellipse(screen, (145, 124, 111), (577, 776, 617-577, 841-776))
ellipse(screen, (145, 124, 111), (646, 776, 617-577, 841-776))
ellipse(screen, (145, 124, 111), (563, 822, 615-563, 845-822))
ellipse(screen, (145, 124, 111), (653, 822, 615-563, 845-822))
# шмотки
rect(screen, (108, 93, 83), (607, 682, 644-607, 786-682))
rect(screen, (108, 93, 83), (555, 790, 708-555, 806-790))
# палка
line(screen, (0, 0, 0), (528, 610), (534, 824), width=1)

#тело кота
ellipse(screen, (204, 204, 204), (118, 843, 262-118, 880-843))
ellipse(screen, (204, 204, 204), (72, 856, 162-72, 873-856))
ellipse(screen, (204, 204, 204), (147, 868, 171-147, 907-868))
ellipse(screen, (204, 204, 204), (242, 856, 162-72, 873-856))
ellipse(screen, (204, 204, 204), (219, 868, 171-147, 907-868))
# голова кота
circle(screen, (204, 204, 204), (140, 833), 20)
circle(screen, (255, 255, 255), (142, 831), 7)
circle(screen, (0, 0, 0), (142+6, 831), 3)
circle(screen, (255, 255, 255), (126, 827), 7)
circle(screen, (0, 0, 0), (126+6, 827), 3)
polygon(screen, (204, 204, 204), [(133, 821-5), (135, 812-5), (141, 819-5),
                              (153, 819-5), (158, 815-5), (158, 830-5), (135, 822-5)])

font = pygame.font.SysFont(None, 24)
img = font.render('Это котик с рыбой', True, (0,0,0))
screen.blit(img, (20, 880))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()