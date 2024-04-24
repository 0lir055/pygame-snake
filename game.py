import pygame
import time
import random
import subprocess
import sys

screen_width = 800
screen_height = 600

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(124, 252, 0)

pygame.init()

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((screen_width, screen_height))

fps = pygame.time.Clock()

snake_position = [100, 50]

snake_segments = [[200, 100],
				  [190, 100],
				  [180, 100],
				  [170, 100],
				  [160, 100],
				  [150, 100]]

fruit_location = [random.randrange(1, (screen_width//10)) * 10, 
				random.randrange(1, (screen_height//10)) * 10]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

current_score = 0

def game_over():
	time.sleep(2)
	pygame.quit()
	subprocess.Popen(["python", "gameover.py"])
	quit()

def pause_game():
	paused = True
	button_font = pygame.font.SysFont(None, 50)
	paused_font = pygame.font.SysFont(None, 70) 
	screen_width, screen_height = game_window.get_size()  
	fps = pygame.time.Clock() 

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				if resume_button.collidepoint(mouse_pos):
					paused = False
				elif restart_button.collidepoint(mouse_pos):
					pygame.quit()
					subprocess.call([sys.executable, "game.py"])  
				elif quit_button.collidepoint(mouse_pos):
					pygame.quit()
					quit()

		game_window.fill((0, 0, 0))  

		paused_text = paused_font.render('Paused', True, (255, 255, 255))  
		game_window.blit(paused_text, ((screen_width - paused_font.size('Paused')[0]) / 2, 20))

		button_width, button_height = 200, 50
		button_spacing = 20  
		button_y_start = (screen_height - 3 * button_height - 2 * button_spacing) / 2  
		resume_button = pygame.draw.rect(game_window, (255, 255, 255), ((screen_width - button_width) / 2, button_y_start, button_width, button_height))  
		restart_button = pygame.draw.rect(game_window, (255, 255, 255), ((screen_width - button_width) / 2, button_y_start + button_height + button_spacing, button_width, button_height))  
		quit_button = pygame.draw.rect(game_window, (255, 255, 255), ((screen_width - button_width) / 2, button_y_start + 2 * (button_height + button_spacing), button_width, button_height))

		game_window.blit(button_font.render('Resume', True, (0, 0, 0)), ((screen_width - button_font.size('Resume')[0]) / 2, button_y_start + 10))  
		game_window.blit(button_font.render('Restart', True, (0, 0, 0)), ((screen_width - button_font.size('Restart')[0]) / 2, button_y_start + button_height + button_spacing + 10))  
		game_window.blit(button_font.render('Quit', True, (0, 0, 0)), ((screen_width - button_font.size('Quit')[0]) / 2, button_y_start + 2 * (button_height + button_spacing) + 10))  

		pygame.display.update()
		fps.tick(5)  


def display_score(choice, color, font, size):
	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('Score : ' + str(current_score), True, color)
	score_rect = score_surface.get_rect()
	game_window.blit(score_surface, score_rect)

while True:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'
			if event.key == pygame.K_ESCAPE:
				pause_game()

	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	snake_segments.insert(0, list(snake_position))
	if snake_position[0] == fruit_location[0] and snake_position[1] == fruit_location[1]:
		current_score += 1
		fruit_spawn = False
		snake_speed += 1
	else:
		snake_segments.pop()
		
	if not fruit_spawn:
		fruit_location = [random.randrange(1, (screen_width//10)) * 10, 
						random.randrange(1, (screen_height//10)) * 10]
		
	fruit_spawn = True
	game_window.fill(green)
	
	for pos in snake_segments:
		pygame.draw.rect(game_window, black,
						pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(game_window, red, pygame.Rect(
		fruit_location[0], fruit_location[1], 10, 10))

	if snake_position[0] < 0 or snake_position[0] > screen_width-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > screen_height-10:
		game_over()

	for block in snake_segments[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	display_score(1, black, 'sans serif', 20)
	
	pygame.display.update()

	snake_speed = 10

	fps.tick(snake_speed)