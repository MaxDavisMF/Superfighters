
# Import Libraries
import pygame
import random
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
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
player_walk_right1 = pygame.transform.scale(player_walk_right1, (42, 63))
player_walk_right2 = pygame.image.load("walkright_3.png")
player_walk_right2 = pygame.transform.scale(player_walk_right2, (42, 63))
player_walk_left1 = pygame.image.load("walkleft_1.png")
player_walk_left1 = pygame.transform.scale(player_walk_left1, (42, 63))
player_walk_left2 = pygame.image.load("walkleft_3.png")
player_walk_left2 = pygame.transform.scale(player_walk_left2, (42, 63))
player_jump_right = pygame.image.load("jumpright.png")
player_jump_right = pygame.transform.scale(player_jump_right, (42, 63))
player_jump_left = pygame.image.load("jumpleft.png")
player_jump_left = pygame.transform.scale(player_jump_left, (42, 63))
player_duck_left = pygame.image.load("duckleft.png")
player_duck_left = pygame.transform.scale(player_duck_left, (33, 45))
player_duck_right = pygame.image.load("duckright.png")
player_duck_right = pygame.transform.scale(player_duck_right, (33, 45))
player_pistol_right = pygame.image.load("pistolaimright.png")
player_pistol_right = pygame.transform.scale(player_pistol_right, (50, 63))
player_pistol_left = pygame.image.load("pistolaimleft.png")
player_pistol_left = pygame.transform.scale(player_pistol_left,  (50, 63))
# Fonts
font = pygame.font.Font(None, 50)

# create lists to cycle through for animations
walkright = [player_walk_right1, player_walk_right2]
walkleft = [player_walk_left1, player_walk_left2]
# Classes
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 4))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"
    def update(self):
        if self.direction == "right":
            self.rect.x = self.rect.x + 8
        elif self.direction == "left":
            self.rect.x -= 8
        # This piece of code seems to make the bullet dissapear straight away, don't know what the bullet is colliding with
        bullet_collision_list = pygame.sprite.spritecollide(self, obstacles, False)
        if bullet_collision_list:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = player_still_image_right
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.walkanimationnum = 0
        self.state = "still"
        # direction will be used to decide which image should be used when moving/standing in different directions
        self.direction = "right"
        self.speedx = 0
        self.speedy = 0
        self.supported = False
        #Supported decides whether or not to make the player fall
        self.accy = 0.163
        self.accx = 0
        # 9.8 / 60, to model realistic acceleration
        self.crouching = True
        self.uncrouching = False
        # Used to decide if player is crouching or uncrouching (changing state) to adjust coords of sprite. Crouching set to True as next time it is used the sprite will be crouching
        self.crouched = False
        #Was crocuhed used to readjust sprite location if crouching after shooting
        self.wascrouched = False
        self.health = 100
        self.gun = "pistol"
        self.shooting = False
        # Used to decide if the player was aiming when the n key is released, so that a bullet is not spawned every frame after it has been released
        self.aiming = True


    def update(self, timer):
        if self.shooting == False:
            if self.crouched == True:
                self.speedx = 0
            # Update sideways movement
            self.rect.x = self.rect.x + self.speedx
            # Update whether player is falling or not
            if not self.supported:
                self.accy = 0.163
            elif self.supported:
                self.accy = 0
            # Walking animation
            if self.state == "walk":
                if timer % 15 == 0:
                    self.walkanimationnum += 1
                    if self.walkanimationnum == 2:
                        self.walkanimationnum = 0
                if self.speedx == 5:
                    self.image = walkright[self.walkanimationnum]
                if self.speedx == -5:
                    self.image = walkleft[self.walkanimationnum]
            # Reset sprites if no longer moving
            elif self.state == "still":
                if self.direction == "right":
                    self.image = player_still_image_right
                elif self.direction == "left":
                    self.image = player_still_image_left
            # Crouch sprite if crouching
            elif self.state == "crouched":
                if self.direction == "right":
                    self.image = player_duck_right
                elif self.direction == "left":
                    self.image = player_duck_left
            # Jump sprite
            elif self.state == "jump":
                if self.direction == "right":
                    self.image = player_jump_right
                elif self.direction== "left":
                    self.image= player_jump_left
            # Acceleration and downwards moving if falling
            if self.supported == False:
                self.speedy += self.accy
                self.rect.y += self.speedy
            # Check if floor has been hit
            player_floor_collision_list = pygame.sprite.spritecollide(self, floors, False)
            # If it has and player was falling, stop falling and place player on top of floor
            if player_floor_collision_list and self.speedy > 0:
                self.speedy = 0
                self.supported = True
                if self.speedx != 0:
                    self.state = "walk"
                else:
                    self.state = "still"
                for floor in player_floor_collision_list:
                    # + 63 to adjust for player height
                    self.rect.y = (floor.rect.y - 63)

        elif self.shooting == True:
            if self.direction == "right":
                self.image = player_pistol_right
            elif self.direction == "left":
                self.image = player_pistol_left
        self.image.set_colorkey(BLACK)

class Hardfloor(pygame.sprite.Sprite):
    def __init__(self, xsize, ysize, xcoord, ycoord):
        super().__init__()
        self.image = pygame.Surface((xsize, ysize))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.x = xcoord
        self.rect.y = ycoord

class Titleimage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Menu_image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.x = 150
        self.rect.y = 25



