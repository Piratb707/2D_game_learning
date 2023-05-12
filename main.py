import pygame

from config import *

# инициализация Pygame
pygame.init()

# окно игры
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My Game")

# игровые объекты
player = pygame.Rect(50, 50, 50, 50)
enemy = pygame.Rect(700, 500, 50, 50)
obstacle = pygame.Rect(350, 275, 100, 50)

# основной цикл игры
running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # обновление игровых объектов
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # обнаружение столкновений
    if player.colliderect(enemy):
        player.center = (50, 50)
    if player.colliderect(obstacle):
        player.y -= 5

    # отрисовка игровых объектов
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, enemy)
    pygame.draw.rect(screen, BLACK, obstacle)

    # обновление экрана
    pygame.display.update()

# выход из игры
pygame.quit()
