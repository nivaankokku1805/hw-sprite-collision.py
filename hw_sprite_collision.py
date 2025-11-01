import pygame
# Initialize Pygame
pygame.init()
# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Add Sprites and Custom Event")
clock = pygame.time.Clock()
# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# Define a custom event for changing sprite colors
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000) # Trigger every 1 second
# Create a Sprite class
class ColorChangingSprite(pygame.sprite.Sprite):
   def __init__(self, color, x, y):
       super().__init__()
       self.image = pygame.Surface((50, 50))
       self.image.fill(color)
       self.rect = self.image.get_rect(center=(x, y))
       self.color = color
   def change_color(self):
       # Toggle between RED and BLUE
       self.color = RED if self.color == BLUE else BLUE
       self.image.fill(self.color)
# Create two sprites and add them to a group
sprite1 = ColorChangingSprite(RED, 200, 200)
sprite2 = ColorChangingSprite(BLUE, 400, 200)
all_sprites = pygame.sprite.Group(sprite1, sprite2)
# Main game loop
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       # Handle the custom event to change sprite colors
       if event.type == CHANGE_COLOR_EVENT:
           for sprite in all_sprites:
               sprite.change_color()
   # Clear the screen
   screen.fill(WHITE)
   # Draw all sprites
   all_sprites.draw(screen)
   # Update the display
   pygame.display.flip()
   clock.tick(30)
pygame.quit()