#!/usr/bin/env python3

# Created by: Ryan Walsh
# Created on: January 2021
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage
import time
import random
import board
import neopixel
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
    text1.text("MT Game Studios")
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
    # this function is the main game game_scene
    
#   def show_alien():
        # this function takes an alien from off screen and moves it on screen
#        for alien_number in range(len(aliens)):
#            if aliens[alien_number].x < 0:
#                aliens[alien_number].move(random.randint(0 + 
#                constants.SPRITE_SIZE,constants.SCREEN_X - 
#                constants.SPRITE_SIZE),constants.OFF_TOP_SCREEN)
#                break
    

   neopixels = neopixel.NeoPixel(board.NEOPIXEL, constants.NEOPIXEL_COUNT, 
                                 auto_write=False)

    # for score
#   score = 0

#   score_text = stage.Text(width=29, height=14)
#   score_text.clear()
#   score_text.cursor(0,0)
#   score_text.move(1,1)
#   score_text.text("Score: {0}".format(score))

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
   boom_sound = open("boom.wav", 'rb')
   crash_sound = open("crash.wav", 'rb')
   sound = ugame.audio
   sound.stop()
   sound.mute(False)
   
   # set the background to image 0 in the image Bank
   #   and the size (10x8 tiles of the size 16x16)
   background = stage.Grid(image_bank_bankground, constants.SCREEN_X,
                            constants.SCREEN_Y)
   for x_location in range(constants.SCREEN_GRID_X):
       for y_location in range(constants.SCREEN_GRID_Y):
           tile_picked = 4
           background.tile(x_location, y_location, tile_picked)
   
   # a sprite that will be updated every frame
   snake = stage.Sprite(image_bank_sprites, 10, 75, constants.SCREEN_Y - 
   (constants.SPRITE_SIZE))
   
#   alien = stage.Sprite(image_bank_sprites, 9, int(constants.SCREEN_X / 2 - 
#   constants.SPRITE_SIZE / 2),16)
   
   # create list of aliens
#   aliens = []
#   for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
#       a_single_alien = stage.Sprite(image_bank_sprites, 9,
#                                     constants.OFF_SCREEN_X,
#                                     constants.OFF_SCREEN_Y)
#       aliens.append(a_single_alien)
   #place 1 alien on the screen
#   show_alien()
   
   # create list of lasers for when we shoot
#   lasers = []
#   for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
#       a_single_laser = stage.Sprite(image_bank_sprites, 10,
#                                     constants.OFF_SCREEN_X,
#                                     constants.OFF_SCREEN_Y)
#       lasers.append(a_single_laser)

   # create a stage for the background to show up on
   #   and set the frame rate for 60fps
   game = stage.Stage(ugame.display, constants.FPS)
   # set layers of all sprites, items show up in order
   game.layers = [snake] + [background]
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
           pass
       if keys & ugame.K_SELECT:
           print("Select")

       if keys & ugame.K_RIGHT != 0:
           if snake.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
               snake.move((snake.x + constants.SPRITE_MOVEMENT_SPEED), snake.y)
           else:
               snake.move((constants.SCREEN_X - constants.SPRITE_SIZE), snake.y)

       if keys & ugame.K_LEFT != 0:
            if snake.x > 0:
                snake.move((snake.x - constants.SPRITE_MOVEMENT_SPEED), snake.y)
            else:
                snake.move(0, snake.y)

       if keys & ugame.K_UP:
           pass
       if keys & ugame.K_DOWN:
           pass
       
       #set neopixels to green by default
       neopixels[0] = (0, 10, 0)
       neopixels[1] = (0, 10, 0)
       neopixels[2] = (0, 10, 0)
       neopixels[3] = (0, 10, 0)
       neopixels[4] = (0, 10, 0) 
       # update game logic
       # play sound if A was just button_just_pressed
#       if a_button == constants.button_state["button_just_pressed"]:
           # fire a laser, if we have enough power (have not used up all the
           # lasers)
#           for laser_number in range(len(lasers)):
#               if lasers[laser_number].x < 0:
#                   lasers[laser_number].move(ship.x, ship.y)
#                   sound.play(pew_sound)
#                   break
               
        # each frame move the lasers, that have been fired up and set neopixels 
        # to yellow when laser is on screen.
