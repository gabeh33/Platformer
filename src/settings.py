basic_level = [
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '            XXXXXXX     ',
    '  XXX                  X',
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

tile_size = 64
# screen_width = len(basic_level[0]) * tile_size
screen_width = 1200
screen_height = min(tile_size * len(basic_level), 800)
player_speed = 5
jump_cooldown = 0.35

gui_height = 160
