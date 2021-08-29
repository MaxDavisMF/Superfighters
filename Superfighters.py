# Import Libraries
import pygame
import random
import decimal
import math
import shelve

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
PLATFORM = (192, 192, 192)
pygame.init()

# Set the screen up
size = (1000, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Superfighters")
# Images
Menu_image = pygame.image.load("Home_screen_title.png").convert()
Menu_image = pygame.transform.scale(Menu_image, (700, 150))
background_image1 = pygame.image.load("citybackground.png").convert()
background_image1 = pygame.transform.scale(background_image1, (1000, 750))
background_image2 = pygame.image.load("Darkcitybackground.png").convert()
background_image2 = pygame.transform.scale(background_image2, (1000, 750))
background_image3 = pygame.image.load("Spacebackground.png").convert()
background_image3 = pygame.transform.scale(background_image3, (1000, 750))

Ladderimage = pygame.image.load("Laddersprite.png").convert()
Ladderimage = pygame.transform.scale(Ladderimage, (40, 100))

player_still_image_right = pygame.image.load("standright_1.png")
player_still_image_right = pygame.transform.scale(player_still_image_right, (37, 63))
player_still_image_left = pygame.image.load("standleft_1.png")
player_still_image_left = pygame.transform.scale(player_still_image_left, (37, 63))

player_still_image_right_red = pygame.image.load("standright_1red.png")
player_still_image_right_red = pygame.transform.scale(player_still_image_right_red, (37, 63))
player_still_image_left_red = pygame.image.load("standleft_1red.png")
player_still_image_left_red = pygame.transform.scale(player_still_image_left_red, (37, 63))

player_walk_right1 = pygame.image.load("walkright_1.png")
player_walk_right1 = pygame.transform.scale(player_walk_right1, (42, 63))
# player_walk_right2 = pygame.image.load("walkright_2.png")
# player_walk_right2 = pygame.transform.scale(player_walk_right2, (42, 63))
player_walk_right3 = pygame.image.load("walkright_3.png")
player_walk_right3 = pygame.transform.scale(player_walk_right3, (42, 63))
player_walk_left1 = pygame.image.load("walkleft_1.png")
player_walk_left1 = pygame.transform.scale(player_walk_left1, (42, 63))
# player_walk_left2 = pygame.image.load("walkleft_2.png")
# player_walk_left2 = pygame.transform.scale(player_walk_left2, (42, 63))
player_walk_left3 = pygame.image.load("walkleft_3.png")
player_walk_left3 = pygame.transform.scale(player_walk_left3, (42, 63))

player_walk_right1_red = pygame.image.load("walkright_1red.png")
player_walk_right1_red = pygame.transform.scale(player_walk_right1_red, (42, 63))
player_walk_right3_red = pygame.image.load("walkright_3red.png")
player_walk_right3_red = pygame.transform.scale(player_walk_right3_red, (42, 63))
player_walk_left1_red = pygame.image.load("walkleft_1red.png")
player_walk_left1_red = pygame.transform.scale(player_walk_left1_red, (42, 63))
player_walk_left3_red = pygame.image.load("walkleft_3red.png")
player_walk_left3_red = pygame.transform.scale(player_walk_left3_red, (42, 63))

player_jump_right = pygame.image.load("jumpright.png")
player_jump_right = pygame.transform.scale(player_jump_right, (42, 63))
player_jump_left = pygame.image.load("jumpleft.png")
player_jump_left = pygame.transform.scale(player_jump_left, (42, 63))

player_jump_right_red = pygame.image.load("jumprightred.png")
player_jump_right_red = pygame.transform.scale(player_jump_right_red, (42, 63))
player_jump_left_red = pygame.image.load("jumpleftred.png")
player_jump_left_red = pygame.transform.scale(player_jump_left_red, (42, 63))

player_duck_left = pygame.image.load("duckleft.png")
player_duck_left = pygame.transform.scale(player_duck_left, (33, 45))
player_duck_right = pygame.image.load("duckright.png")
player_duck_right = pygame.transform.scale(player_duck_right, (33, 45))

player_duck_left_red = pygame.image.load("duckleftred.png")
player_duck_left_red = pygame.transform.scale(player_duck_left_red, (33, 45))
player_duck_right_red = pygame.image.load("duckrightred.png")
player_duck_right_red = pygame.transform.scale(player_duck_right_red, (33, 45))

player_pistol_right = pygame.image.load("pistolaimright.png")
player_pistol_right = pygame.transform.scale(player_pistol_right, (50, 63))
player_pistol_left = pygame.image.load("pistolaimleft.png")
player_pistol_left = pygame.transform.scale(player_pistol_left, (50, 63))

player_pistol_right_red = pygame.image.load("pistolaimrightred.png")
player_pistol_right_red = pygame.transform.scale(player_pistol_right_red, (50, 63))
player_pistol_left_red = pygame.image.load("pistolaimleftred.png")
player_pistol_left_red = pygame.transform.scale(player_pistol_left_red, (50, 63))

player_magnum_right = pygame.image.load("magnumaimright.png")
player_magnum_right = pygame.transform.scale(player_magnum_right, (50, 63))
player_magnum_left = pygame.image.load("magnumaimleft.png")
player_magnum_left = pygame.transform.scale(player_magnum_left, (50, 63))

player_magnum_right_red = pygame.image.load("magnumaimrightred.png")
player_magnum_right_red = pygame.transform.scale(player_magnum_right_red, (50, 63))
player_magnum_left_red = pygame.image.load("magnumaimleftred.png")
player_magnum_left_red = pygame.transform.scale(player_magnum_left_red, (50, 63))

player_rifle_right = pygame.image.load("rifleaimright.png")
player_rifle_right = pygame.transform.scale(player_rifle_right, (50, 63))
player_rifle_left = pygame.image.load("rifleaimleft.png")
player_rifle_left = pygame.transform.scale(player_rifle_left, (50, 63))


player_ladder_climb = pygame.image.load("climbladder.png")
player_ladder_climb = pygame.transform.scale(player_ladder_climb, (35, 63))

magnum = pygame.image.load("magnum.png")
magnum = pygame.transform.scale(magnum, (30, 18))
pistol = pygame.image.load("pistol.png")
pistol = pygame.transform.scale(pistol, (20, 18))
rifle = pygame.image.load("rifle.png")
rifle = pygame.transform.scale(rifle, (45, 18))

# Fonts
font = pygame.font.Font(None, 50)
statfont = pygame.font.Font(None, 25)
# create lists to cycle through for animations
walkright = [player_walk_right1, player_walk_right3]
walkleft = [player_walk_left1, player_walk_left3]
walkrightred = [player_walk_right1_red, player_walk_right3_red]
walkleftred = [player_walk_left1_red, player_walk_left3_red]
# Load top scores
L1 = open("L1highscore.txt", "r")
L1topscore = (L1.read())
L1.close
L2 = open("L2highscore.txt", "r")
L2topscore = (L2.read())
L2.close
L3 = open("L3highscore.txt", "r")
L3topscore = (L3.read())
L3.close


# Classes
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, spread, ydirection):
        super().__init__()
        self.image = pygame.Surface((6, 4))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"
        self.directiony = ydirection
        self.spread = spread
        self.timer = 0
        self.gun = "pistol"
        # Timer used to time spread

    def update(self):
        self.timer += 1
        if self.direction == "right":
            self.rect.x = self.rect.x + 8
        elif self.direction == "left":
            self.rect.x -= 8
        if self.timer == self.spread:
            self.timer = 0
            if self.directiony == True:
                self.rect.y += 1
            else:
                self.rect.y -= 1
        # This piece of code seems to make the bullet dissapear straight away, don't know what the bullet is colliding with
        # FIXED earlier but forgot to document, bullet was colliding with player shooting it instantly due to faulty spawn coords
        # bullet_collision_list = pygame.sprite.spritecollide(self, obstacles, False)
        # if bullet_collision_list:
        #    self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, ypos):
        super().__init__()
        self.image = player_still_image_left_red
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 1050
        self.rect.y = ypos
        self.health = 15
        self.walkanimationnum = 0
        self.jumping = False
        self.state = "still"
        # direction will be used to decide which image should be used when moving/standing in different directions
        self.direction = "left"
        self.speedx = -2
        self.speedy = 0
        self.supported = False
        # Supported decides whether or not to make the enemy fall
        self.accy = 0.16
        self.accx = 0
        self.gun = "pistol"
        self.ammo = 12
        self.shooting = False
        self.timer = 0

    def update(self):
        self.timer += 1
        self.rect.x += self.speedx
        if not self.supported:
            self.speedy += self.accy
            self.rect.y += self.speedy
        # This is the same code that was use in the Player update function to allow the player to land on floors. Explained there
        player_floor_collision_list = pygame.sprite.spritecollide(self, floors, False)
        if not player_floor_collision_list:
            self.supported = False
        if player_floor_collision_list and self.speedy > 0:
            for floor in player_floor_collision_list:
                if self.rect.y < (floor.rect.y - 58) or (self.speedy > 5 and self.rect.y < (floor.rect.y - 50)):
                    if self.speedx != 0:
                        self.state = "walk"
                    self.speedy = 0
                    self.supported = True
                    self.jumping = False
                    # + 63 to adjust for player height
                    self.rect.y = (floor.rect.y - 63)

        if self.jumping == False:
            if self.timer % 10 == 0:
                self.timer = 0
                self.walkanimationnum += 1
                if self.walkanimationnum == 2:
                    self.walkanimationnum = 0
                self.image = walkleftred[self.walkanimationnum]
            jump = random.randrange(0, 30)
            if Level == "1" or "2":
                if player1.rect.y == self.rect.y:
                    if (jump == 1 or jump == 2 or jump == 3) and self.supported == True:
                        self.jumping = True
                        self.state = "jumping"
                        self.speedy = -5.4
                else:
                    if jump == 1 and self.supported == True:
                        self.jumping = True
                        self.state = "jumping"
                        self.speedy = -5.4
            if Level == "3":
                if (jump == 1 or jump == 2 or jump == 3) and self.supported == True:
                    self.jumping = True
                    self.state = "jumping"
                    self.speedy = -5.4

        else:
            self.image = player_jump_left_red


