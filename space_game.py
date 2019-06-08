import pygame
import random
import player
import collectible
import os.path

def add_sprites(block_num, block_list, all_sprites_list, score):
    for i in range(block_num):
        # This represents a block
        if score % 5 ==  0 and score != 0:
            block = collectible.Collectible(False, 20, 15, HOLE, screen_width)
        else:
            block = collectible.Collectible(True, 20, 15, ICE_CREAM, screen_width)
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
SCOREBOARD_COLOR = (237, 252, 251)
 
# Initialize Pygame
pygame.init()
 
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

# Set the height and width of the screen
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode([screen_width, screen_height], pygame.FULLSCREEN)
 
DOGGO = pygame.image.load(os.path.join('images', 'doggo.png')).convert_alpha()
ICE_CREAM = pygame.image.load(os.path.join('images', 'ice-cream.png')).convert_alpha()
HOLE = pygame.image.load(os.path.join('images', 'hole.png')).convert_alpha()

background = pygame.image.load(os.path.join('images', 'space.jpg'))
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 

block_num = 3

add_sprites(block_num, block_list, all_sprites_list, 0)

 
player = player.Player(True, 20, 15, DOGGO, screen_width)
all_sprites_list.add(player)

# Text test
pygame.font.init()
myfont = pygame.font.SysFont('Fira Mono Medium', 30)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
health= 5
scoreSurface = myfont.render("Score: " + str(score), False, SCOREBOARD_COLOR)
healthSurface = myfont.render("Health: " + str(health), False, SCOREBOARD_COLOR)
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

    # Clear the screen
    screen.blit(background, (0, 0))
 
    # Calls update() method on every sprite in the list
    all_sprites_list.update(screen_width, score)
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        if block.value:
            score += 1
        else:
            health -= 1
        scoreSurface = myfont.render("Score: " + str(score), False, SCOREBOARD_COLOR)
        healthSurface = myfont.render("Health: " + str(health), False, SCOREBOARD_COLOR)
        # Reset block to the top of the screen to fall again.
        block.reset_pos(screen_width)
        if score <= 12:
            add_sprites(1, block_list, all_sprites_list, score)
        if health == 0:
            done = True
    # Draw all the spites
    all_sprites_list.draw(screen)

    # Text logic
    screen.blit(scoreSurface, (5, 5))
    screen.blit(healthSurface, (865, 5))
    # Limit to 30 frames per second
    clock.tick(30)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
