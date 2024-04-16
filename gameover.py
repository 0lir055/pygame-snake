import pygame
import subprocess
import sys

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
background_color = (0, 0, 0)  # Black
screen.fill(background_color)

# Set the title font and size
title_font = pygame.font.Font(None, 64)

# Create the title text
title_text = title_font.render("GAME OVER!", True, (255, 255, 255))  # White

# Calculate the position of the title text
title_x = (screen_width - title_text.get_width()) // 2
title_y = (screen_height - title_text.get_height()) // 3

# Draw the title text on the screen
screen.blit(title_text, (title_x, title_y))

# Set the button font and size
button_font = pygame.font.Font(None, 32)

# Create the buttons
button1_text = button_font.render("Home screen", True, (0, 0, 0))  # Black
button2_text = button_font.render("Quit", True, (0, 0, 0))  # Black

# Create button surfaces
button1_surface = pygame.Surface((button1_text.get_width() + 20, button1_text.get_height() + 10))
button2_surface = pygame.Surface((button2_text.get_width() + 20, button2_text.get_height() + 10))

# Fill the button surfaces with white color
button1_surface.fill((255, 255, 255))  # White
button2_surface.fill((255, 255, 255))  # White

# Blit the text onto the button surfaces
button1_surface.blit(button1_text, (10, 5))
button2_surface.blit(button2_text, (10, 5))

# Calculate the position of the buttons
button1_x = (screen_width - button1_surface.get_width()) // 2
button1_y = (screen_height - button1_surface.get_height()) // 2
button2_x = (screen_width - button2_surface.get_width()) // 2
button2_y = button1_y + button1_surface.get_height() + 20

# Draw the buttons on the screen
screen.blit(button1_surface, (button1_x, button1_y))
screen.blit(button2_surface, (button2_x, button2_y))

# Update the display
pygame.display.flip()

# Game loop
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the "Start Game" button was clicked
            if button1_x <= mouse_x <= button1_x + button1_surface.get_width() and button1_y <= mouse_y <= button1_y + button1_surface.get_height():
                # Run the game.py file
                subprocess.Popen(["python", "snake.py"])
                running = False

            if button2_x <= mouse_x <= button2_x + button2_surface.get_width() and button2_y <= mouse_y <= button2_y + button2_surface.get_height():
                pygame.quit()
                sys.exit()

    # Update the display
    pygame.display.flip()

    if not running:
        break

# Quit Pygame
pygame.quit()
sys.exit()