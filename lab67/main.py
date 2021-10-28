import pygame
from pygame.draw import *
from random import randint
import math
pygame.init()

FPS = 20
dt1 = 2
dt2 = 4
scr_x = 1200
scr_y = 600
r_max = 100
screen = pygame.display.set_mode((scr_x, scr_y))

k = 0

#Цвет фона
BLACK = (0, 0, 0)

def new_ball():
    '''
    Создает новый шарик:
    color - цвет, задается рандомно;
    x, y - координаты;
    r - радиус;
    vx, vy - скорость шарика вдоль каждой из осей.
    Все данные помещаются в словарик.
    '''
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(50,255)
    color = (red, green, blue)
    x = randint(r_max, scr_x - r_max)
    y = randint(r_max, scr_y - r_max)
    r = randint(10, r_max)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    ball = {'type': 'ball', 'clr': color, 'r': r, 'p': {'x': x, 'y': y}, 'v': {'vx': vx, 'vy': vy}}
    return ball

def new_word():
    '''
    Создает новое слово:
    color - цвет, задается рандомно;
    x, y - координаты;
    r - длина слова в пикселях;
    vx, vy - скорость шарика вдоль каждой из осей;
    f_size - размер шрифта
    Все данные помещаются в словарик.
    '''

    # Цензура
    #words = ["самое", "важное", "слово"]
    # Без цезнуры
    words = ["пиздато", "ебануться", "блять", "охуенно"]
    l = len(words)
    t = randint(0,l-1)
    wrd = words[t]
    f_size = randint(10, 80)
    r = int(f_size * len(wrd)/2)
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(50,255)
    color = (red, green, blue)
    x = randint(r, scr_x - r)
    y = randint(2 * f_size, scr_y - 2* f_size)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    word = {'type':'word', 'word': wrd, 'clr': color, 'r': r, 'p': {'x': x, 'y': y},
            'v': {'vx': vx, 'vy': vy}, 'f': f_size}
    return word


def Pythagoras(a0, b0, a, b):
    '''
    Считает расстояние между двумя точками
    '''
    r0 = math.sqrt((a-a0)**2+(b-b0)**2)
    return r0


def counter():
    # Создает счетчик на экране
    font = pygame.font.SysFont(None, int(40))
    txt = "Колличество очков: " + str(k)
    img = font.render(txt, True, (255, 255, 0))
    screen.blit(img, (30, 50))


def painter(object):
    '''
    Отрисовка объектов в зависимости от типа.
    '''
    if object['type'] == 'ball':
        circle(screen, object['clr'], (object['p']['x'], object['p']['y']), object['r'])
    elif object['type'] == 'word':
        font = pygame.font.SysFont(None, int(object['f']))
        txt = object['word']
        img = font.render(txt, True, object['clr'])
        screen.blit(img, (object['p']['x'], object['p']['y']))

def processing(object):
    '''
    Изменение координат объекта.
    '''
    if object['type'] == 'word':
        cube = randint(0, 5)
        switch = randint(-50, 50)
        if cube == 2:
            object['p']['x'] += switch
        elif cube == 3:
            object['p']['y'] += switch

    object['p']['x'] += object['v']['vx'] * dt1
    object['p']['y'] += object['v']['vy'] * dt1
    painter(object)

def wall_hit(object):
    '''
    Обработка удара о стенку.
    '''
    # Правая и левая стенки
    if object['p']['x'] > scr_x - object['r'] or object['p']['x'] < object['r'] :
        object['v']['vx'] *= - 1
    # Нижняя и верхняя стенка
    if object['p']['y'] >= scr_y - object['r'] or object['p']['y'] <= object['r']:
        object['v']['vy'] *= - 1

def click(event):
    '''
    Обработка клика.
    Клик попал в один из объектов -> объект удаляется из массива, счетчик повышается, создается новый объект.
    '''
    global k, floating_objects
    for objects in floating_objects:
        for obj in objects:
            r0 = Pythagoras(event.pos[0], event.pos[1], obj['p']['x'], obj['p']['y'])
            if r0 <= obj['r']:
                objects.remove(obj)
                if obj['type'] == 'ball':
                    new_obj = new_ball()
                    k += 1
                elif obj['type'] == 'word':
                    new_obj = new_word()
                    k += 100
                objects.append(new_obj)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

floating_words = []
floating_balls = []
floating_objects = [floating_balls, floating_words]

for i in range(5):
    ball = new_ball()
    floating_balls.append(ball)

for i in range(6):
    word = new_word()
    floating_words.append(word)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    for objects in floating_objects:
        for obj in objects:
            wall_hit(obj)
            processing(obj)

    counter()

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

