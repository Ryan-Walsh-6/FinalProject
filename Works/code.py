#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: January 2020
# This program is the "The Snake Game" program on the PyBadge

import ugame
import stage
import time
import random
import board
import supervisor

import constants

def splash_scene():
    # this function is the menu scene

    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # used this program to split the image into tile:
    #    https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white


    # create a stage for the background to show up on
    #    and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # this function is the menu scene

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, 
    palette=constants.RED_PALETTE, buffer=None)
    text1.move(20,10)
    text1.text("The Snake Game")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, 
    palette=constants.RED_PALETTE, buffer=None)
    text2.move(40,110)
    text2.text("PRESS START")
    text.append(text2)

    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # create a stage for the background to show up on
    #    and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Start button selected
        if keys & ugame.K_START != 0:
            game_scene()

        # update game logic
        game.tick() # wait until refresh rate finishes

def game_scene():
   def show_apple():
        # this function takes an alien from off screen and moves it on screen
       for apple_number in range(len(apples)):
           if apples[apple_number].x < 0:
               apples[apple_number].move(random.randint(0 + 
               2*constants.SNAKE_SIZE,constants.SCREEN_X - 
               2*constants.SNAKE_SIZE),(random.randint(0 + 
               2*constants.SNAKE_SIZE,constants.SCREEN_Y - 
               2*constants.SNAKE_SIZE)))
               break
    
   apple_crunch = open("apple_crunch.wav", 'rb')
   sound = ugame.audio
   sound.stop()
   sound.mute(False)
   
   score = 0

   score_text = stage.Text(width=29, height=14)
   score_text.clear()
   score_text.cursor(0,0)
   score_text.move(1,1)
   score_text.text("Score: {0}".format(score))
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
   for snake_number in range(50):
       a_single_snake = stage.Sprite(image_bank_sprites, 11,
                                     constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
       snakes.append(a_single_snake)
   #place 1 alien on the screen
   x = 75
   y = 66
   show_snake(x, y)

 #  snake = stage.Sprite(image_bank_sprites, 11, 75, 66)
   apples = []
   for apple_number in range(2):
       a_single_apple = stage.Sprite(image_bank_sprites, 8 , constants.OFF_SCREEN_X,
                                     constants.OFF_SCREEN_Y)
       apples.append(a_single_apple)
   show_apple()
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
   wormCoords = [{'x': snakes[0].x , 'y': snakes[0].y}]
   newHead = {'x':snakes[0].x, 'y' :snakes[0].y}
   HEAD = 0       
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
      
       for snake_number in range(1):
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
                           sound.stop()
                           sound.play(apple_crunch)
                        # you hit an alien
                           score = score + 1
                           score_text.clear()
                           score_text.cursor(0,0)
                           score_text.move(1,1)
                           score_text.text("Score: {0}".format(score))

                           apples[apple_number].move(constants.OFF_SCREEN_X,
                                                  constants.OFF_SCREEN_Y)
                           show_apple()
                           if right_button == "button_pressed" :
                               newHead = {'x':snakes[0].x +16, 'y' :snakes[0].y}
                               wormCoords.insert(0,newHead)
                           elif left_button == "button_pressed" :
                               newHead = {'x':snakes[0].x - 16, 'y' :snakes[0].y}
                               wormCoords.insert(0,newHead)
                           elif up_button == "button_pressed" :
                               newHead = {'x':snakes[0].x, 'y' :snakes[0].y - 16}
                               wormCoords.insert(0,newHead)
                           elif down_button == "button_pressed" :
                               newHead = {'x':snakes[0].x, 'y' :snakes[0].y + 16}
                               wormCoords.insert(0,newHead)
                       else:        
                           if right_button == "button_pressed" :
                               newHead = {'x':snakes[0].x +16, 'y' :snakes[0].y}
                               wormCoords.insert(0,newHead)
                               del wormCoords[-1]
                           elif left_button == "button_pressed" :
                               newHead = {'x':snakes[0].x - 16, 'y' :snakes[0].y}
                               wormCoords.insert(0,newHead)
                               del wormCoords[-1]
                           elif up_button == "button_pressed" :
                               newHead = {'x':snakes[0].x, 'y' :snakes[0].y - 16}
                               wormCoords.insert(0,newHead)
                               del wormCoords[-1]
                           elif down_button == "button_pressed" :
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

 #      for snake_number in range (len(snakes)):
 #          if snakes[snake_number].x > 0:
       if snakes[HEAD].x > (constants.SCREEN_X - constants.SNAKE_SIZE):
           game_over_scene(score)
       if snakes[HEAD].x  < 0:
           game_over_scene(score)
       if snakes[HEAD].y <  0:
           game_over_scene(score)
       if snakes[HEAD].y > (constants.SCREEN_Y):
           game_over_scene(score)
           
       # redraw Sprite
       game.render_sprites(snakes + apples)
       game.tick() # wait until refresh rate finishes

def game_over_scene(final_score):
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
   text = []
   text1 = stage.Text(width=29, height=14, font=None,
   palette=constants.BLUE_PALETTE, buffer=None)
   text1.move(22,20)
   text1.text("Final Score: {:0>2d}".format(final_score))
   text.append(text1)
           
   text2 = stage.Text(width=29, height=14, font=None, 
                      palette=constants.BLUE_PALETTE, buffer=None) 
   text2.move(43,60)
   text2.text("GAME OVER")
   text.append(text2)
           
   text3 = stage.Text(width=29, height=14, font=None, 
                      palette=constants.BLUE_PALETTE, buffer=None)
   text3.move(32,110)
   text3.text("PRESS SELECT")
   text.append(text3)
   # create a stage for the background to show up on
   #     ad set the frame rate to 60fps
   game = stage.Stage(ugame.display, constants.FPS)
   # set layers of all sprites, items show up in order
   game.layers = text + [background]
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
    splash_scene()
