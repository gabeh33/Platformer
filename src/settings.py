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
blue_background = '../res/main/Background/Blue.png'
purple_background = '../res/main/Background/Purple.png'
yellow_background = '../res/main/Background/Yellow.png'

gui_image = '../res/main/Background/Gray.png'
character_info = '../res/main/Main Characters/Virtual Guy/'

# Layout information for the gui
left_right_center_offset = 150
distance_from_screen_height = 84
square_size = 64
dimensions = (square_size, square_size)
space_button_width = 128
left_pos = (screen_width / 2 - left_right_center_offset,
            screen_height - distance_from_screen_height)
space_pos = (screen_width / 2, screen_height - distance_from_screen_height)
right_pos = (screen_width / 2 + left_right_center_offset, screen_height - distance_from_screen_height)

# Menu layout dimensions
top_button_to_top_screen = 300
center_x = screen_width / 2
menu_button_width = 400
menu_button_height = 80
button_spacing = 150
