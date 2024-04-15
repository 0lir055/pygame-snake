# importing libraries
import pygame
import time
import random
import subprocess

snake_speed = 10

# Window size
screen_width = 800
screen_height = 600

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(124, 252, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((screen_width, screen_height))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_segments = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]
# fruit position
fruit_location = [random.randrange(1, (screen_width//10)) * 10, 
				random.randrange(1, (screen_height//10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
current_score = 0

# displaying Score function
def display_score(choice, color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object 
	# score_surface
	score_surface = score_font.render('Score : ' + str(current_score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)

# game over function
def game_over():
    # After 2 seconds we will quit the program
    time.sleep(2)

    # Deactivating pygame library
    pygame.quit()

    # Run the gameover.py file
    subprocess.Popen(["python", "gameover.py"])

    # Quit the program
    quit()

# Main Function
while True:
	
	# handling key events
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

	# If two keys pressed simultaneously
	# we don't want snake to move into two 
	# directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10
	snake_segments.insert(0, list(snake_position))
	if snake_position[0] == fruit_location[0] and snake_position[1] == fruit_location[1]:
		current_score += 10
		fruit_spawn = False
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

	# Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > screen_width-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > screen_height-10:
		game_over()

	# Touching the snake body
	for block in snake_segments[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# displaying score continuously
	display_score(1, white, 'times new roman', 20)
	
	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refresh Rate
	fps.tick(snake_speed)