# Instantiate Objects
player1 = Player(900, 650)
player2 = Player(100, 650)
titlepic = Titleimage()
map1floor = Hardfloor(1000, 100, 0, 650)
# Set up sprite lists
all_sprites_list = pygame.sprite.Group()
floors = pygame.sprite.Group()
hard_floors = pygame.sprite.Group()
bullet_sprite_list = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
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
                Map1 = True
                #Set Map1 to true so that i can develop the first map, there will be the option to choose a map late ron
    if Multiplayer:
        if Setup:
            Setup = False
            all_sprites_list.empty()
            all_sprites_list.add(player1)
            all_sprites_list.add(player2)
            all_sprites_list.add(map1floor)
            if Map1:
                all_sprites_list.add(map1floor)
                hard_floors.add(map1floor)
                floors.add(map1floor)
                obstacles.add(map1floor)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player1.crouched == False:
                player1.speedx = -5
                player1.state = "walk"
                player1.direction = "left"
            elif event.key == pygame.K_RIGHT and player1.crouched == False:
                player1.speedx = 5
                player1.state = "walk"
                player1.direction = "right"
            elif event.key == pygame.K_UP and player1.supported == True:
                player1.speedy = -5
                player1.supported = False
                player1.state = "jump"
            elif event.key == pygame.K_DOWN and player1.supported == True and player1.shooting == False:
                player1.state = "crouched"
                player1.crouched = True
                player1.uncrouching = True
                if player1.crouching == True:
                    player1.rect.y += 18
                    player1.crouching = False
            elif event.key == pygame.K_n:
                player1.aiming = True
                player1.shooting = True
                # This is to adjust the coordinates of the player sprite so that he stands correctly
                if player1.crouched == True:
                    player1.crouched = False
                    # Remember that the player was crocuhed
                    player1.wascrouched = True
                    # Adjust coords of player
                    player1.rect.y -= 18
                    # So that the player is not shifted up again if the player lets go of the down key
                    player1.uncrouching = False
                    #To readjust the sprite when the player stops shooting.
                    player1.crouching = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player1.crouched == False:
                player1.speedx = 0
                player1.state = "still"
            elif event.key == pygame.K_RIGHT and player1.crouched == False:
                player1.speedx = 0
                player1.state = "still"
            elif event.key == pygame.K_DOWN:
                if player1.uncrouching == True:
                    player1.rect.y -= 18
                    player1.uncrouching = False
                player1.state = "still"
                player1.crouching = True
                player1.crouched = False
                player1.wascrouched = False
            elif event.key == pygame.K_n:
                if player1.aiming == True:
                    player1.aiming = False
                    if player1.direction == "right":
                        bullet = Bullet((player1.rect.x + 50), (player1.rect.y + 9))
                        bullet.direction = "right"
                        all_sprites_list.add(bullet)
                        bullet_sprite_list.add(bullet)
                    elif player1.direction == "left":
                        bullet = Bullet(player1.rect.x, player1.rect.y + 9)
                        bullet.direction = "left"
                        all_sprites_list.add(bullet)
                        bullet_sprite_list.add(bullet)
                player1.shooting = False
                if player1.wascrouched == True:
                    if player1.crouching == True:
                        player1.rect.y += 18
                        player1.wascrouched = False
                        player1.crouched = True
                        player1.crouching = False
                        player1.uncrouching = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and player2.crouched == False:
                player2.speedx = -5
                player2.state = "walk"
                player2.direction = "left"
            elif event.key == pygame.K_d and player2.crouched == False:
                player2.speedx = 5
                player2.state = "walk"
                player2.direction = "right"
            elif event.key == pygame.K_w and player2.supported == True:
                player2.speedy = -5
                player2.supported = False
                player2.state = "jump"
            elif event.key == pygame.K_s and player2.supported == True and player2.shooting == False:
                player2.state = "crouched"
                player2.crouched = True
                player2.uncrouching = True
                if player2.crouching == True:
                    player2.rect.y += 18
                    player2.crouching = False
            elif event.key == pygame.K_2:
                player2.aiming = True
                player2.shooting = True
                # This is to adjust the coordinates of the player sprite so that he stands correctly
                if player2.crouched == True:
                    player2.crouched = False
                    # Remember that the player was crocuhed
                    player2.wascrouched = True
                    # Adjust coords of player
                    player2.rect.y -= 18
                    # So that the player is not shifted up again if the player lets go of the down key
                    player2.uncrouching = False
                    #To readjust the sprite when the player stops shooting.
                    player2.crouching = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player2.crouched == False:
                player2.speedx = 0
                player2.state = "still"
            elif event.key == pygame.K_d and player2.crouched == False:
                player2.speedx = 0
                player2.state = "still"
            elif event.key == pygame.K_s:
                if player2.uncrouching == True:
                    player2.rect.y -= 18
                    player2.uncrouching = False
                player2.state = "still"
                player2.crouching = True
                player2.crouched = False
                player2.wascrouched = False
            elif event.key == pygame.K_2:
                if player2.aiming == True:
                    player2.aiming = False
                    if player2.direction == "right":
                        bullet = Bullet((player2.rect.x + 50), (player2.rect.y + 9))
                        bullet.direction = "right"
                        all_sprites_list.add(bullet)
                        bullet_sprite_list.add(bullet)
                    elif player2.direction == "left":
                        bullet = Bullet(player2.rect.x, player2.rect.y + 9)
                        bullet.direction = "left"
                        all_sprites_list.add(bullet)
                        bullet_sprite_list.add(bullet)
                player2.shooting = False
                if player2.wascrouched == True:
                    if player2.crouching == True:
                        player2.rect.y += 18
                        player2.wascrouched = False
                        player2.crouched = True
                        player2.crouching = False
                        player2.uncrouching = True

        player1.update(timer)
        player2.update(timer)
        for bullet in bullet_sprite_list:
            bullet.update()

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
