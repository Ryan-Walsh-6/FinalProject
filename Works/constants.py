#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: December 2020
# This program is the constants file for The Snake Game game

# PyBadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SNAKE_SIZE = 16
TOTAL_NUMBER_OF_APPLES = 5
MAX_SCORE = 30
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SNAKE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SNAKE_SIZE
NEOPIXEL_COUNT = 5
FPS = 60
SNAKE_MOVEMENT_SPEED = 1

# using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}

# new pallet for red filled text
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff')
BLUE_PALETTE = (b'\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
