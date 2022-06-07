basic_level = [
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '            XXXXXXX     ',
    '  XXX                  G',
    '           XXXX         ',
    '   P  XXXXXX  X      XX ',
    ' XXXXX         XXXX     ',
    ' XXXXX         XXXX     ',
    ' XXXXX         XXXX     ',
    ' XXXXXXXXXXXXXXXXXXXXXXX',
]

level_1 = [
    '                                   ',
    '                                   ',
    '                                   ',
    '                                   ',
    '                                   ',
    '       XX    G                     ',
    ' P       XX            XX          ',
    'XX                                 ',
    '                                   ',
]

level_2 = [
    '                                       ',
    '                                       ',
    '  P                                    ',
    '  X                                    ',
    '           X                           ',
    '                                       ',
    '                                       ',
    '                                       ',
    '                                       ',
]

tile_size = 64
# screen_width = len(basic_level[0]) * tile_size
screen_width = 1200
screen_height = min(tile_size * len(basic_level), 800)
player_speed = 5
jump_cooldown = 0.75
background_scroll_speed = 0.5
gui_height = 160
background_image = '../res/main/Background/Brown.png'
gui_image = '../res/main/Background/Gray.png'
character_info = '../res/main/Main Characters/Virtual Guy/'
