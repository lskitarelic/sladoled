import pygame
import random

class Collectible(pygame.sprite.Sprite):

    def __init__(self, value, width, height, image, screen_width):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.increment = 1
        self.value = value;
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = image
        #self.image.fill(color)
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(-100, -20)
        self.rect.x = random.randrange(0, screen_width)
        self.flag = True

 
    def reset_pos(self, screen_width):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-500, -20)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self, screen_width, score):
        """ Called each frame. """
        
        if (score % 15) != 0: self.flag = True

        if score % 15 == 0 and self.flag and self.increment < 25 and score != 0:
            self.increment += 1
            self.flag = False
 
        # Move block down one pixel
        self.rect.y += self.increment
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 540:
            self.reset_pos(screen_width)

