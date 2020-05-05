"""Game tutorial"""

import pygame

def treasure_collision_check(player_x, player_y, treasure_x, treasure_y):
    '''Checks to see if player has collided with the treasure'''

    global player_width, player_height, treasure_width, treasure_height

    collision_state = False

    # if player_y >= treasure_y and player_y <= treasure_y + treasure_height:
    #     if player_x >= treasure_x and player_x <= treasure_x + treasure_height:
    #         screen.blit(text_win, (300, 300))
    #     elif player_x + player_width >= treasure_x and \
    #         player_x + player_width <= treasure_x + treasure_width:
    #             screen.blit(text_win, (300, 300))
    # elif player_y + player_height >= treasure_y and \
    #     player_y + player_height <= treasure_y + treasure_height:
    #         if player_x >= treasure_x and player_x <= treasure_x + treasure_height:
    #             screen.blit(text_win, (300, 300))
    #         elif player_x + player_width >= treasure_x and \
    #             player_x + player_width <= treasure_x + treasure_width:
    #                 screen.blit(text_win, (300, 300))

    # refactored collision check
    if player_x + player_width >= treasure_x and player_x <= treasure_x + treasure_width:
        if player_y + player_height >= treasure_y and player_y <= treasure_y + treasure_height:
            #screen.blit(text_win, text_loc)
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

treasure_x = int(screen_width / 2) - int(treasure_width / 2)
treasure_y = 50
treasure_loc = (treasure_x, treasure_y)

treasure_image = pygame.image.load("images/treasure.png")
treasure_image = pygame.transform.scale(treasure_image, treasure_size)
#screen.blit(treasure_image, treasure_loc)

#enemy
enemy_width = 40
enemy_height = 45
enemy_size = (enemy_width, enemy_height)

enemy_x = 100
enemy_y = 300
enemy_loc = (enemy_x, enemy_y)

enemy_image = pygame.image.load("images/enemy.png")
enemy_image = pygame.transform.scale(enemy_image, enemy_size)
enemy_image = enemy_image.convert()

font = pygame.font.SysFont("comicsans", 60)
#text_win = font.render("Great Job!", True, (0, 0, 0))
# text_loc = \
#     (int(screen_width / 2 - text_win.get_width() / 2), \
#     int(screen_height / 2 - text_win.get_height() / 2))

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

    screen.blit(background_image, (0, 0))
    screen.blit(treasure_image, treasure_loc)
    screen.blit(player_image, player_loc)
    screen.blit(enemy_image, enemy_loc)

    if treasure_collision_check(player_x, player_y, treasure_x, treasure_y):
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

    pygame.display.flip()
    frame.tick(30)
