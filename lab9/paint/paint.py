#Imports
import pygame as p
import math

#Initialzing 
p.init()

#Setting up FPS
clock = p.time.Clock()

#Creating colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (122, 127, 128)

#Creating a screen
X, Y = 1000, 800
screen = p.display.set_mode((X, Y))
p.display.set_caption("Paint")
screen.fill(WHITE)

#Other variables for programm
cur_color = BLACK
brush_size = 5
drawing = False
drawing_rect = False
drawing_circle = False
erasing = False
cur_tool = 0

#Creating font
font = p.font.SysFont("Sand", 20)

#Setting up color buttons
colors_button = [
    (RED, p.Rect(10,10,30,30)),
    (GREEN, p.Rect(50,10,30,30)),
    (BLUE, p.Rect(90,10,30,30)),
    (YELLOW, p.Rect(130,10,30,30)),
    (BLACK, p.Rect(170,10,30,30)),
]

#Setting up tool buttons
tools_button = [
    ("Brush", p.Rect(300, 10, 60, 30), 0),
    ("Rect", p.Rect(370, 10, 60, 30), 1),
    ("Circle", p.Rect(440, 10, 60, 30), 2),
    ("Eraser", p.Rect(510, 10, 60, 30), 3),
    ("Square", p.Rect(580, 10, 60, 30), 4),
    ("Triangle", p.Rect(650, 10, 80, 30), 5),
    ("Eq Tri", p.Rect(740, 10, 80, 30), 6),
    ("Rhombus", p.Rect(830, 10, 80, 30), 7),
]

#Main loop
run = True
while run:
    for i in p.event.get():
        if i.type == p.QUIT:
            run = False
        if i.type == p.MOUSEBUTTONDOWN:
            pos = p.mouse.get_pos()
            for color, rect in colors_button:
                if rect.collidepoint(pos):
                    cur_color = color
                    break
            for _, rect, tool in tools_button:
                if rect.collidepoint(pos):
                    cur_tool = tool
                    break
            start_pos = pos
            drawing = cur_tool == 0
            drawing_rect = cur_tool == 1
            drawing_circle = cur_tool == 2
            erasing = cur_tool == 3
            drawing_square = cur_tool == 4
            drawing_triangle = cur_tool == 5
            drawing_eq_triangle = cur_tool == 6
            drawing_rhombus = cur_tool == 7

        if i.type == p.MOUSEBUTTONUP:
            end_pos = p.mouse.get_pos()
            if drawing_rect:
                p.draw.rect(screen, cur_color, (*start_pos, *(end_pos[i] - start_pos[i] for i in range(2))))
            elif drawing_circle:
                R = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                p.draw.circle(screen, cur_color, start_pos, R)
            elif drawing_square:
                side = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                p.draw.rect(screen, cur_color, (*start_pos, side, side))
            elif drawing_triangle:
                p.draw.polygon(screen, cur_color, [start_pos, end_pos, (start_pos[0], end_pos[1])])
            elif drawing_eq_triangle:
                height = abs(end_pos[1] - start_pos[1])
                base = int(height * math.sqrt(3))
                p.draw.polygon(screen, cur_color, [start_pos, (start_pos[0] + base // 2, end_pos[1]), (start_pos[0] - base // 2, end_pos[1])])
            elif drawing_rhombus:
                dx, dy = (end_pos[0] - start_pos[0]) // 2, (end_pos[1] - start_pos[1]) // 2
                p.draw.polygon(screen, cur_color, [(start_pos[0], start_pos[1] - dy), (start_pos[0] + dx, start_pos[1]), (start_pos[0], start_pos[1] + dy), (start_pos[0] - dx, start_pos[1])])
            drawing, drawing_rect, drawing_circle, erasing, drawing_square, drawing_triangle, drawing_eq_triangle, drawing_rhombus = [False] * 8

        if i.type == p.MOUSEMOTION:
            pos = p.mouse.get_pos()
            if drawing:
                p.draw.circle(screen, cur_color, pos, brush_size)
            elif erasing:
                p.draw.circle(screen, WHITE, pos, brush_size)
    
    pressed = p.key.get_pressed()
    if pressed[p.K_UP]: brush_size += 1
    if pressed[p.K_DOWN] and brush_size > 1: brush_size -= 1

    for color, rect in colors_button:
        p.draw.rect(screen, color, rect)
        p.draw.rect(screen, BLACK, rect, 1)

    for name, rect, tool in tools_button:
        p.draw.rect(screen, GRAY if cur_tool == tool else WHITE, rect)
        p.draw.rect(screen, BLACK, rect, 1)
        screen.blit(font.render(name, True, BLACK), (rect.x + 5, rect.y + 5))

    p.display.update()
    clock.tick(99999999)

p.quit()