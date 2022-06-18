#  A simple platformer game built by Gabe Holmes
#  This is the main event loop, run this file to run the game
#
from controller import *
from level import Level
from settings import *

# Level strings
level0 = basic_level
level1 = level_1
level2 = level_2



level_0_controller = Controller([level0])
#level_0_controller.run()

level_1_controller = Controller([level1])

level_0_1_controller = Controller([level0, level1])
# level_0_1_controller.run()

level_2_controller = Controller([level2])
# level_2_controller.run()

menu_controller = MenuController()
menu_controller.run()