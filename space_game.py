import pygame
import random
# Sprite class for blocks + player
import sprites
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
AYAYA = pygame.image.load('AYAYA.png').convert_alpha()
HYPER = pygame.image.load('HYPER.png').convert_alpha()
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = sprites.Block(BLACK, 20, 15, AYAYA, screen_width)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = sprites.Player(RED, 20, 15, HYPER, screen_width)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Calls update() method on every sprite in the list
    all_sprites_list.update(screen_width)
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
 
        # Reset block to the top of the screen to fall again.
        block.reset_pos(screen_width)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Limit to 20 frames per second
    clock.tick(30)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()

