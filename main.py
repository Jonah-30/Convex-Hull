import pygame
import random
import time
import os
from queue import PriorityQueue

from point import Points
from algorithm import JarvisMarch


def start():
    WIDTH, HEIGHT = 800, 700
    SCREEN = (WIDTH, HEIGHT)
    # for full screen enable the line bellow
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # configurations
    fps = 30
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Convex Hull ( Gift Wrapper)")
    win = pygame.display.set_mode(SCREEN)

    # colors
    White = (255, 255, 255)
    Black = (30, 30, 30)
    Grey = (180, 180, 180)
    Blue = (0, 183, 255)
    Yellow = (255, 230, 0, 128)
    Red = (255, 15, 79)
    Green = (41, 255, 123)

    # background color
    win.fill(Black)

    # variables
    sleep_time = 0.01
    point_number = 10
    offset = 50
    points = []
    convex_hull = []
    # Generate Points Points(number of points , offset number of the screen, ......)
    for n in range(point_number):
        point = Points(random.randint(offset, WIDTH - offset), random.randint(offset, HEIGHT - offset))
        pygame.draw.circle(win, White, (point.x, point.y), 4)
        points.append(point)
    pygame.display.update()

    # jarvis March algorithm
    next_step = False
    while not next_step:
        for event in pygame.event.get():
            # click the space or return key to run program
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    jarvis = JarvisMarch(points, Green, win, convex_hull, Yellow, Red, Grey, sleep_time)
                    jarvis.left_most()
                    jarvis.convex()
                    next_step = True
                # click 'q' to quit completely
                if event.key == pygame.K_q:
                    pygame.quit()

    # draw border lines
    index = 0
    for t in range(len(convex_hull)):
        if index != len(convex_hull) - 1:
            time.sleep(sleep_time)
            pygame.draw.line(win, Blue, convex_hull[index], convex_hull[index + 1], 4)
            index = index + 1
            pygame.display.update()
        else:
            time.sleep(sleep_time)
            pygame.draw.line(win, Blue, convex_hull[len(convex_hull) - 1], convex_hull[0], 4)
            pygame.display.update()

    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                # click 'q' to quit completely
                if event.key == pygame.K_q:
                    pygame.quit()
                # click 'r' to restart
                if event.key == pygame.K_r:
                    start()

    pygame.quit()


start()
