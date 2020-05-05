"""Game tutorial"""

import pygame

def collision_check(player_x, player_y, object_x, object_y):
    '''Checks to see if player has collided with the treasure or enemies'''

    global player_width, player_height, treasure_width, treasure_height

    collision_state = False

    if player_x + player_width >= object_x and player_x <= object_x + treasure_width:
        if player_y + player_height >= object_y and player_y <= object_y + treasure_height:
            collision_state = True

    return collision_state

pygame.init()

#screen
screen_width = 900
screen_height = 700
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

finished = False

#player
player_width = 40
player_height = 45
player_size = (player_width, player_height)

start_x = int(screen_width / 2) - int(player_width / 2)
start_y = screen_height - 50
player_x = start_x
player_y = start_y
player_loc = (player_x, player_y)

player_image = pygame.image.load("images/Player.png")
player_image = pygame.transform.scale(player_image, player_size)
player_image = player_image.convert()

#background
background_image = pygame.image.load("images/background.png")
background_image = pygame.transform.scale(background_image, screen_size)
screen.blit(background_image, (0, 0))

#treasure
treasure_width = 40
treasure_height = 45
treasure_size = (treasure_width, treasure_height)

object_x = int(screen_width / 2) - int(treasure_width / 2)
object_y = 50
treasure_loc = (object_x, object_y)

treasure_image = pygame.image.load("images/treasure.png")
treasure_image = pygame.transform.scale(treasure_image, treasure_size)

#enemy
enemy_width = 40
enemy_height = 45
enemy_size = (enemy_width, enemy_height)

enemy_x = 100
enemy_y = 300
enemy_loc = (enemy_x, enemy_y)
move_right = True

enemy_image = pygame.image.load("images/enemy.png")
enemy_image = pygame.transform.scale(enemy_image, enemy_size)
enemy_image = enemy_image.convert()

font = pygame.font.SysFont("comicsans", 60)

level = 1

frame = pygame.time.Clock()

while finished is not True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pressed_keys = pygame.key.get_pressed()

    #player movement
    if pressed_keys[pygame.K_UP]:
        player_y -= 5

    if pressed_keys[pygame.K_DOWN]:
        player_y += 5

    if pressed_keys[pygame.K_LEFT]:
        player_x -= 5

    if pressed_keys[pygame.K_RIGHT]:
        player_x += 5

    player_loc = (player_x, player_y)

    #enemy movement
    if enemy_x >= screen_width - enemy_width * 2:
        move_right = False
    elif enemy_x <= enemy_width * 2:
        move_right = True

    if move_right is True:
        enemy_x += 5 * level
    else:
        enemy_x -= 5 * level

    enemy_loc = (enemy_x, enemy_y)

    #draw objects on screen
    screen.blit(background_image, (0, 0))
    screen.blit(treasure_image, treasure_loc)
    screen.blit(player_image, player_loc)
    screen.blit(enemy_image, enemy_loc)

    #check is player collides with treasure
    if collision_check(player_x, player_y, object_x, object_y):
        # update level
        level += 1

        # update win message
        text_win = font.render("You've reached level " + str(level) + "!", True, (0, 0, 255))
        text_loc = \
            (int(screen_width / 2 - text_win.get_width() / 2), \
            int(screen_height / 2 - text_win.get_height() / 2))

        screen.blit(text_win, text_loc)
        pygame.display.flip()
        frame.tick(1)

        # reset player position
        player_x = start_x
        player_y = start_y

    #check if player collides with an enemy
    if collision_check(player_x, player_y, enemy_x, enemy_y):
        #display loss message
        text_loss = font.render("The enemy caught you!", True, (100, 0, 100))
        text_loc = \
            (int(screen_width / 2 - text_loss.get_width() / 2), \
            int(screen_height / 2 - text_loss.get_height() / 2))

        screen.blit(text_loss, text_loc)
        pygame.display.flip()
        frame.tick(1)

        # reset player position
        player_x = start_x
        player_y = start_y

    pygame.display.flip()
    frame.tick(30)
