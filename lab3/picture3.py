from graph import *

penColor('purple')        #фон
rectangle(0, 0, 500, 400)
brushColor(204, 255, 255)
rectangle(0, 0, 500, 200)
brushColor(0, 0, 102)
rectangle(0, 200, 500, 300)
penColor(255, 204, 0)


brushColor(255, 204, 0)
circle(430, 50, 30)
rectangle(0, 300, 500, 400)

n = 13                   # волны
r = 500 / (n * 2)
x = r
for i in range(n):
    circle(x, 310, r)
    x += 2 * r

penColor(102, 51, 0)     #зонтики
penSize(5)
line(55, 280, 55, 390)
brushColor(230, 30, 0)
penSize(1)
polygon([(5, 280), (55, 260), (60, 260), (110, 280)])

penSize(5)
line(125, 260, 125, 360)
brushColor(230, 30, 0)
penSize(1)
polygon([(75, 260), (125, 240), (130, 240), (180, 260)])

penColor(102, 51, 51)       #кораблики
brushColor(102, 51, 51)
polygon([(480, 220), (420, 260), (220, 260), (200, 220), (480, 220)])
polygon([(190, 210), (160, 230), (50, 230), (40, 210), (190, 210)])
penSize(0)
brushColor('black')
rectangle(300, 220, 310, 100)
rectangle(100, 210, 105, 155)
penSize(1)
penColor('black')
brushColor(255, 255, 153)
polygon([(310, 220), (340, 160), (400, 160), (310, 220)])
polygon([(310, 100), (340, 160), (400, 160), (310, 100)])
polygon([(105, 210), (120, 183), (150, 183), (105, 210)])
polygon([(105, 155), (120, 183), (150, 183), (105, 155)])
penSize(5)
brushColor('white')
circle(420, 240, 10)
penSize(3)
circle(150, 220, 5)

brushColor('white')     #облака
penSize(1)
circle(150, 50, 15)
circle(170, 50, 15)
circle(185, 50, 15)
circle(200, 50, 15)
circle(160, 35, 15)
circle(175, 35, 15)
circle(190, 35, 15)

circle(50, 50, 10)
circle(65, 50, 10)
circle(80, 50, 10)
circle(95, 50, 10)
circle(55, 40, 10)
circle(70, 40, 10)
circle(85, 40, 10)

circle(120, 110, 13)
circle(140, 110, 13)
circle(155, 110, 13)
circle(170, 110, 13)
circle(130, 95, 13)
circle(145, 95, 13)
circle(160, 95, 13)

run()