import pygame
from pygame.draw import *

pygame.init()

def igloo(x, y, k):
    '''
    Иглу
    x - крайняя левая координата итоговой фигуры;
    y - крайняя верхняя координата итоговой фигуры;
    k - масштабирующий фактор.
    '''
    # Рисуем Иглу
    ellipse(screen, (230, 230, 230), (x, y, 400*k, 360*k))
    ellipse(screen, (0, 0, 0), (x, y, 400*k, 360*k), width=2)
    # Вертикальные полосочки
    ellipse(screen, (0, 0, 0), (x, y, 400*k, 800*k), width=2)
    ellipse(screen, (0, 0, 0), (x, y, 400*k, 2400*k), width=2)
    ellipse(screen, (0, 0, 0), (x, y, 400*k, 7200*k), width=2)
    # Горизонтальные полосочки
    line(screen, (0, 0, 0), (x, y+180*k), (x+400*k, y+180*k), width=1)
    line(screen, (0, 0, 0), (x+8*k, y+140*k), (x+400*k-8*k, y+140*k), width=1)
    line(screen, (0, 0, 0), (x+22*k, y+100*k), (x+400*k-22*k, y+100*k), width=1)
    line(screen, (0, 0, 0), (x+52*k, y+60*k), (x+400*k-52*k, y+60*k), width=1)
    line(screen, (0, 0, 0), (x+110*k, y+20*k), (x+400*k-110*k, y+20*k), width=1)
    # Скрашиваем уродство белым прямоугольником
    rect(screen, (250, 250, 250), (x-50, y+180*k, 794*k, 800*k))

def eskimos(x,y,k):
    '''
    Эскимос
    x - крайняя левая координата итоговой фигуры;
    y - крайняя верхняя координата итоговой фигуры;
    k - масштабирующий фактор.
    (переменные x0 и y0 используются для перехода из начальной СК в новую.)
    '''
    x0 = 561
    y0 = 603

    # тело и голова
    ellipse(screen, (227, 222, 219), (x, y, (696 - 561)*k, (692 - 603)*k))
    ellipse(screen, (145, 124, 111), (x+(553-x0)*k, y+(652-y0)*k, (710 - 553)*k, (806 - 652) * 2*k))
    rect(screen, (250, 250, 250), (x+(550-x0)*k, y+(800-y0)*k, 200*k, 200*k))
    ellipse(screen, (172, 157, 147), (x+(577-x0)*k, y+(615-y0)*k, (679 - 577)*k, (683 - 615)*k))
    ellipse(screen, (227, 219, 219), (x+(595-x0)*k, y+(629-y0)*k, (664 - 595)*k, (676 - 629)*k))
    # лицо
    line(screen, (0, 0, 0), (x+(602-x0)*k, y+(641-y0)*k), (x+(618-x0)*k, y+(650-y0)*k), width=1)
    line(screen, (0, 0, 0), (x+(655-x0)*k, y+(646-y0)*k), (x+(637-x0)*k, y+(650-y0)*k), width=1)
    polygon(screen, (255, 0, 0), [(x+(649-x0)*k, y+(668-y0)*k),
                                  (x+(638-x0)*k, y+(663-y0)*k),
                                  (x+(614-x0)*k, y+(664-y0)*k)])
    # руки
    ellipse(screen, (145, 124, 111), (x+(520-x0)*k, y+(696-y0)*k, (600 - 520)*k, (723 - 696)*k))
    ellipse(screen, (145, 124, 111), (x+(668-x0)*k, y+(696-y0)*k, (600 - 520)*k, (723 - 696)*k))
    # ноги
    ellipse(screen, (145, 124, 111), (x+(577-x0)*k, y+(776-y0)*k, (617 - 577)*k, (841 - 776)*k))
    ellipse(screen, (145, 124, 111), (x+(646-x0)*k, y+(776-y0)*k, (617 - 577)*k, (841 - 776)*k))
    ellipse(screen, (145, 124, 111), (x+(563-x0)*k, y+(822-y0)*k, (615 - 563)*k, (845 - 822)*k))
    ellipse(screen, (145, 124, 111), (x+(653-x0)*k, y+(822-y0)*k, (615 - 563)*k, (845 - 822)*k))
    # шмотки
    rect(screen, (108, 93, 83), (x+(607-x0)*k, y+(682-y0)*k, (644 - 607)*k, (786 - 682)*k))
    rect(screen, (108, 93, 83), (x+(555-x0)*k, y+(790-y0)*k, (708 - 555)*k, (806 - 790)*k))
    # палка
    line(screen, (0, 0, 0), (x+(528-x0)*k, y+(610-y0)*k), (x+(534-x0)*k, y+(824-y0)*k), width=1)

