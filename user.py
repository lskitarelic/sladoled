import pygame
import collectible
import os.path


class Player(collectible.Collectible):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self, screen_width, score):
        self.images = []
        self.images.append(pygame.image.load(os.path.join('images', 'doggo1.png')))
        self.images.append(pygame.image.load(os.path.join('images', 'doggo2.png')))
        self.images.append(pygame.image.load(os.path.join('images', 'doggo3.png')))
        self.images.append(pygame.image.load(os.path.join('images', 'doggo2.png')))
        self.images.append(pygame.image.load(os.path.join('images', 'doggo1.png')))
        self.images.append(pygame.image.load(os.path.join('images', 'doggo4.png')))
        self.images.append(pygame.image.load(os.path.join('images', 'doggo5.png')))
        self.images.append(pygame.image.load(os.path.join('images', 'doggo4.png')))
        self.images.append(pygame.image.load(os.path.join('images', 'doggo1.png')))
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        self.image = self.images[self.idx]
        self.idx = (self.idx + 1) % 9
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.center = pos
        