class Pickups(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, gunnum):
        super().__init__()
        if gunnum == 0:
            self.image = pistol
            self.type = "pistol"
        elif gunnum == 1:
            self.image = magnum
            self.type = "magnum"
        elif gunnum ==2:
            self.image = rifle
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


class Player(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = player_still_image_right
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.health = 100
        self.walkanimationnum = 0
        self.state = "still"
        # direction will be used to decide which image should be used when moving/standing in different directions
        self.direction = "right"
        self.speedx = 0
        self.speedy = 0
        self.supported = False
        # Supported decides whether or not to make the player fall
        self.accy = 0.16
        self.accx = 0
        self.crouching = True
        self.uncrouching = False
        # Used to decide if player is crouching or uncrouching (changing state) to adjust coords of sprite. Crouching set to True as next time it is used the sprite will be crouching
        self.crouched = False
        # Was crocuhed used to readjust sprite location if crouching after shooting
        self.wascrouched = False
        self.gun = "pistol"
        self.ammo = 12
        self.shooting = False
        # Used to decide if the player was aiming when the n key is released, so that a bullet is not spawned every frame after it has been released
        self.aiming = True
        # Dropping is used when the player drops through a soft floor
        self.dropping = False
        self.lives = 3
        self.climbing = False
        self.movingplatform = None

    def update(self, timer):
        if self.shooting == False:
            if self.crouched == True:
                self.speedx = 0
            # Update sideways movement
            self.rect.x = self.rect.x + self.speedx
            # Walking animation
            if self.state == "walk" and self.supported == True:
                if timer % 3 == 0:
                    self.walkanimationnum += 1
                    if self.walkanimationnum == 2:
                        self.walkanimationnum = 0
                if self.speedx > 0:
                    self.image = walkright[self.walkanimationnum]
                if self.speedx < 0:
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
                elif self.direction == "left":
                    self.image = player_jump_left
            # Acceleration and downwards moving if falling
            if self.supported == False:
                self.speedy += self.accy
                self.rect.y += self.speedy
            # If climbing
            if self.state == "climb":
                self.image = player_ladder_climb
            # Check if floor has been hit
            player_floor_collision_list = pygame.sprite.spritecollide(self, floors, False)
            # If it has and player was falling, stop falling and place player on top of floor
            if not player_floor_collision_list:
                self.supported = False
            if player_floor_collision_list and self.speedy > 0:
                for floor in player_floor_collision_list:
                    # This checks that the player is sufficiently high to "land" on the platform, so that he does not
                    # teleport up to it if the top of his head touches it
                    # The second part of the or statement allows the character to land on the platform if he is lower than the required hieght if
                    # he is falling fast enough. This is because I had a problem where the characters would fall
                    # so fast that he would miss the acceptable range for landing on the platform in 1 frame
                    # Note this may need to be improved later on by creating more speed categories with different windows since 5 and above is quite a large range of speeds,
                    # What works at 15 pixels a frane may look bad if the character is falling 5 pixels a frame
                    if self.rect.y < (floor.rect.y - 58) or (
                            self.speedy > 5 and self.rect.y < (floor.rect.y - 50)) and self.dropping == False:
                        if self.speedx != 0:
                            self.state = "walk"
                        else:
                            self.state = "still"
                        self.speedy = 0
                        self.supported = True
                        # + 63 to adjust for player height
                        self.rect.y = (floor.rect.y - 63)

            # Set self.supported to true so that the player moves up the ladder instead of instantly falling back down
            if self.state == "climb":
                self.supported = True

        # Stop the player shooting in mid air

        elif self.shooting == True:
            if self.gun == "pistol":
                if self.direction == "right":
                    self.image = player_pistol_right
                elif self.direction == "left":
                    self.image = player_pistol_left
            elif self.gun == "magnum":
                if self.direction == "right":
                    self.image = player_magnum_right
                elif self.direction == "left":
                    self.image = player_magnum_left
            elif self.gun == "rifle":
                if self.direction == "right":
                    self.image = player_rifle_right
                elif self.direction == "left":
                    self.image = player_rifle_left
        self.image.set_colorkey(BLACK)

        Player_hit_list = pygame.sprite.spritecollide(self, bullet_sprite_list, False)
        if Player_hit_list:
            for bullet in Player_hit_list:
                if bullet.gun == "pistol":
                    self.health -= 9
                elif bullet.gun == "magnum":
                    self.health -= 20
                bullet.kill()


class Hardfloor(pygame.sprite.Sprite):
    def __init__(self, xsize, ysize, xcoord, ycoord):
        super().__init__()
        self.image = pygame.Surface((xsize, ysize))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.x = xcoord
        self.rect.y = ycoord


class Softfloor(pygame.sprite.Sprite):
    def __init__(self, xsize, xcoord, ycoord):
        super().__init__()
        self.image = pygame.Surface((xsize, 5))
        self.image.fill(PLATFORM)
        self.rect = self.image.get_rect()
        self.rect.x = xcoord
        self.rect.y = ycoord

class Movingsoftfloor(pygame.sprite.Sprite):
    def __init__(self, xsize, xcoord, ycoord, direction, parameter1, parameter2, startdirection):
        super().__init__()
        self.image = pygame.Surface((xsize, 5))
        self.image.fill(PLATFORM)
        self.rect = self.image.get_rect()
        self.rect.x = xcoord
        self.rect.y = ycoord
        self.moving = False
        self.direction = direction
        # These parameters are the coords that the platform will move between. The following code ensures that parameter 1 is the larger coord
        if parameter1 < parameter2:
            Temp = parameter1
            parameter1 = parameter2
            parameter2 = Temp
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.currentdirection = startdirection

    def update(self):
        if self.direction == "y":
            if self.currentdirection == "up":
                if self.rect.y > self.parameter2:
                       self.rect.y -= 2
                else:
                       self.currentdirection = "down"
            if self.currentdirection == "down":
                if self.rect.y < self.parameter1:
                    self.rect.y += 2
                else:
                       self.currentdirection = "up"


class Titleimage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Menu_image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.x = 150
        self.rect.y = 25


class Ladder(pygame.sprite.Sprite):
    def __init__(self, xcoord, ycoord):
        super().__init__()
        self.image = Ladderimage
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.x = xcoord
        self.rect.y = ycoord


# These funtions will create the maps
# Map1:
def mapcreate(map):
    map1floor = Hardfloor(1000, 100, 0, 650)
    all_sprites_list.add(map1floor)
    floors.add(map1floor)
    obstacles.add(map1floor)
    if map == "1":
        map1softfloor1 = Softfloor(300, 50, 550)
        all_sprites_list.add(map1softfloor1)
        floors.add(map1softfloor1)
        obstacles.add(map1softfloor1)

        map1softfloor2 = Softfloor(300, 650, 550)
        all_sprites_list.add(map1softfloor2)
        floors.add(map1softfloor2)
        obstacles.add(map1softfloor2)

        map1softfloor3 = Softfloor(300, 350, 450)
        all_sprites_list.add(map1softfloor3)
        floors.add(map1softfloor3)
        obstacles.add(map1softfloor3)

        map1softfloor4 = Softfloor(300, 50, 350)
        all_sprites_list.add(map1softfloor4)
        floors.add(map1softfloor4)
        obstacles.add(map1softfloor4)

        map1softfloor5 = Softfloor(300, 650, 350)
        all_sprites_list.add(map1softfloor5)
        floors.add(map1softfloor5)
        obstacles.add(map1softfloor5)

    elif map == "2":
        map2hardwall1 = Hardfloor(50, 700, 0, 150)
        all_sprites_list.add(map2hardwall1)
        floors.add(map2hardwall1)
        obstacles.add(map2hardwall1)

        map2hardwall2 = Hardfloor(50, 700, 950, 150)
        all_sprites_list.add(map2hardwall2)
        floors.add(map2hardwall2)
        obstacles.add(map2hardwall2)

        map2softfloor1 = Softfloor(200, 50, 450)
        all_sprites_list.add(map2softfloor1)
        floors.add(map2softfloor1)
        obstacles.add(map2softfloor1)

        map2softfloor2 = Softfloor(200, 50, 250)
        all_sprites_list.add(map2softfloor2)
        floors.add(map2softfloor2)
        obstacles.add(map2softfloor2)

        map2softfloor3 = Softfloor(200, 750, 250)
        all_sprites_list.add(map2softfloor3)
        floors.add(map2softfloor3)
        obstacles.add(map2softfloor3)

        map2softfloor4 = Softfloor(200, 400, 450)
        all_sprites_list.add(map2softfloor4)
        floors.add(map2softfloor4)
        obstacles.add(map2softfloor4)

        map2softfloor5 = Softfloor(50, 650, 350)
        all_sprites_list.add(map2softfloor5)
        floors.add(map2softfloor5)
        obstacles.add(map2softfloor5)

        map2ladder1 = Ladder(150, 550)
        all_sprites_list.add(map2ladder1)
        ladders.add(map2ladder1)

        map2ladder2 = Ladder(150, 450)
        all_sprites_list.add(map2ladder2)
        ladders.add(map2ladder2)

        map2ladder3 = Ladder(80, 350)
        all_sprites_list.add(map2ladder3)
        ladders.add(map2ladder3)

        map2ladder4 = Ladder(80, 250)
        all_sprites_list.add(map2ladder4)
        ladders.add(map2ladder4)

        map2ladder5 = Ladder(450, 450)
        all_sprites_list.add(map2ladder5)
        ladders.add(map2ladder5)

        map2ladder6 = Ladder(450, 550)
        all_sprites_list.add(map2ladder6)
        ladders.add(map2ladder6)

    elif map == "3":
        map3softfloor1 = Movingsoftfloor(100, 150, 150, "y", 150, 600, "down")
        all_sprites_list.add(map3softfloor1)
        floors.add(map3softfloor1)
        movingfloors.add(map3softfloor1)
        obstacles.add(map3softfloor1)
        map3softfloor1.moving = True

        map3softfloor2 = Movingsoftfloor(100, 850, 550, "y", 150, 600, "up")
        all_sprites_list.add(map3softfloor2)
        floors.add(map3softfloor2)
        movingfloors.add(map3softfloor2)
        obstacles.add(map3softfloor2)
        map3softfloor2.moving = True

        map3softfloor3 = Softfloor(200, 400, 400)
        all_sprites_list.add(map3softfloor3)
        floors.add(map3softfloor3)
        obstacles.add(map3softfloor3)



# This function draws the Players stats at the top of the screen
def drawstats():
        pygame.draw.rect(screen, BLACK, [300, 0, 400, 150])
        player1title = statfont.render("Player 1", True, WHITE)
        screen.blit(player1title, [310, 10])
        player1health = statfont.render(str(player1.health), True, WHITE)
        screen.blit(player1health, [310, 45])
        player1gun = statfont.render(player1.gun, True, WHITE)
        screen.blit(player1gun, [310, 80])
        player1ammo = statfont.render(str(player1.ammo), True, WHITE)
        screen.blit(player1ammo, [310, 115])
        player2title = statfont.render("Player 2", True, WHITE)
        screen.blit(player2title, [510, 10])
        player2health = statfont.render(str(player2.health), True, WHITE)
        screen.blit(player2health, [510, 45])
        player2gun = statfont.render(player2.gun, True, WHITE)
        screen.blit(player2gun, [510, 80])
        player2ammo = statfont.render(str(player2.ammo), True, WHITE)
        screen.blit(player2ammo, [510, 115])

def drawstatsSP():
    pygame.draw.rect(screen, BLACK, [400, 0, 200, 75])
    player1lives = statfont.render("Lives: ", True, WHITE)
    player1lives2 = statfont.render(str(player1.lives), True, WHITE)
    screen.blit(player1lives, [410, 25])
    screen.blit(player1lives2, [470, 25])





# This function displays the winner after a game
def drawwinner(winner):
    if Multiplayer and Gameover:
        if winner == "Player 1":
            Winnertext = font.render("Player 1 Wins!", True, WHITE)
            screen.blit(Winnertext, [370, 150])
        elif winner == "Player 2":
            Winnertext = font.render("Player 2 Wins!", True, WHITE)
            screen.blit(Winnertext, [370, 150])
        nexttext = font.render("Press Space to return to menu", True, WHITE)
        screen.blit(nexttext, [250, 500])


# This function draws the results after a singleplayer level
def drawresult(result):
    if result == False:
        Resulttext = font.render("You Lose!", True, WHITE)
        screen.blit(Resulttext, [400, 200])
    if result == True:
        Resulttext = font.render("Level Complete!", True, WHITE)
        screen.blit(Resulttext, [370, 200])
    resettext = font.render("Press Space to return to the main menu", True, WHITE)
    screen.blit(resettext, [175, 280])

def spawnpickups(map):
    for item in pickups_sprite_list:
        item.kill()
    if map == "1":
        gunnum = random.randrange(0, 3)
        spawn1 = Pickups(490, 625, gunnum)
        all_sprites_list.add(spawn1)
        pickups_sprite_list.add(spawn1)
        gunnum = random.randrange(0, 3)
        spawn2 = Pickups(490, 425, gunnum)
        all_sprites_list.add(spawn2)
        pickups_sprite_list.add(spawn2)
        gunnum = random.randrange(0, 3)
        spawn3 = Pickups(190, 325, gunnum)
        all_sprites_list.add(spawn3)
        pickups_sprite_list.add(spawn3)
        gunnum = random.randrange(0, 3)
        spawn4 = Pickups(790, 325, gunnum)
        all_sprites_list.add(spawn4)
        pickups_sprite_list.add(spawn4)

    if map == "2":
        gunnum = random.randrange(0, 3)
        spawn1 = Pickups(150, 225, gunnum)
        all_sprites_list.add(spawn1)
        pickups_sprite_list.add(spawn1)
        gunnum = random.randrange(0, 3)
        spawn2 = Pickups(850, 225, gunnum)
        all_sprites_list.add(spawn2)
        pickups_sprite_list.add(spawn2)
        gunnum = random.randrange(0, 3)
        spawn3 = Pickups(665, 325, gunnum)
        all_sprites_list.add(spawn3)
        pickups_sprite_list.add(spawn3)
        gunnum = random.randrange(0, 3)
        spawn4 = Pickups(160, 425, gunnum)
        all_sprites_list.add(spawn4)
        pickups_sprite_list.add(spawn4)
        gunnum = random.randrange(0, 3)
        spawn5 = Pickups(490, 625, gunnum)
        all_sprites_list.add(spawn5)
        pickups_sprite_list.add(spawn5)

# Instantiate Objects
titlepic = Titleimage()
map1floor = Hardfloor(1000, 100, 0, 650)
# Set up sprite lists
all_sprites_list = pygame.sprite.Group()
floors = pygame.sprite.Group()
movingfloors = pygame.sprite.Group()
bullet_sprite_list = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
pickups_sprite_list = pygame.sprite.Group()
enemies = pygame.sprite.Group()
ladders = pygame.sprite.Group()
# Adding Objects to sprite lists
# all_sprites_list.add(player1)
# variables
timer = 0
pickup_timer = 0
done = False
Menu = True
Setup = True
Multiplayer = False
Gameover = False
Singleplayer = False
gunnum = 0
player1downcount = 0
player1downtimer = 0
Levelselect = False
Enemy_spawn_timer = 0
Leveltimer = 0
score = 0
Mapselect = True
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if Menu:
        if Setup:
            Setup = False
            for sprite in all_sprites_list:
                sprite.kill()
            titlepic = Titleimage()
            all_sprites_list.add(titlepic)
            Multiplayertext = font.render("Press 1 to play Multiplayer!", True, WHITE)
            Singleplayertext = font.render("Press 2 to play Singleplayer!", True, WHITE)

        screen.fill(BLACK)
        screen.blit(Multiplayertext, [275, 250])
        screen.blit(Singleplayertext, [275, 350])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                Menu = False
                Multiplayer = True
                Setup = True
                Map1 = True
                Gameover = False
                # Set Map1 to true so that i can develop the first map, there will be the option to choose a map later on
            if event.key == pygame.K_2:
                Menu = False
                Singleplayer = True
                Setup = False
                Levelselect = True
                Gameover = False
    if Singleplayer == True:
        if not Gameover:
            if Levelselect == True:
                Level1text = font.render("Press A for Level 1", True, WHITE)
                Level2text = font.render("Press B for Level 2", True, WHITE)
                Level3text = font.render("Press C for Level 3", True, WHITE)
                Level1hs = statfont.render("L1 Highscore: ", True, WHITE)
                Level1hsnum = statfont.render(L1topscore, True, WHITE)
                Level2hs = statfont.render("L2 Highscore: ", True, WHITE)
                Level2hsnum = statfont.render(L2topscore, True, WHITE)
                Level3hs = statfont.render("L3 Highscore: ", True, WHITE)
                Level3hsnum = statfont.render(L3topscore, True, WHITE)
                screen.fill(BLACK)
                screen.blit(Level1text, [350, 250])
                screen.blit(Level1hs, [425, 290])
                screen.blit(Level1hsnum, [550, 290])
                screen.blit(Level2text, [350, 350])
                screen.blit(Level2hs, [425, 390])
                screen.blit(Level2hsnum, [550, 390])
                screen.blit(Level3text, [350, 450])
                screen.blit(Level3hs, [425, 490])
                screen.blit(Level3hsnum, [550, 490])
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        Setup = True
                        Levelselect = False
                        Level = "1"
                    if event.key == pygame.K_b:
                        Setup = True
                        Level = "2"
                        Levelselect = False
                    if event.key == pygame.K_c:
                        Setup = True
                        Level = "3"
                        Levelselect = False
            elif Levelselect == False:
                if Setup == True:
                    Setup = False
                    all_sprites_list.empty()
                    floors.empty()
                    player1 = Player(470, 580)
                    all_sprites_list.add(player1)

                    # This won't work when I try to use the subroutine, only when the level1 floor is declared here
                    Levelfloor = Hardfloor(1000, 100, 0, 650)
                    all_sprites_list.add(Levelfloor)
                    floors.add(Levelfloor)
                    obstacles.add(Levelfloor)
                    if Level == "1":
                        for x in range(25):
                            map1softfloor1 = Softfloor(300, 0 + (1200 * x), 550)
                            all_sprites_list.add(map1softfloor1)
                            floors.add(map1softfloor1)
                            obstacles.add(map1softfloor1)
                            map1softfloor2 = Softfloor(300, 600 + (1200 * x), 550)
                            all_sprites_list.add(map1softfloor2)
                            floors.add(map1softfloor2)
                            obstacles.add(map1softfloor2)
                            map1softfloor3 = Softfloor(300, 300 + (1200 * x), 450)
                            all_sprites_list.add(map1softfloor3)
                            floors.add(map1softfloor3)
                            obstacles.add(map1softfloor3)
                            map1softfloor4 = Softfloor(300, 0 + (1200 * x), 350)
                            all_sprites_list.add(map1softfloor4)
                            floors.add(map1softfloor4)
                            obstacles.add(map1softfloor4)
                            map1softfloor5 = Softfloor(300, 600 + (1200 * x), 350)
                            all_sprites_list.add(map1softfloor5)
                            floors.add(map1softfloor5)
                            obstacles.add(map1softfloor5)
                            map1softfloor6 = Softfloor(300, 900 + (1200 * x), 450)
                            all_sprites_list.add(map1softfloor6)
                            floors.add(map1softfloor6)
                            obstacles.add(map1softfloor6)

                    if Level == "2":
                        for x in range(25):
                            map2softfloor1 = Softfloor(300, 0 + (1200 * x), 550)
                            all_sprites_list.add(map2softfloor1)
                            floors.add(map2softfloor1)
                            obstacles.add(map2softfloor1)
                            map2softfloor2 = Softfloor(300, 300 + (1200 * x), 450)
                            all_sprites_list.add(map2softfloor2)
                            floors.add(map2softfloor2)
                            obstacles.add(map2softfloor2)
                            map2softfloor3 = Softfloor(300, 600 + (1200 * x), 350)
                            all_sprites_list.add(map2softfloor3)
                            floors.add(map2softfloor3)
                            obstacles.add(map2softfloor3)
                            map2softfloor4 = Softfloor(300, 900 + (1200 * x), 450)
                            all_sprites_list.add(map2softfloor4)
                            floors.add(map2softfloor4)
                            obstacles.add(map2softfloor4)

                    if Level == "3":
                        for x in range(25):
                            for y in range(3):
                                map3softfloor1 = Softfloor(100, 0 + (1200 * x), 350 + (y * 100))
                                all_sprites_list.add(map3softfloor1)
                                floors.add(map3softfloor1)
                                map3softfloor2 = Softfloor(100, 200 + (1200 * x), 350 + (y * 100))
                                all_sprites_list.add(map3softfloor2)
                                floors.add(map3softfloor2)
                                map3softfloor3 = Softfloor(100, 400 + (1200 * x), 350 + (y * 100))
                                all_sprites_list.add(map3softfloor3)
                                floors.add(map3softfloor3)
                                map3softfloor4 = Softfloor(100, 600 + (1200 * x), 350 + (y * 100))
                                all_sprites_list.add(map3softfloor4)
                                floors.add(map3softfloor4)
                                map3softfloor5 = Softfloor(100, 800 + (1200 * x), 350 + (y * 100))
                                all_sprites_list.add(map3softfloor5)
                                floors.add(map3softfloor5)
                                map3softfloor6 = Softfloor(100, 1000 + (1200 * x), 350 + (y * 100))
                                all_sprites_list.add(map3softfloor6)
                                floors.add(map3softfloor6)

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
                        player1.speedy = -5.4
                        player1.supported = False
                        player1.state = "jump"
                    elif event.key == pygame.K_DOWN and player1.supported == True and player1.shooting == False:
                        player1.state = "crouched"
                        player1.crouched = True
                        player1.uncrouching = True
                        if player1.crouching == True:
                            player1.rect.y += 18
                            player1.crouching = False
                        # This code is for double tapping the down key to drop from a floor
                        # player1downcount += 1
                        # if player1downcount == 2 and player1downtimer <= 20:
                        #    player1downcount = 0
                        #    player1.supported = False
                        #    player1.dropping = True
                        # splayer1downtimer = 0

                    elif event.key == pygame.K_n and player1.supported == True:
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
                            # To readjust the sprite when the player stops shooting.
                            player1.crouching = True
                    elif event.key == pygame.K_k:
                        pickup_player_contact = pygame.sprite.spritecollide(player1, pickups_sprite_list, False)
                        for gun in pickup_player_contact:
                            player1.gun = gun.type
                            if gun.type == "magnum":
                                player1.ammo = 5
                            elif gun.type == "pistol":
                                player1.ammo = 12
                            gun.kill()

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
                        if player1.aiming == True and player1.ammo > 0:
                            player1.aiming = False
                            x = random.randrange(0, 2)
                            spread = random.randrange(2, 30)
                            # Generate the amount of spread
                            if x == 1:
                                Ydirection = True
                            else:
                                Ydirection = False
                            # Generate which way the spread goes
                            if player1.direction == "right":
                                # Coords adjusted a bit so that the bullet dies not collide with the player and dissapear straight away once created
                                bullet = Bullet((player1.rect.x + 55), (player1.rect.y + 9), spread, Ydirection)
                                bullet.direction = "right"
                                all_sprites_list.add(bullet)
                                bullet_sprite_list.add(bullet)
                            elif player1.direction == "left":
                                bullet = Bullet(player1.rect.x - 12, player1.rect.y + 9, spread, Ydirection)
                                bullet.direction = "left"
                                all_sprites_list.add(bullet)
                                bullet_sprite_list.add(bullet)
                            bullet.gun = player1.gun
                        player1.shooting = False
                        if player1.wascrouched == True:
                            player1.rect.y += 18
                            player1.wascrouched = False
                            player1.crouched = True
                            player1.crouching = False
                            player1.uncrouching = True

                for bullet in bullet_sprite_list:
                    bullet.update()
                for sprite in all_sprites_list:
                    sprite.rect.x -= 2

                Levelfloor.rect.x += 2

                if Enemy_spawn_timer == 180:
                    Enemy_spawn_timer = 0
                    ypos = random.randrange(110, 600)
                    enemy = Enemy(ypos)
                    enemies.add(enemy)
                    all_sprites_list.add(enemy)

                for enemy in enemies:
                    enemy.update()
                    if enemy.rect.x < -42:
                        enemy.kill()
                        player1.lives -= 1

                Enemy_hit_list = pygame.sprite.groupcollide(enemies, bullet_sprite_list, True, True)

                for sprite in floors:
                    if sprite.rect.x < -300:
                        sprite.kill()
                screen.blit(background_image1, (0, 0))
                drawstatsSP()
                player1.update(timer)

                Enemy_spawn_timer += 1

                if player1.lives == 0:
                    Gameover = True
                    if Leveltimer > 2000:
                        Result = True
                    elif Leveltimer < 2000:
                        Result = False
                    for sprite in all_sprites_list:
                        sprite.kill()
                Leveltimer += 1

                score += 1
        if Gameover:

            if Level == "1":
                if score > int(L1topscore):
                    L1 = open("L1highscore.txt", "w")
                    L1.write(str(score))
                    L1.close()
                    L1topscore = str(score)
                    score = 0
            if Level == "2":
                if score > int(L2topscore):
                    L2 = open("L2highscore.txt", "w")
                    L2.write(str(score))
                    L2.close()
                    L2topscore = str(score)
                    score = 0
            if Level == "3":
                if score > int(L3topscore):
                    L3 = open("L3highscore.txt", "w")
                    L3.write(str(score))
                    L3.close()
                    L3topscore = str(score)
                    score = 0


            screen.fill(BLACK)
            drawresult(Result)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Singleplayer = False
                    Menu = True
                    Setup = True

    if Multiplayer:
        if Mapselect:
            Map1text = font.render("Press A for Map 1", True, WHITE)
            Map2text = font.render("Press B for Map 2", True, WHITE)
            Map3text = font.render("Press C for Map 3", True, WHITE)
            screen.fill(BLACK)
            screen.blit(Map1text, [350, 250])
            screen.blit(Map2text, [350, 350])
            screen.blit(Map3text, [350, 450])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    Setup = True
                    Mapselect = False
                    Map = "1"
                if event.key == pygame.K_b:
                    Setup = True
                    Map = "2"
                    Mapselect = False
                if event.key == pygame.K_c:
                    Setup = True
                    Map = "3"
                    Mapselect = False

        elif not Mapselect:
            if not Gameover:
                if Setup:
                    Setup = False
                    all_sprites_list.empty()
                    floors.empty()

                    mapcreate(Map)

                    player1 = Player(900, 580)
                    player2 = Player(100, 0)
                    all_sprites_list.add(player1)
                    all_sprites_list.add(player2)

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
                        player1_ladder_list = pygame.sprite.spritecollide(player1, ladders, False)
                        if not player1_ladder_list:
                            player1.speedy = -5.4
                            player1.supported = False
                            player1.state = "jump"
                        elif player1_ladder_list:
                            player1.state = "climb"
                            player1.rect.y -= 3
                            player1.climbing = True

                    elif event.key == pygame.K_DOWN and player1.supported == True and player1.shooting == False:
                        player1.state = "crouched"
                        player1.crouched = True
                        player1.uncrouching = True
                        if player1.crouching == True:
                            player1.rect.y += 18
                            player1.crouching = False
                        # This code is for double tapping the down key to drop from a floor
                        # player1downcount += 1
                        # if player1downcount == 2 and player1downtimer <= 20:
                        #    player1downcount = 0
                        #    player1.supported = False
                        #    player1.dropping = True
                        # aplayer1downtimer = 0

                    elif event.key == pygame.K_n and player1.supported == True:
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
                            # To readjust the sprite when the player stops shooting.
                            player1.crouching = True
                    elif event.key == pygame.K_k:
                        pickup_player_contact = pygame.sprite.spritecollide(player1, pickups_sprite_list, False)
                        for gun in pickup_player_contact:
                            player1.gun = gun.type
                            if gun.type == "magnum":
                                player1.ammo = 5
                            elif gun.type == "pistol":
                                player1.ammo = 12
                            gun.kill()

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
                    elif event.key == pygame.K_UP:
                        player1_ladder_list = pygame.sprite.spritecollide(player1, ladders, False)
                        if player1.climbing == True and not player1_ladder_list:
                            player1.state = "walk"
                            player1.supported = False
                            player1.climbing = False

                    elif event.key == pygame.K_n:
                        if player1.aiming == True and player1.ammo > 0:
                            player1.ammo -= 1
                            player1.aiming = False
                            x = random.randrange(0, 2)
                            spread = random.randrange(2, 30)
                            # Generate the amount of spread
                            if x == 1:
                                Ydirection = True
                            else:
                                Ydirection = False
                            # Generate which way the spread goes
                            if player1.direction == "right":
                                # Coords adjusted a bit so that the bullet dies not collide with the player and dissapear straight away once created
                                bullet = Bullet((player1.rect.x + 55), (player1.rect.y + 9), spread, Ydirection)
                                bullet.direction = "right"
                                all_sprites_list.add(bullet)
                                bullet_sprite_list.add(bullet)
                            elif player1.direction == "left":
                                bullet = Bullet(player1.rect.x - 12, player1.rect.y + 9, spread, Ydirection)
                                bullet.direction = "left"
                                all_sprites_list.add(bullet)
                                bullet_sprite_list.add(bullet)
                            bullet.gun = player1.gun
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
                        player2_ladder_list = pygame.sprite.spritecollide(player2, ladders, False)
                        if not player2_ladder_list:
                            player2.speedy = -5.4
                            player2.supported = False
                            player2.state = "jump"
                        elif player2_ladder_list:
                            player2.state = "climb"
                            player2.rect.y -= 3
                            player2.climbing = True
                    elif event.key == pygame.K_s and player2.supported == True and player2.shooting == False:
                        player2.state = "crouched"
                        player2.crouched = True
                        player2.uncrouching = True
                        if player2.crouching == True:
                            player2.rect.y += 18
                            player2.crouching = False
                    elif event.key == pygame.K_2 and player2.supported == True:
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
                            # To readjust the sprite when the player stops shooting.21
                            player2.crouching = True
                    elif event.key == pygame.K_q:
                        pickup_player_contact = pygame.sprite.spritecollide(player2, pickups_sprite_list, False)
                        for gun in pickup_player_contact:
                            player2.gun = gun.type
                            if gun.type == "magnum":
                                player2.ammo = 5
                            elif gun.type == "pistol":
                                player2.ammo = 12
                            gun.kill()

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
                    elif event.key == pygame.K_w:
                        player2_ladder_list = pygame.sprite.spritecollide(player2, ladders, False)
                        if player2.climbing == True and not player2_ladder_list:
                            player2.state = "walk"
                            player2.supported = False
                            player2.climbing = False

                    elif event.key == pygame.K_2:
                        if player2.aiming == True and player2.ammo > 0:
                            player2.ammo -= 1
                            player2.aiming = False
                            x = random.randrange(0, 2)
                            spread = random.randrange(2, 15)
                            # Generate the amount of spread
                            if x == 1:
                                Ydirection = True
                            else:
                                Ydirection = False
                            # Generate which way the spread goes
                            if player2.direction == "right":
                                # Coords adjusted a bit so that the bullet does not collide with the player straight away when created
                                bullet = Bullet((player2.rect.x + 55), (player2.rect.y + 9), spread, Ydirection)
                                bullet.direction = "right"
                                all_sprites_list.add(bullet)
                                bullet_sprite_list.add(bullet)
                            elif player2.direction == "left":
                                bullet = Bullet(player2.rect.x - 12, player2.rect.y + 9, spread, Ydirection)
                                bullet.direction = "left"
                                all_sprites_list.add(bullet)
                                bullet_sprite_list.add(bullet)
                            bullet.gun = player2.gun
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

                if pickup_timer == 599:
                    spawnpickups(Map)

                if Map == "1":
                    screen.blit(background_image1, (0, 0))
                if Map == "2":
                    screen.blit(background_image2, (0, 0))
                if Map == "3":
                    screen.blit(background_image3, (0, 0))
                    for item in movingfloors:
                        item.update()

                        
                # Timers
                timer = timer + 1
                if timer % 60 == 0:
                    timer = 0
                player1downtimer += 1
                if player1downtimer == 15:
                    player1.dropping = False
                    player1downtimer = 0
                pickup_timer += 1
                if pickup_timer % 600 == 0:
                    pickup_timer = 0

                # To check if either character is dead
                if player1.health <= 0:
                    winner = "Player 2"
                    for sprite in all_sprites_list:
                        sprite.kill()
                    Gameover = True
                if player2.health <= 0:
                    winner = "Player 1"
                    for sprite in all_sprites_list:
                        sprite.kill()
                    Gameover = True
            elif Gameover:
                screen.fill(BLACK)
                drawwinner(winner)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Multiplayer = False
                        Menu = True
                        Setup = True
            drawstats()

    # This is ran every frame regardless of the gamemode
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()


def drawwinner(winner):
    if Multiplayer and Gameover:
        if winner == "Player 1":
            Winnertext = font.render("Player 1 Wins!", True, WHITE)
            screen.blit(Winnertext, [370, 150])
        elif winner == "Player 2":
            Winnertext = font.render("Plare 2 Wins!", True, WHITE)
            screen.blit(Winnertext, [370, 150])
        nexttext = font.render("Press Space to return to menu", True, WHITE)
        screen.blit(nexttext, [250, 500])