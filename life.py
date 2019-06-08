import pygame

class Health(pygame.sprite.Sprite):
    def __init__(self, image, x):
        # Call the parent class (Sprite) constructor
        self.n = 0
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image.fill(color)
        # of rect.x and rect.y
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.y = 5
        self.rect.x = x
        '''
        for i in range(5):
            self.images.append(image)
            self.rect = self.images[i].get_rect()
            self.rect.y = 100
            self.rect.x = 100 + 75 * i
        '''

    def update(self, screen_width, score):
        """ Called each frame. """
        self.rect.x = 500 

