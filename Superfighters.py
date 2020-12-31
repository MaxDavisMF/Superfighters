# Import Libraries
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

# Images
player_still_image_right= pygame.image.load("standright_1.png").convert()
player_still_image_right = pygame.transform.scale(player_still_image_right, (37, 63))
player_still_image_left = pygame.image.load("standleft_1.png").convert()
player_still_image_left = pygame.transform.scale(player_still_image_left, (37, 63))
player_walk_right1 = pygame.image.load("walkright_1.png").convert()
player_walk_right1 = pygame.transform.scale(player_walk_right1, (42, 60))
player_walk_right2 = pygame.image.load("walkright_3.png").convert()
player_walk_right2 = pygame.transform.scale(player_walk_right2, (48, 60))
player_walk_left1 = pygame.image.load("walkleft_1.png").convert()
player_walk_left1 = pygame.transform.scale(player_walk_left1, (42, 60))
player_walk_left2 = pygame.image.load("walkleft_3.png").convert()
player_walk_left2 = pygame.transform.scale(player_walk_left2, (42, 60))


# create lists to cycle through for animations
walkright = [player_walk_right1, player_walk_right2]
walkleft = [player_walk_left1, player_walk_left2]
# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_still_image_right
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # Programe not registering self.rect. values at all
        self.rect.x = 305
        self.rect.y = 15
        self.walkanimationnum = 0
        self.state = "still"
        # direction will be used to decide which image should be used when moving/ standing in different directions
        self.direction = "right"
        self.xspeed = 0

    def update(self, speed, timer):
        self.rect.x += speed
        if speed == 5 or speed == -5:
            if timer % 15 == 0:
                self.walkanimationnum += 1
                if self.walkanimationnum == 2:
                    self.walkanimationnum = 0
            if speed == 5:
                self.image = walkright[self.walkanimationnum]
            if speed == -5:
                self.image = walkleft[self.walkanimationnum]
        elif speed == 0:
            if self.direction == "right":
                self.image = player_still_image_right
            elif self.direction == "left":
                self.image = player_still_image_left
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    #def fall(self):

# Instantiate Objects
player1 = Player()

# Set up sprite lists
all_sprites_list = pygame.sprite.Group()

# Adding Objects to sprite lists
all_sprites_list.add(player1)
# variables
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
                player1.state = "walk"
                player1.direction = "left"
            elif event.key == pygame.K_RIGHT:
                player1_x_speed = 5
                player1.state = "walk"
                player1.direction = "right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1_x_speed = 0
                player1.state = "still"
            elif event.key == pygame.K_RIGHT:
                player1_x_speed = 0
                player1.state = "still"
    player1.update(player1_x_speed, timer)


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
