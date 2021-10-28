import pygame as pg
from pygame.draw import *

pg.init()
FPS = 20
BLACK = (0, 0, 0)

cars_coord = [[40, 555, True, 1, -5],
              [210, 560, True, 1, -8],
              [335, 555, True, 1, -3],
              [440, 570, True, 1, -15],
              [60, 650, False, 2.5, 10],
              [300, 670, True, 2.5, -11]]

def car(x, y, left, k):

    '''
    Синяя машина
    x, y - координаты левого нижнего угла
    left - поворот машины
    k - коэфициент масштабирования
    Рисует по очереди:
    Выхлопную трубу, саму машину, два окна, колеса
    '''

    if left == True:
        ellipse(screen, (0, 0, 0), (x + 77 * k, y - 6 * k, 10 * k, 4 * k))
    else:
        ellipse(screen, (0, 0, 0), (x - 6 * k, y - 6 * k, 10 * k, 4 * k))

    polygon(screen, (36, 204, 242),
            [
                (x, y), (x, y - 15*k), (x + 25*k, y - 15*k),
                (x + 25*k, y - 26*k), (x + 60*k, y - 26*k), (x + 60*k, y - 15*k),
                (x + 80*k, y - 15*k), (x + 80*k, y), (x, y)
            ])
    rect(screen, (255, 255, 255), (x + 29*k, y - 24*k, 12*k, 8*k))
    rect(screen, (255, 255, 255), (x + 46*k, y - 24*k, 12*k, 8*k))
    circle(screen, (0, 0, 0), (x + 18*k, y), 7*k)
    circle(screen, (0, 0, 0), (x + 62*k, y), 7*k)



# Генерация экрана и дополнительных слоев для прозрачных элементов
scr_x = 550
scr_y = 700
screen = pg.display.set_mode((scr_x, scr_y))
surface1 = pg.Surface((550, 400), pg.SRCALPHA)
surface2 = pg.Surface((550, 400), pg.SRCALPHA)
surface3 = pg.Surface((550, 400), pg.SRCALPHA)
surface4 = pg.Surface((550, 600), pg.SRCALPHA)
surface5 = pg.Surface((550, 600), pg.SRCALPHA)
surface6 = pg.Surface((550, 700), pg.SRCALPHA)
surface7 = pg.Surface((550, 700), pg.SRCALPHA)
surface8 = pg.Surface((550, 700), pg.SRCALPHA)

to_red = 0

def up():
    '''
    Верхняя часть картинки
    Рисует полкпрозрачные дома и облака в ЧБ
    '''
    global to_red
    to_red = +2
    for i in range(140):
        rect(screen, (235 - i, 235 - i, 235 - i), (0, i, 413, 1))
        rect(screen, (i + 20, i + 20, i + 20), (413, i, 137, 1))
    rect(surface1, (15, 15, 15), (530, 0, 20, 140))
    rect(surface1, (20, 20, 20), (353, 0, 80, 140))
    rect(surface1, (0, 0, 0, 100), (0, 0, 40, 140))
    screen.blit(surface1, (0, 0))
    rect(surface2, (0, 0, 0, 150), (313, 0, 80, 140))
    rect(surface2, (0, 0, 0, 150), (223, 20, 80, 140))
    rect(surface2, (0, 0, 0, 150), (0, 70, 70, 140))
    screen.blit(surface2, (0, 0))
    rect(surface3, (0, 0, 0, 150), (255, 60, 80, 140))
    ellipse(surface3, (40, 40, 40, 100), (30, -20, 300, 60))
    screen.blit(surface3, (0, 0))
    ellipse(surface4, (50, 50, 50, 50), (150, -30, 500, 90))
    ellipse(surface4, (40, 40, 40, 150), (490, 90, 200, 70))
    ellipse(surface4, (20, 20, 20, 100), (50, 110, 300, 60))
    screen.blit(surface4, (0, 0))
    ellipse(surface5, (20, 20, 20, 80), (100, 10, 450, 70))
    screen.blit(surface5, (0, 0))
    rect(screen, (255, 255, 255), (413, 0, 3, 140))


def right():
    '''
    Правая часть картинки
    Рисует небо, рамку, дома, облако
    '''
    rect(screen, (255, 255, 255), (187, 127, 376, 356))
    rect(screen, (183, 198, 200), (190, 130, 370, 350))
    rect(screen, (148, 168, 173), (500, 140, 50, 337))
    rect(screen, (148, 173, 168), (420, 155, 70, 328))
    rect(screen, (112, 146, 139), (290, 195, 75, 335))
    ellipse(surface6, (168, 186, 186, 150), (340, 150, 300, 55))
    screen.blit(surface6, (0, 0))
    rect(screen, (182, 199, 195), (450, 187, 75, 342))


def left():
    '''
    Левая часть картинки
    Рисует небо, рамку, дома
    '''
    rect(screen, (255, 255, 255), (0, 140, 328, 366))
    rect(screen, (183, 198, 200), (0, 143, 325, 360))
    rect(screen, (148, 168, 173), (0, 148, 10, 50))
    rect(screen, (148, 173, 168), (20, 163, 70, 343))
    rect(screen, (184, 201, 197), (0, 200, 70, 343))
    rect(screen, (220, 228, 227), (220, 170, 80, 334))
    rect(screen, (111, 146, 139), (180, 210, 80, 335))


def down():
    '''
    Нижняя часть картинки
    Рисует машины
    '''
    global cars_coord
    for each in cars_coord:
        x, y, left, k = each[0], each[1], each[2], each[3]
        car(x, y, left, k)

def processing():
    global cars_coord
    for car in cars_coord:
        car[0] += car[4]
        if (car[2] == False) and (car[0] >= scr_x):
            car[0] = - car[3] * 80
        elif (car[2] == True) and (car[0] <= - car[3] * 80):
            car[0] = scr_x


def white():
    '''
    Белое точечное размытие снизу
    '''
    for i in range(200):
        circle(surface7, (255, 255, 255, 150 - 150 * i / 200), (260, 620), i, 2)
    screen.blit(surface7, (0, 0))


def green():
    '''
    Зеленое горизонтальное размытие посередине
    '''
    for i in range(150):
        rect(surface8, (125, 156, 150, 150 - 150 * i / 150), (0, 310 - i, 550, 1))
        rect(surface8, (125, 156, 150, 150 - 150 * i / 150), (0, 310 + i, 550, 1))
    screen.blit(surface8, (0, 0))


def draw_pict():
    '''
    Картинка
    Рисует картинку
    '''
    rect(screen, (85, 112, 106), (0, 300, 550, 600))  # Фон трава
    up()
    right()
    left()
    down()
    white()
    green()

#draw_pict()


# Проекция
pg.display.update()
clock = pg.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    processing()
    draw_pict()
    pg.display.update()
    screen.fill(BLACK)

pg.quit()
