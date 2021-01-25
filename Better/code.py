#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: January 2020
# This program is the "The Snake Game" program on the PyBadge

import ugame
import stage
import random

import constants
def game_scene():
    # this function is the main game game_scene
   snakes = []
   def show_snake(x , y):
        # this function takes an alien from off screen and moves it on screen
       for snake_number in range(len(snakes)):
           if snakes[snake_number].x < 0:
               snakes[snake_number].move(x,y)
               break
   # image banks for CircuitPython
   image_bank_bankground = stage.Bank.from_bmp16("ball.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, 10,8)
   
   # a sprite that will be updated every frame
   for snake_number in range(5):
       a_single_snake = stage.Sprite(image_bank_sprites, 11,
                                     constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
       snakes.append(a_single_snake)
   #place 1 alien on the screen
   x = 75
   y = 66
   show_snake(x, y)
   show_snake(x-16,y)
   show_snake(x-32,y)
 #  snake = stage.Sprite(image_bank_sprites, 11, 75, 66)
   apple = stage.Sprite(image_bank_sprites, 8, 20, 42)
   # create a stage for the background to show up on
   #   and set the frame rate for 60fps
   game = stage.Stage(ugame.display, 60)
   # set layers of all sprites, items show up in order
   game.layers = snakes + [apple] + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
   
   right_button = "button_up"
   left_button = "button_up"
   up_button = "button_up"
   down_button = "button_up"
  
  # repeat forever, game loop
   while True:
       # get user input
       keys = ugame.buttons.get_pressed()
      
       if keys & ugame.K_RIGHT !=0:
           right_button = "button_pressed"
           left_button = "button_up"
           up_button = "button_up"
           down_button = "button_up"
       elif keys & ugame.K_LEFT !=0:
           right_button = "button_up"
           left_button = "button_pressed"
           up_button = "button_up"
           down_button = "button_up"
       elif keys & ugame.K_UP !=0:
           right_button = "button_up"
           left_button = "button_up"
           up_button = "button_pressed"
           down_button = "button_up"
       elif keys & ugame.K_DOWN !=0:
           right_button = "button_up"
           left_button = "button_up"
           up_button = "button_up"
           down_button = "button_pressed"
           
       
       if keys & ugame.K_X:
           pass
       if keys & ugame.K_O:
           pass
       if keys & ugame.K_START:
           pass
       if keys & ugame.K_SELECT:
           pass
       if right_button == "button_pressed" :
           x = 0
           i = 0 
           j = 0
           for snake_number in range(len(snakes)):
               if snakes[snake_number].x > 0:
                  i += 1
           for snake_number in range(len(snakes)):
               if snakes[snake_number].x > 0:              
                  x = snakes[snake_number].x + 1
                  y = snakes[snake_number].y
                  while j < i:
                        snakes[j].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
                        j = j + 1
                        show_snake(x,y)
                        x=x-16
                  break
       if left_button == "button_pressed" :
           x = 0
           i = 0 
           j = 0
           for snake_number in range(len(snakes)):
               if snakes[snake_number].x > 0:
                  i += 1
           for snake_number in range(len(snakes)):
               if snakes[snake_number].x > 0:              
                  x = snakes[i-1].x - 1
                  y = snakes[i-1].y
                  while i > j:
                        snakes[i-1].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
                        i = i - 1
                        show_snake(x,y)
                        x=x+16
                  break
       if up_button == "button_pressed" :
           x = 0
           i = 0 
           j = 0
           for snake_number in range(len(snakes)):
               if snakes[snake_number].x > 0:
                  i += 1
           count = i * 16          
           for snake_number in range(len(snakes)):
               if snakes[snake_number].x > 0:              
                  x = snakes[snake_number].x
                  y = snakes[snake_number].y - 1
                  while j < i:
                        snakes[j].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
                        j = j + 1
                        show_snake(x,y)
                        y=y-16
                  break
       if down_button == "button_pressed" :
           x = 0
           i = 0 
           j = 0
           for snake_number in range(len(snakes)):
               if snakes[snake_number].x > 0:
                  i += 1
           count = i * 16          
           for snake_number in range(len(snakes)):
               if snakes[snake_number].x > 0:              
                  x = snakes[snake_number].x
                  y = snakes[snake_number].y + 1
                  while j < i:
                        snakes[j].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
                        j = j + 1
                        show_snake(x,y)
                        y=y+16
                  break
       # update game logic
       
       # redraw Sprite
       game.render_sprites(snakes)
       game.tick() # wait until refresh rate finishes

if __name__ == "__main__":
    game_scene()
