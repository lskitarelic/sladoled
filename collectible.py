import pygame
import random
import os.path

class Collectible(pygame.sprite.Sprite):

    def __init__(self, value, width, height, image, screen_width):
        self.idx = 0
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.increment = 1
        self.value = value
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = image
        #self.image.fill(color)
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(-200, -50)
        self.rect.x = random.randrange(0, screen_width)
        self.flag = 1

        if not self.value:
            self.images = []
            self.images.append(pygame.image.load(os.path.join('images', 'hole1.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'hole2.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'hole3.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'hole4.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'hole1.png')))
            """ Called each frame. """
        else:
            self.images = []
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream1.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream1.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream1.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream1.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream3.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream3.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream3.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream4.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream4.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream4.png')))
            self.images.append(pygame.image.load(os.path.join('images', 'ice-cream4.png')))
            """ Called each frame. """

 
    def reset_pos(self, screen_width):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-700, -50)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self, screen_width, score):
        if not self.value:
            self.image = self.images[self.idx]
            self.idx = (self.idx + 1) % 5
        else:
            self.image = self.images[self.idx]
            self.idx = (self.idx + 1) % 11
        
        if (score % 25) != 0 : self.flag = 1

        if score % 25 == 0 and self.flag and self.increment < 12 and score != 0:
            self.increment += 1
            self.flag = 0
 
        # Move block down one pixel
        self.rect.y += self.increment
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > pygame.display.Info().current_h:
            self.reset_pos(screen_width)

