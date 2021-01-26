#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: January 2020
# This program is the "The Snake Game" program on the PyBadge

import ugame
import stage
import random

import constants
HEAD = 0
def game_scene():
    # this function is the main game game_scene
   snakes = []
   def show_snake(x , y):
        # this function takes an alien from off screen and moves it on screen
       for snake_number in range(len(snakes)):
           if snakes[snake_number].x < 0:
               snakes[snake_number].move(x,y)
               break
   def show_apple():
       apples[0].move(20, 30)
   # image banks for CircuitPython
   image_bank_bankground = stage.Bank.from_bmp16("ball.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("PyBadge_bank_color_template.bmp")
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, 10,8)
   
   # a sprite that will be updated every frame
   for snake_number in range(10):
       a_single_snake = stage.Sprite(image_bank_sprites, 11,
                                     constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
       snakes.append(a_single_snake)
   #place 1 alien on the screen
   x = 75
   y = 66
   show_snake(x, y)
   show_snake(x-16,y)
#   show_snake(x-32,y)
#   show_snake(x-48,y)
 #  snake = stage.Sprite(image_bank_sprites, 11, 75, 66)
   apples = []
   for apple_number in range(2):
       a_single_apple = stage.Sprite(image_bank_sprites, 8 , constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
       apples.append(a_single_apple)
   apples[0].move(20, 30)
   # create a stage for the background to show up on
   #   and set the frame rate for 60fps
   game = stage.Stage(ugame.display, 5)
   # set layers of all sprites, items show up in order
   game.layers = snakes + apples + [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
   
   right_button = "button_up"
   left_button = "button_up"
   up_button = "button_up"
   down_button = "button_up"
   wormCoords = [{'x': snakes[0].x , 'y': snakes[0].y},
                  {'x': snakes[1].x , 'y': snakes[1].y}]
   newHead = {'x':snakes[0].x, 'y' :snakes[0].y}
       
   
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
           newHead = {'x':snakes[0].x +16, 'y' :snakes[0].y}
           wormCoords.insert(0,newHead)
           del wormCoords[-1]
           for snake_number in range (len(snakes)):
               if snakes[snake_number].x > 0:
                   snakes[snake_number].move(constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
                   
       if left_button == "button_pressed" :
           newHead = {'x':snakes[0].x - 16, 'y' :snakes[0].y}
           wormCoords.insert(0,newHead)
           del wormCoords[-1]
           for snake_number in range (len(snakes)):
               if snakes[snake_number].x > 0:
                   snakes[snake_number].move(constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
        
       if up_button == "button_pressed" :
           newHead = {'x':snakes[0].x, 'y' :snakes[0].y - 16}
           wormCoords.insert(0,newHead)
           del wormCoords[-1]
           for snake_number in range (len(snakes)):
               if snakes[snake_number].x > 0:
                   snakes[snake_number].move(constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
                  
       if down_button == "button_pressed" :
           newHead = {'x':snakes[0].x, 'y' :snakes[0].y + 16}
           wormCoords.insert(0,newHead)
           del wormCoords[-1]
           for snake_number in range (len(snakes)):
              if snakes[snake_number].x > 0:
                       snakes[snake_number].move(constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
       

                   
 
                    
       for coords in wormCoords:
           x= coords['x']
           y= coords['y']
           show_snake(x,y)
           
           
       for snake_number in range(len(snakes)):
           if snakes[snake_number].x > 0:
               for apple_number in range(len(apples)):
                   if apples[apple_number].x > 0:
                       if stage.collide(snakes[snake_number].x , 
                                        snakes[snake_number].y,
                                        snakes[snake_number].x + 15,
                                        snakes[snake_number].y + 15,
                                        apples[apple_number].x ,
                                        apples[apple_number].y,
                                        apples[apple_number].x + 15,
                                        apples[apple_number].y + 15):
                           pass
                        # you hit an alien

                           apples[apple_number].move(constants.OFF_SCREEN_X,
                                                  constants.OFF_SCREEN_Y)
 #                          show_apple()                       
#           else:        
#               del wormCoords[-1]    
       # redraw Sprite
       game.render_sprites(snakes + apples)
       game.tick() # wait until refresh rate finishes

def game_over_scene():
    # this function is the game over scene
           
   # turn off sound from last scene
   sound = ugame.audio
   sound.stop()
           
   # image banks for Circuitpython
   image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
           
   # sets the background to image 0 in the image bank
   background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                                    constants.SCREEN_GRID_Y)
            
   # add text objects
 
   # create a stage for the background to show up on
   #     ad set the frame rate to 60fps
   game = stage.Stage(ugame.display, constants.FPS)
   # set layers of all sprites, items show up in order
   game.layers = [background]
   # render all sprites
   #   most likely you will only render the background once per game scene
   game.render_block()
           
   # repeat forever, game loop
   while True:
       # get user input
       keys = ugame.buttons.get_pressed()
                
       # Start button selecte
       if keys & ugame.K_SELECT !=0:
           supervisor.reload()
                
           # update game logic
       game.tick() #  wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()
