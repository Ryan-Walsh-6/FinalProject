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
   image_bank_bankground = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")
   
   # buttons that you want to keep state information on
   a_button = constants.button_state["button_up"]
   b_button = constants.button_state["button_up"]
   start_button = constants.button_state["button_up"]
   select_button = constants.button_state["button_up"]
   
   # get sound ready
   pew_sound = open("pew.wav", 'rb')
   sound = ugame.audio
   sound.stop()
   sound.mute(False)
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, 10,8)
   
   # a sprite that will be updated every frame
   snake = stage.Sprite(image_bank_sprites, 10, 75, constants.SCREEN_Y - 
   (2 * constants.SNAKE_SIZE))
   
   apple = stage.Sprite(image_bank_sprites, 8, int(constants.SCREEN_X / 2 - 
   constants.SNAKE_SIZE / 2),16)

   # create a stage for the background to show up on
   #   and set the frame rate for 60fps
   game = stage.Stage(ugame.display, 60)
   # set layers of all sprites, items show up in order
   game.layers = [snake] + [apple] + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()

    # repeat forever, game loop
   while True:
       # get user input
       keys = ugame.buttons.get_pressed()
       
       if keys & ugame.K_O != 0:
           if a_button == constants.button_state["button_up"]:
               a_button = constants.button_state["button_just_pressed"]
           elif a_button == constants.button_state["button_just_pressed"]:
                 a_button = constants.button_state["button_still_pressed"]
       else: 
           if a_button == constants.button_state["button_still_pressed"]:
               a_button = constants.button_state["button_released"]
           else:
                a_button = constants.button_state["button_up"]
        # B button        
       if keys & ugame.K_X != 0:
           pass
       if keys & ugame.K_START:
           print("Start")
       if keys & ugame.K_SELECT:
           print("Select")

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
       # play sound if A was just button_just_pressed
       if a_button == constants.button_state["button_just_pressed"]:
           sound.play(pew_sound)

       # redraw sprites
       game.render_sprites([snake] + [apple])
       game.tick() # wait until refresh rate finishes

if __name__ == "__main__":
    game_scene()
