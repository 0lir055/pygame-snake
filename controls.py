import pygame
import subprocess

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Python")

background_color = (0, 0, 0)  # Black
button_background_color = (255,255,255)

button_text_color = (0,0,0)
text_color = (255, 255, 255)  # White

font = pygame.font.Font(None, 36)

text = "controls:"
text_surface = font.render(text, True, text_color)
text_pos = (screen.get_width() // 2 - text_surface.get_width() // 2, screen.get_height() // 4 - text_surface.get_height() // 2 - 120)

controls_text = "Up Arrow - Move Up\nRight Arrow - Turn Right\nLeft Arrow - Turn Left\nDown Arrow - Move Down"
controls_surfaces = [font.render(line, True, text_color) for line in controls_text.split('\n')]

button_text = "Return"
button_text_surface = font.render(button_text, True, button_text_color)

button_surface = pygame.Surface((button_text_surface.get_width() + 20, button_text_surface.get_height() + 10))
button_surface.fill(button_background_color)


button_rect = button_surface.get_rect()
button_center = button_rect.center
button_text_pos = (button_center[0] - button_text_surface.get_width() // 2, button_center[1] - button_text_surface.get_height() // 2)
button_surface.blit(button_text_surface, button_text_pos)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # Check if the mouse position is within the button's rectangle
      if button_rect.collidepoint(event.pos):
        # Run the snake.py script and exit
        subprocess.Popen(["python", "snake.py"])
        running = False

  screen.fill(background_color)

  screen.blit(text_surface, text_pos)

  for i, surface in enumerate(controls_surfaces):
    screen.blit(surface, (0, screen_height // 2 - surface.get_height() // 2 + i * 40 - 100))

  button_rect.center = (screen_width // 2, screen_height - button_rect.height // 2 - 50)
  screen.blit(button_surface, button_rect)

  pygame.display.flip()

pygame.quit()