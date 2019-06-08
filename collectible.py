import pygame
import random

class Collectible(pygame.sprite.Sprite):
    def __init__(self, color, width, height, image, screen_width):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.increment = 1

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = image
        #self.image.fill(color)
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(-1000, -50)
        self.rect.x = random.randrange(0, screen_width)

 
    def reset_pos(self, screen_width):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-200, -80)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self, screen_width, score):
        """ Called each frame. """
        if score % 50 == 0 and self.increment <= 7:
            self.increment += 0.2
 
        # Move block down one pixel
        self.rect.y += self.increment
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 540:
            self.reset_pos(screen_width)
