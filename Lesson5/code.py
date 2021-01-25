#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: January 2020
# This program is the "The Snake Game" program on the PyBadge

import ugame
import stage

import constants

def game_scene():
    # this function is the main game game_scene

   # image banks for CircuitPython
   image_bank_bankground = stage.Bank.from_bmp16("ball.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, 10,8)
   
   # a sprite that will be updated every frame
   snake = stage.Sprite(image_bank_sprites, 11, 75, constants.SCREEN_Y - (2 * constants.SNAKE_SIZE))

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
       if keys & ugame.K_RIGHT != 0:
           if snake.x < (constants.SCREEN_X - constants.SNAKE_SIZE):
               snake.move((snake.x + constants.SNAKE_MOVEMENT_SPEED), snake.y)
           else:
               snake.move((constants.SCREEN_X - constants.SNAKE_SIZE), snake.y)
       if keys & ugame.K_LEFT != 0:
            if snake.x > 0:
                snake.move((snake.x - constants.SNAKE_MOVEMENT_SPEED), snake.y)
            else:
                snake.move(0, snake.y)
       if keys & ugame.K_UP != 0:
           if snake.y > 0:
               snake.move(snake.x,(snake.y - constants.SNAKE_MOVEMENT_SPEED))
           else:
               snake.move(snake.x, 0)
       if keys & ugame.K_DOWN != 0:
           if snake.y < (constants.SCREEN_Y - constants.SNAKE_SIZE):
               snake.move(snake.x,(snake.y + constants.SNAKE_MOVEMENT_SPEED))
           else:
               snake.move(snake.x, (constants.SCREEN_Y - constants.SNAKE_SIZE))
       # update game logic
       
       # redraw Sprite
       game.render_sprites([snake])
       game.tick() # wait until refresh rate finishes

if __name__ == "__main__":
    game_scene()
