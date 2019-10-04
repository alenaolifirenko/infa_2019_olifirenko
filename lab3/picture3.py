from graph import *


def waves(n):
    listWaves = []
    brushColor(255, 204, 0)
    r = 500 / (n * 2)
    x = r
    for i in range(n):
        listWaves.append(circle(x, 310, r))
        x += 2 * r
    return listWaves


def umbrella(k, x, y):
    penColor(102, 51, 0)
    penSize(5)
    line(x, y - 110 * k, x, y)
    brushColor(230, 30, 0)
    penSize(1)
    polygon([(x - 50 * k, y - 110 * k), (x, y - 130 * k),
             (x + 5 * k, y - 130 * k), (x + 55 * k, y - 110 * k)])


def ship(k, x, y):
    listShip = []
    # основа
    penSize(0)
    penColor(102, 51, 51)
    brushColor(102, 51, 51)
    listShip.append(polygon([(x, y), (x - 60 * k, y + 40 * k),
                             (x - 260 * k, y + 40 * k), (x - 280 * k, y), (x, y)]))
    # мачта
    penColor('black')
    brushColor('black')
    listShip.append(rectangle(x - 180 * k, y, x - 170 * k, y - 120 * k))
    # парус
    penSize(1)
    brushColor(255, 255, 153)
    listShip.append(polygon([(x - 170 * k, y), (x - 140 * k, y - 60 * k),
                             (x - 80 * k, y - 60 * k), (x - 170 * k, y)]))
    listShip.append(polygon([(x - 170 * k, y - 120 * k), (x - 140 * k, y - 60 * k),
                             (x - 80 * k, y - 60 * k), (x - 170 * k, y - 120 * k)]))
    # иллюминатор
    penSize(5 * k)
    brushColor('white')
    listShip.append(circle(x - 60 * k, y + 20 * k, 10 * k))
    return listShip


def cloud(k, x, y):
    listCloud = []
    brushColor('white')
    penColor('black')
    penSize(1)
    for i in range(4):
        listCloud.append(circle(x, y, 15 * k))
        x += 15 * k
    x -= 4 * 15 * k - 10 * k
    y -= 15 * k
    for u in range(3):
        listCloud.append(circle(x, y, 15 * k))
        x += 15 * k
    return listCloud


def sun(x, y):
    listSun = []
    penColor(255, 204, 0)
    brushColor(255, 204, 0)
    listSun.append(circle(x, y, 30))
    return listSun


def background():
    penSize(0)
    brushColor(204, 255, 255)
    rectangle(0, 0, 500, 200)
    brushColor(255, 204, 0)
    rectangle(0, 300, 500, 400)


def sea():
    brushColor(0, 0, 102)
    rectangle(0, 200, 500, 300)


def moving(OBJECT, x, y):
    for obj in OBJECT:
        moveObjectBy(obj, x, y)


windowSize(500, 400)
background()
Sun = sun(430, 50)
sea()
Waves = waves(13)
Cloud1 = cloud(1, 200, 50)
Cloud2 = cloud(1.5, 50, 50)
Cloud3 = cloud(1.3, 150, 110)
umbrella(0.7, 150, 330)
umbrella(1.1, 70, 390)
bigShip = ship(1, 480, 220)
smallShip = ship(0.5, 200, 195)


def animation():
    moving(bigShip, 4, 0)
    moving(smallShip, 5, 0)
    moving(Cloud1, -2, 0.5)
    moving(Sun, 0, 1)
    moving(Cloud2, -1, 0)
    moving(Cloud3, -.5, -1)
    moving(Waves, 1, 0.1)


onTimer(animation, 50)

run()