#       for laser_number in range(len(lasers)):
#           if lasers[laser_number].x > 0:
#               lasers[laser_number].move(lasers[laser_number].x,
#                                          lasers[laser_number].y - 
#                                          constants.LASER_SPEED)
#               neopixels[laser_number] = (10, 10, 0)
#               if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
#                   lasers[laser_number].move(constants.OFF_SCREEN_X,
#                                             constants.OFF_SCREEN_Y)
              
   
       #Set neopixel to red if all 5 lasers are on screen. 
       if (neopixels[0] == (10,10,0) and neopixels[1] == (10,10,0) and 
           neopixels[2] == (10,10,0) and neopixels[3] == (10,10,0) and 
           neopixels[4] == (10,10,0)):
           neopixels[0] = (10, 0, 0)
           neopixels[1] = (10, 0, 0)
           neopixels[2] = (10, 0, 0)
           neopixels[3] = (10, 0, 0)
           neopixels[4] = (10, 0, 0)
       
       #each frame move the aliens down, that are on the screen
#       for alien_number in range(len(aliens)):
#           if aliens[alien_number].x > 0:
#               aliens[alien_number].move(aliens[alien_number].x,
#                                         aliens[alien_number].y +
#                                         constants.ALIEN_SPEED)
#               if aliens[alien_number].y > constants.SCREEN_Y:
#                    aliens[alien_number].move(constants.OFF_SCREEN_X,
#                                              constants.OFF_SCREEN_Y)
#                    show_alien()
#                    score -= 1
#                    if score < 0:
#                        score = 0 
#                    score_text.clear()
#                    score_text.cursor(0,0)
#                    score_text.move(1,1)
#                    score_text.text("Score: {0}".format(score))

    # each frame check if any of the lasers are touching any of the aliens
#       for laser_number in range(len(lasers)):
#           if lasers[laser_number].x > 0:
#              for alien_number in range(len(aliens)):
#                   if aliens[alien_number].x > 0:
#                       if stage.collide(lasers[laser_number].x + 6,
#                                    lasers[laser_number].y + 2,
#                                    lasers[laser_number].x + 11,
#                                    lasers[laser_number].y + 12,
#                                    aliens[alien_number].x + 1,
#                                    aliens[alien_number].y,
#                                    aliens[alien_number].x + 15,
#                                    aliens[alien_number].y + 15):
                        # you hit an alien
#                           aliens[alien_number].move(constants.OFF_SCREEN_X,
#                                                  constants.OFF_SCREEN_Y)
#                           lasers[laser_number].move(constants.OFF_SCREEN_X,
#                                                  constants.OFF_SCREEN_Y)
#                           sound.stop()
#                           sound.play(boom_sound)
#                           show_alien()
#                           show_alien()
#                           score = score + 1
#                           score_text.clear()
#                           score_text.cursor(0,0)
#                           score_text.move(1,1)
#                           score_text.text("Score: {0}".format(score))
       
       # each frame cheack if any aliens are touching the space ship
#       for alien_number in range (len(aliens)):
#           if aliens[alien_number].x > 0:
#               if stage.collide(aliens[alien_number].x + 1,
#               aliens[alien_number].y, aliens[alien_number].x + 15,
#               aliens[alien_number].y + 15, ship.x, ship.y, ship.x + 15, 
#               ship.y + 15):
                # alien hit the ship
#                    sound.stop()
#                    sound.play(crash_sound)
#                    neopixels[0] = (10, 0, 0)
#                    neopixels[1] = (10, 0, 0)
#                    neopixels[2] = (10, 0, 0)
#                    neopixels[3] = (10, 0, 0)
#                    neopixels[4] = (10, 0, 0)
#                    neopixels.show()
#                    time.sleep(3.0)
#                    neopixels[0] = (0, 0, 0)
#                    neopixels[1] = (0, 0, 0)
#                    neopixels[2] = (0, 0, 0)
#                    neopixels[3] = (0, 0, 0)
#                    neopixels[4] = (0, 0, 0)
#                    neopixels.show()
#                    game_over_scene(score)
       # redraw sprites
       neopixels.show()
       game.render_sprites([snake])
       game.tick()
       
       
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
