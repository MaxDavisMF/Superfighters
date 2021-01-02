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
Menu_image = pygame.image.load("Home_screen_title.png").convert()
Menu_image = pygame.transform.scale(Menu_image, (700, 150))
background_image = pygame.image.load("citybackground.png").convert()
background_image = pygame.transform.scale(background_image, (1000, 750))

player_still_image_right = pygame.image.load("standright_1.png")
player_still_image_right = pygame.transform.scale(player_still_image_right, (37, 63))
player_still_image_left = pygame.image.load("standleft_1.png")
player_still_image_left = pygame.transform.scale(player_still_image_left, (37, 63))
player_walk_right1 = pygame.image.load("walkright_1.png")
player_walk_right1 = pygame.transform.scale(player_walk_right1, (42, 60))
player_walk_right2 = pygame.image.load("walkright_3.png")
player_walk_right2 = pygame.transform.scale(player_walk_right2, (48, 60))
player_walk_left1 = pygame.image.load("walkleft_1.png")
player_walk_left1 = pygame.transform.scale(player_walk_left1, (42, 60))
player_walk_left2 = pygame.image.load("walkleft_3.png")
player_walk_left2 = pygame.transform.scale(player_walk_left2, (42, 60))

# Fonts
font = pygame.font.Font(None, 50)

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
        self.rect.x = 100
        self.rect.y = 100
        self.walkanimationnum = 0
        self.state = "still"
        # direction will be used to decide which image should be used when moving/standing in different directions
        self.direction = "right"
        self.speedx = 0

    def update(self, timer):
        self.rect.x = self.rect.x + self.speedx
        if self.speedx == 5 or self.speedx == -5:
            if timer % 15 == 0:
                self.walkanimationnum += 1
                if self.walkanimationnum == 2:
                    self.walkanimationnum = 0
            if self.speedx == 5:
                self.image = walkright[self.walkanimationnum]
            if self.speedx == -5:
                self.image = walkleft[self.walkanimationnum]
        elif self.speedx == 0:
            if self.direction == "right":
                self.image = player_still_image_right
            elif self.direction == "left":
                self.image = player_still_image_left
        self.image.set_colorkey(BLACK)

class Titleimage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Menu_image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.x = 150
        self.rect.y = 25



# Instantiate Objects
player1 = Player()
titlepic = Titleimage()
# Set up sprite lists
all_sprites_list = pygame.sprite.Group()

# Adding Objects to sprite lists
# all_sprites_list.add(player1)
# variables
timer = 0
done = False
Menu = True
setup = True
Multiplayer = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    if Menu:
        if setup:
            setup = False
            all_sprites_list.empty()
            all_sprites_list.add(titlepic)
            Multiplayertext = font.render("Press 1 to play Multiplayer!", True, WHITE)

        screen.fill(BLACK)
        screen.blit(Multiplayertext, [275, 250])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                Menu = False
                Multiplayer = True
                Setup = True
    if Multiplayer:
        if Setup:
            Setup = False
            all_sprites_list.empty()
            all_sprites_list.add(player1)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.speedx = -5
                player1.state = "walk"
                player1.direction = "left"
            elif event.key == pygame.K_RIGHT:
                player1.speedx = 5
                player1.state = "walk"
                player1.direction = "right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1.speedx = 0
                player1.state = "still"
            elif event.key == pygame.K_RIGHT:
                player1.speedx = 0
                player1.state = "still"
        player1.update(timer)

        screen.blit(background_image, (0, 0))

        # --- Limit to 60 frames per second
        clock.tick(60)

        timer = timer + 1
        if timer % 60 == 0:
            timer = 0

    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
# Close the window and quit.
pygame.quit()


