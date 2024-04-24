import pygame
import subprocess
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

background_color = (0, 0, 0)  
screen.fill(background_color)

title_font = pygame.font.Font(None, 64)

title_text = title_font.render("GAME OVER!", True, (255, 255, 255))  

title_x = (screen_width - title_text.get_width()) // 2
title_y = (screen_height - title_text.get_height()) // 3

screen.blit(title_text, (title_x, title_y))

button_font = pygame.font.Font(None, 32)

button1_text = button_font.render("Home screen", True, (0, 0, 0))  
button2_text = button_font.render("Quit", True, (0, 0, 0))  

button1_surface = pygame.Surface((button1_text.get_width() + 20, button1_text.get_height() + 10))
button2_surface = pygame.Surface((button2_text.get_width() + 20, button2_text.get_height() + 10))

button1_surface.fill((255, 255, 255))  
button2_surface.fill((255, 255, 255))  

button1_surface.blit(button1_text, (10, 5))
button2_surface.blit(button2_text, (10, 5))

button1_x = (screen_width - button1_surface.get_width()) // 2
button1_y = (screen_height - button1_surface.get_height()) // 2
button2_x = (screen_width - button2_surface.get_width()) // 2
button2_y = button1_y + button1_surface.get_height() + 20

screen.blit(button1_surface, (button1_x, button1_y))
screen.blit(button2_surface, (button2_x, button2_y))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if button1_x <= mouse_x <= button1_x + button1_surface.get_width() and button1_y <= mouse_y <= button1_y + button1_surface.get_height():
                subprocess.Popen(["python", "snake.py"])
                running = False

            if button2_x <= mouse_x <= button2_x + button2_surface.get_width() and button2_y <= mouse_y <= button2_y + button2_surface.get_height():
                pygame.quit()
                sys.exit()

    pygame.display.flip()

    if not running:
        break

pygame.quit()
sys.exit()