#Import Libraries
import pygame
import random
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the screen up
size = (1000, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Superfighters")

#Images
player_still_image= pygame.image.load("standright_1.png").convert()
player_walk_right1 = pygame.image.load("walkright_1.png").convert()
player_walk_right1 = pygame.transform.scale(player_walk_right1, (42, 60))
#player_walk_right2 = pygame.image.load("walkright_2.png").convert()
#player_walk_right2 = pygame.transform.scale(player_walk_right2, (27, 60))
player_walk_right3 = pygame.image.load("walkright_3.png").convert()
player_walk_right3 = pygame.transform.scale(player_walk_right3, (48, 60))
#player_walk_right4 = pygame.image.load("walkright_4.png").convert()

#create lists to cycle through for animations
walkright = [player_walk_right1, player_walk_right3]
#Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_still_image
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(player_still_image, (37, 63))
        self.rect = self.image.get_rect()
        self.rect.x = 45
        self.rect.y = 15
        self.walkanimationnum = 0

    def move(self, speed, timer):
        self.rect.x += player1_x_speed
        if timer % 3 == 0:
            self.walkanimationnum += 1
            if self.walkanimationnum == 2:
                self.walkanimationnum = 0
        if speed == 5:
            self.image = walkright[self.walkanimationnum]
            self.image.set_colorkey(BLACK)

#Instantiate Objects
player1 = Player()

#Set up sprite lists
all_sprites_list = pygame.sprite.Group()

#Adding Objects to sprite lists
all_sprites_list.add(player1)
#variables
player1_x_speed = 0
timer = 0
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # --- Game logic should go here
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1_x_speed = -5
            elif event.key == pygame.K_RIGHT:
                player1_x_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1_x_speed = 0
            elif event.key == pygame.K_RIGHT:
                player1_x_speed = 0

    player1.move(player1_x_speed, timer)


    screen.fill(WHITE)
    
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

    timer = timer + 1
    if timer % 60 == 0:
        timer = 0

# Close the window and quit.
pygame.quit()
