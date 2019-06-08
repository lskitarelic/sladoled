import pygame
import random

class Collectible(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, width, height, image, screen_width):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = image
        #self.image.fill(color)
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
    def reset_pos(self, screen_width):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self, screen_width):
        """ Called each frame. """
 
        # Move block down one pixel
        self.rect.y += 1
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 540:
            self.reset_pos(screen_width)
