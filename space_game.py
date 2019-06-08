import pygame
import random
import user
import collectible
import os.path
import time
import life

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
 
DOGGO = pygame.image.load(os.path.join('images', 'doggo1.png')).convert_alpha()
ICE_CREAM = pygame.image.load(os.path.join('images', 'ice-cream1.png')).convert_alpha()
HOLE = pygame.image.load(os.path.join('images', 'hole1.png')).convert_alpha()
HEALTH = pygame.image.load(os.path.join('images', 'health.png')).convert_alpha()


gameover = pygame.image.load(os.path.join('images', 'game-over.jpg'))
gameover_end = pygame.image.load(os.path.join('images', 'game-over-end.jpg'))
background = pygame.image.load(os.path.join('images', 'space.jpg'))

finished = False
while not finished:
    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    block_list = pygame.sprite.Group()
     
    # This is a list of every sprite. All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()
    health_sprites_list = pygame.sprite.Group()

    block_num = 3

    add_sprites(block_num, block_list, all_sprites_list, 0)

    for i in range(5):
        health_sprites_list.add(life.Health(HEALTH, 650 + 60 * i))
     
    player = user.Player(True, 20, 15, DOGGO, screen_width)
    all_sprites_list.add(player)

    pygame.mixer.init()
    

    # Text test
    pygame.font.init()
    myfont = pygame.font.SysFont('Fira Mono Medium', 30)
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    with open('highscore.txt') as f:
        line = f.readline()
        highscore = 0
        if line:
            highscore = int(line)
     
    score = 0
    health= 5
    scoreSurface = myfont.render('Score: ' + str(score) + '        Highscore: ' + str(highscore), False, SCOREBOARD_COLOR)
    healthSurface = myfont.render("Health: " + str(health), False, SCOREBOARD_COLOR)
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        screen.blit(gameover_end, (0, 0))
                        pygame.display.flip()
                        time.sleep(2)
                        done = True
                        finished = True

        # Clear the screen
        if done != True:
            screen.blit(background, (0, 0))
     
        # Calls update() method on every sprite in the list
        all_sprites_list.update(screen_width, score)
     
        # See if the player block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
     
        # Check the list of collisions.
        for block in blocks_hit_list:
            if block.value:
                score += 1
                pygame.mixer.music.load(os.path.join('music', 'eat.wav'))
                pygame.mixer.music.play()
            else:
                health -= 1
                pygame.mixer.music.load(os.path.join('music', 'scream.wav'))
                pygame.mixer.music.play()
                for h in health_sprites_list:
                    health_sprites_list.remove(h)
                    break
            scoreSurface = myfont.render('Score: ' + str(score) + '        Highscore: ' + str(highscore), False, SCOREBOARD_COLOR)
            # Reset block to the top of the screen to fall again.
            block.reset_pos(screen_width)
            if score % 100 == 0 and score != 0:
                add_sprites(1, block_list, all_sprites_list, score)
            if score <= 12:
                add_sprites(1, block_list, all_sprites_list, score)
            if health == 0:
                screen.blit(gameover, (0, 0))
                highscoreSurface = myfont.render('New highscore: ' + str(score), False, SCOREBOARD_COLOR)
                if score > highscore:
                    screen.blit(highscoreSurface, (360, 310))
                    highscore = score
                    with open('highscore.txt', 'w') as f:
                            f.write(str(highscore))
                pygame.display.flip()
                pygame.mixer.music.load(os.path.join('music', 'lose.wav'))
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                done = True
        # Draw all the sprites
        all_sprites_list.draw(screen)

        health_sprites_list.draw(screen)

        # Text logic
        screen.blit(scoreSurface, (5, 5))
        # Limit to 30 frames per second
        clock.tick(30)
     
        # Go ahead and update the screen with what we've drawn.
        if done != True:
            pygame.display.flip()
pygame.quit()
