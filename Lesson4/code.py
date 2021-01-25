#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: January 2020
# This program is the "The Snake Game" program on the PyBadge

import ugame
import stage


def game_scene():
    # this function is the main game game_scene

   # image banks for CircuitPython
   image_bank_bankground = stage.Bank.from_bmp16("ball.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, 10,8)
   
   # a sprite that will be updated every frame
   snake = stage.Sprite(image_bank_sprites, 11, 75, 66)

   # create a stage for the background to show up on
   #   and set the frame rate for 60fps
   game = stage.Stage(ugame.display, 60)
   # set layers of all sprites, items show up in order
   game.layers = [snake] + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
   
   while True:
       # get user input
       keys = ugame.buttons.get_pressed()
       
       if keys & ugame.K_X:
           pass
       if keys & ugame.K_O:
           pass
       if keys & ugame.K_START:
           pass
       if keys & ugame.K_SELECT:
           pass
       if keys & ugame.K_RIGHT:
           snake.move(snake.x + 1, snake.y)
       if keys & ugame.K_LEFT:
           snake.move(snake.x - 1, snake.y)
       if keys & ugame.K_UP:
           snake.move(snake.x, snake.y - 1)
       if keys & ugame.K_DOWN:
           snake.move(snake.x, snake.y + 1) 
       # update game logic
       
       # redraw Sprite
       game.render_sprites([snake])
       game.tick() # wait until refresh rate finishes

if __name__ == "__main__":
    game_scene()