def cat(x,y,k):
    '''
    Кит с рибой
    x - крайняя левая координата тела кота;
    y - крайняя верхняя координата тела кота;
    k - масштабирующий фактор.
    (переменные x0 и y0 используются для перехода из начальной СК в новую.)
    '''
    x0 = 118
    y0 = 843

    # тело кота
    ellipse(screen, (204, 204, 204), (x+(118-x0)*k, y+(843-y0)*k, (262 - 118)*k, (880 - 843)*k))
    ellipse(screen, (204, 204, 204), (x+(72-x0)*k, y+(856-y0)*k, (162 - 72)*k, (873 - 856)*k))
    ellipse(screen, (204, 204, 204), (x+(147-x0)*k, y+(868-y0)*k, (171 - 147)*k, (907 - 868)*k))
    ellipse(screen, (204, 204, 204), (x+(242-x0)*k, y+(856-y0)*k, (162 - 72)*k, (873 - 856)*k))
    ellipse(screen, (204, 204, 204), (x+(219-x0)*k, y+(868-y0)*k, (171 - 147)*k, (907 - 868)*k))
    # голова кота
    circle(screen, (204, 204, 204), (x+(140-x0)*k, y+(833-y0)*k), 20*k)
    circle(screen, (255, 255, 255), (x+(142-x0)*k, y+(831-y0)*k), 7*k)
    circle(screen, (0, 0, 0), (x+(142-x0)*k + 6*k, y+(831-y0)*k), 3*k)
    circle(screen, (255, 255, 255), (x+(126-x0)*k, y+(827-y0)*k), 7*k)
    circle(screen, (0, 0, 0), (x+(126-x0)*k + 6*k, y+(827-y0)*k), 3*k)
    polygon(screen, (204, 204, 204), [(x+(133-x0)*k, y+(821-y0)*k - 5*k), (x+(135-x0)*k, y+(812-y0)*k - 5*k),
                                      (x+(141-x0)*k, y+(819-y0)*k - 5*k), (x+(153-x0)*k, y+(819-y0)*k - 5*k),
                                      (x+(158-x0)*k, y+(815-y0)*k - 5*k), (x+(158-x0)*k, y+(830-y0)*k - 5*k),
                                      (x+(135-x0)*k, y+(822-y0)*k - 5*k)])
    font = pygame.font.SysFont(None, int(24*k))
    img = font.render('Это котик с рибой', True, (0, 0, 0))
    screen.blit(img, (x+(20-x0)*k, y+(880-y0)*k))


FPS = 30
screen = pygame.display.set_mode((794, 1123))

# закрашиваем фон
screen.fill((230, 230, 230))
rect(screen, (250, 250, 250), (0, 500, 794, 1123-500))

# Рисуем Иглу

igloo_coord = [(25, 480, 0.3),
               (377, 506, 0.3),
               (50, 460, 1),
               (47, 595, 0.5),
               (195, 661, 0.5)]

for data in igloo_coord:
    x =data[0]
    y = data[1]
    k = data[2]
    igloo(x, y, k)

# Рисуем эскимоса
eskimos_coord = [(617,488,0.3),
                 (723,505,0.3),
                 (640,538,0.3),
                 (611,595,0.3),
                 (510,576,0.3),
                 (491, 672, 0.3),
                 (561,603,1)]

for data in eskimos_coord:
    x =data[0]
    y = data[1]
    k = data[2]
    eskimos(x, y, k)

# Рисуем кита с рибой
cat_coord = [(118,843,1),
             (150,754,0.6)]

for data in cat_coord:
    x =data[0]
    y = data[1]
    k = data[2]
    cat(x, y, k)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
