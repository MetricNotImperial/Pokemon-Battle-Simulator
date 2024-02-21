"""
Author: Shubh Patel
Program: pokemon.py
Description: The game takes user_input through out the code, to make decisions for level picking, pokemon picking, as well as the moves pokemons use.
            All of these things are used to determine, the battle sequence of the user and the computer against each other, by changing the level, pokemon in the team, and the pokemon moves picked.
"""


import os
import time
import copy
import random
import math

################################################################################
#functions for editing the screen

#function will edit images based of lists on the screen
#makes sure the img is in a rectangle and empty spaces should have spaces
#img is the list of the image, x and y is where it is located
#characters are the characters u do not want on the image but are just place holders, the default is just space
def edit_screen(img,x,y,screen,characters = [" "]):
    #gets how many characters are in each row
    x_length = len(img[0])
    #gets how many rows there are
    y_length = len(img)
    
    #adds the img to the screen list
    for i in range(y_length):
        for j in range(x_length):
             #checks if the space is empty before replacing that character on the screen
            if img[i][j] not in characters:
                screen[y+i][x+j] = img[i][j]


#this function will take the a list with every row in a 2d list is a whole row of the ascii code, and will make it so that every character in that row is it's own index
#an example of this function is used in the title screen
def text_to_list(img_list):
    #new list the characters will be stored as each index, as a 2d list
    new_img_list = []
    
    #adds the amount of rows needed to the list
    for i in range(len(img_list)):
        #adds new rows to the list
        new_img_list.append([])
    

    #adds the characters to the list depending on the amount of rows and columns
    for i in range(len(img_list)):
        #adds the characters to the list
        for j in range(len(img_list[0][0])):
            new_img_list[i].append(img_list[i][0][j])
    
    return new_img_list

#function to open title screen
def title_screen(screen):
    
    #clears the screen first
    clear_screen(screen)

    #a temporary list to iterate through to create a list with every character as there own index in a different list below
    #this ascii art will be displayed on the title screen
    #80x13
    pokemonTemp = [ ["                                          ╓██                                   "],
                    ["                                         ██▀██╦                                 "],
                    ["                            ╓╦╦╦█╦     ▄█▀▄▄▀╜        ╦╦╦╦╦                     "],
                    ["    ╓╦▓██▀▀▀▀████╗     ▄▓██▀▀████▀██╖ ██████▓╦╖ ███▀▀██▌▀▐█▄    ███▄╦╦╖         "],
                    [" ▄██▀           ▀██╕   ████  ▐█▀   ▀██▀▀ ▄▄  ▀████   ▐█   ██    ████▀▀▀█████▄╦╦╖"],
                    [" ███▄      ╒███▄  ██   ▄███  └    ▄██▌ ▄█ █▀ ▄████    ▀   ██╥╦█████▌   ███   ▐█ "],
                    ["  █████▄    █▌██ ▐██▀▀██▀███    ▄██╓█  ▐█▀ ▄█▀███▌        ██▀▄█▀ ▄▀██  ▐██   █▌ "],
                    ["   ╚╜███▄   ▐█▀ ▄██ ▄██▄▄▌▐██     ▀▀██▄       ▄██▀  █▄ ▄ ██ ▐████▀ ██ ▄ ▓─  ██  "],
                    ["      ███▄   ▄▄███   ▀██▀  █▌ ███▄▄  ▀██████████▌  ▐██▄█▌██   ▀   ╓█▀▐▌    ▐█   "],
                    ["       ███▄  ▐█████       ██  ██▀█████▄▄ ██  ╒███████████▀██▄▄▄▄▄██  █▌   ╒█╛   "],
                    ["        ███▄  ▓██████▄▄█████▄▄██     ██████          █████████╙ ███▄▄█▌   ██    "],
                    ["         ███▄  ██   ▀▀   └▀╙             ▀                 ▀▀╙   ▀▀▀███  ██     "],
                    ["          █████▀╙                                                   ▀█████      "]]
    
    #a temporary list to iterate through to create a list with every character as there own index
    #this will be placed on the screen
    #43x21
    pikachuTemp = [["                          ▄█               "],
                   ["▐▄▄▄                     ███               "],
                   ["  ███░▒╔╖               ▐░▀█               "],
                   ["    ▀▌╖░░░▒╥            ░░░█               "],
                   ["       ╙▓╖░░░╦╗╦╗╗╗╖   ║░░░                "],
                   ["           ▀░░░░░░░░░░╥╢░░▓                "],
                   ["         ┌▒▄▌╣░░░░░░░░░░░╫                 "],
                   ["        ╓▓░▀▀▀░░░░░░░▒░░░                  "],
                   ["        ▒╢░░░░███▄░░▀██░░                  "],
                   ["        ╣▀░░░▐╢▒╢▓▀░░░░░▌  ╓╥╕             "],
                   ["      ╓╓╖░░░░░▒╢╫▀░░░╔▒▒▀░░░░╓             "],
                   ["    ╓░░░░░░░░░░░░░░░░╠▀░░░░░▀▒▒╥╗╗╦╥       "],
                   ["    ╚░░░░░░░░░▀╜░░░░░░░░╓╢▀░░░░░░░░░░░░▒▒╦╖"],
                   ["      ╙▒╨╜▀░░░░░░░░░░░▒╩  ▐░╢╢▓╗░░░░░░░░░╜ "],
                   ["      ╢░░░░░░░░░░░░░░░    ░╟▒▀╙▀▓╢▒╖░░▒╜   "],
                   ["      ▐░░░░░░░░░░░░░░░░ ▓▓╖░▒              "],
                   ["     ░░░░░░░░░░░░░░░░░▄██▌                 "],
                   ["    ▒░░░░░░░░░░░░░░░░░░▀▀                  "],
                   ["    ╙▒▓▓╗╥╥╥╗╬▓▓▓▓▓╗╖░░                    "],
                   ["  ┌██░╢╩▀      ▀╙╙╩▒▒▒▒▄                   "],
                   ["                       ╙▀▀                 "]]
    
    
    #temporary lists for the buttons displayed on the title screen
    #10x42
    startTemp = [[" ██████╗████████╗ █████╗ ██████╗ ████████╗"],
                 ["██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝"],
                 ["╚█████╗    ██║   ███████║██████╔╝   ██║   "],
                 [" ╚═══██╗   ██║   ██╔══██║██╔══██╗   ██║   "],
                 ["██████╔╝   ██║   ██║  ██║██║  ██║   ██║   "],
                 ["╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   "]]
    
    #10x37
    guideTemp = [[" ██████╗ ██╗   ██╗██╗██████╗ ███████╗"],
                 ["██╔════╝ ██║   ██║██║██╔══██╗██╔════╝"],
                 ["██║  ██╗ ██║   ██║██║██║  ██║█████╗  "],
                 ["██║  ╚██╗██║   ██║██║██║  ██║██╔══╝  "],
                 ["╚██████╔╝╚██████╔╝██║██████╔╝███████╗"],
                 [" ╚═════╝  ╚═════╝ ╚═╝╚═════╝ ╚══════╝"]]
    
    #the 2d list as every charcter is it's owns index to pass into edit_screen function to display on the title screen
    pokemon_img = text_to_list(pokemonTemp)
    
    #the 2d list every character of pikachu will take to be put on the screen
    pikachu_img = text_to_list(pikachuTemp)
    
    #the 2d list above with every character of the buttons for start and guide will be converted into lists with each character as its own index
    start_img = text_to_list(startTemp)
    
    guide_img = text_to_list(guideTemp)
    
    #edits the screen to add the pokmon_img 10 down from the top and 10 left from the left side
    edit_screen(pokemon_img,10,3,screen)
    
    #adds pikachu to the screen
    edit_screen(pikachu_img,52,17,screen)
    
    #adds where the buttons will be on the screen
    edit_screen(start_img,10,22,screen)
    
    edit_screen(guide_img,10,30,screen)
    

#function for the guide screen
def guide_screen(screen):
    #"┏","┓","┗","┛","━","┃"
    backTemp = [["┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"],
                ["┃ ██████╗  █████╗  █████╗ ██╗  ██╗ ┃"],
                ["┃ ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝ ┃"],
                ["┃ ██████╦╝███████║██║  ╚═╝█████═╝  ┃"],
                ["┃ ██╔══██╗██╔══██║██║  ██╗██╔═██╗  ┃"],
                ["┃ ██████╦╝██║  ██║╚█████╔╝██║ ╚██╗ ┃"],
                ["┃ ╚═════╝ ╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ┃"],
                ["┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"]]
    
    back_img = text_to_list(backTemp)
    
    clear_screen(screen)
    
    #adds all the lines of the guide onto the screen
    edit_screen(["Welcome to Pokemon Budget Version. In this game you will get a chance to use pokemon from"],5,5,screen)
    edit_screen(["the famous franchise to battle in 5 distinct levels to win the game."],16,6,screen)
    
    edit_screen(["How To Play?"],44,8,screen)
    edit_screen(["The controls of the game are very simple, use 'w'/'s' Or 'a'/'d' to move the buttons and 'q' to"],2,9,screen)
    edit_screen(["select a choice. Remember to click 'enter after each input'. And lastly make sure to input only"],2,10,screen)
    edit_screen(["one character at a time."],38,11,screen)
    
    edit_screen(["Pokemon is a game where you get monsters and battle with them to win. In this game there are"],4,13,screen)
    edit_screen(["5 levels. Each level number will correspond to the amount of pokemon you can have in your"],5,14,screen)
    edit_screen(["team, as well the amount the opposing team will have in theirs. You will get to choose from a "],3,15,screen)
    edit_screen(["selection of 10 pokemon, to be in your team. Each pokemon has types, sometimes 2, each "],7,16,screen)
    edit_screen(["pokemon has 2 moves, which also have their own types, a starting health amount, and a speed."],4,17,screen)
    edit_screen(["Each of these stats are unique to every pokemon."],26,18,screen)
    
    edit_screen(["The player and the computer will play each other and the person with no pokemon left first"],5,20,screen)
    edit_screen(["loses. You and the computer will attack first based on the choice of that turn, as well as the"],3,21,screen)
    edit_screen(["speed of the pokemon to a selection of two moves. You can also switch to another alive"],7,22,screen)
    edit_screen(["pokemon in your team if you have any."],37,23,screen)
    
    edit_screen(["After beating every level the next level will be unlocked, as well as the completed level having a"],1,25,screen)
    edit_screen(["checkmark beside it. You can not replay levels that you have already beat."],13,26,screen)
    
    edit_screen(back_img,34,30,screen)
    print_screen(screen)
    
    while True:
        user_input = input("")
        if user_input == "q":
            break

#function that will present the level selection screen, aswell  as the levels that hae been completed and unlocked 
def levels_screen(screen,record):
    #clears the screen of anything first
    clear_screen(screen)
    
    #temp lists to be used later to display on the screen
    #dimensions for all of them are 6x51
    levelOneTemp = [["██╗     ███████╗██╗   ██╗███████╗██╗         ███╗  "], 
                    ["██║     ██╔════╝██║   ██║██╔════╝██║        ████║  "], 
                    ["██║     █████╗  ╚██╗ ██╔╝█████╗  ██║       ██╔██║  "], 
                    ["██║     ██╔══╝   ╚████╔╝ ██╔══╝  ██║       ╚═╝██║  "], 
                    ["███████╗███████╗  ╚██╔╝  ███████╗███████╗  ███████╗"], 
                    ["╚══════╝╚══════╝   ╚═╝   ╚══════╝╚══════╝  ╚══════╝"]]
                    
    levelTwoTemp = [["██╗     ███████╗██╗   ██╗███████╗██╗       ██████╗ "], 
                    ["██║     ██╔════╝██║   ██║██╔════╝██║       ╚════██╗"], 
                    ["██║     █████╗  ╚██╗ ██╔╝█████╗  ██║         ███╔═╝"], 
                    ["██║     ██╔══╝   ╚████╔╝ ██╔══╝  ██║       ██╔══╝  "], 
                    ["███████╗███████╗  ╚██╔╝  ███████╗███████╗  ███████╗"], 
                    ["╚══════╝╚══════╝   ╚═╝   ╚══════╝╚══════╝  ╚══════╝"]]
                    
    levelThreeTemp = [["██╗     ███████╗██╗   ██╗███████╗██╗       ██████╗ "], 
                      ["██║     ██╔════╝██║   ██║██╔════╝██║       ╚════██╗"], 
                      ["██║     █████╗  ╚██╗ ██╔╝█████╗  ██║        █████╔╝"], 
                      ["██║     ██╔══╝   ╚████╔╝ ██╔══╝  ██║        ╚═══██╗"], 
                      ["███████╗███████╗  ╚██╔╝  ███████╗███████╗  ██████╔╝"], 
                      ["╚══════╝╚══════╝   ╚═╝   ╚══════╝╚══════╝  ╚═════╝ "]]
                    
    levelFourTemp = [["██╗     ███████╗██╗   ██╗███████╗██╗         ██╗██╗"], 
                     ["██║     ██╔════╝██║   ██║██╔════╝██║        ██╔╝██║"], 
                     ["██║     █████╗  ╚██╗ ██╔╝█████╗  ██║       ██╔╝ ██║"], 
                     ["██║     ██╔══╝   ╚████╔╝ ██╔══╝  ██║       ███████║"], 
                     ["███████╗███████╗  ╚██╔╝  ███████╗███████╗  ╚════██║"], 
                     ["╚══════╝╚══════╝   ╚═╝   ╚══════╝╚══════╝       ╚═╝"]]
                    
    levelFiveTemp = [["██╗     ███████╗██╗   ██╗███████╗██╗       ███████╗"], 
                     ["██║     ██╔════╝██║   ██║██╔════╝██║       ██╔════╝"], 
                     ["██║     █████╗  ╚██╗ ██╔╝█████╗  ██║       ██████╗ "], 
                     ["██║     ██╔══╝   ╚████╔╝ ██╔══╝  ██║       ╚════██╗"], 
                     ["███████╗███████╗  ╚██╔╝  ███████╗███████╗  ██████╔╝"], 
                     ["╚══════╝╚══════╝   ╚═╝   ╚══════╝╚══════╝  ╚═════╝ "]]
    
    
    #the temporary lists for the completed, locked and unlocked levels
    
    #6x13
    lockedTemp =[["  █████████  "],
                 [" ██       ██ "],
                 ["█████████████"],
                 ["█████ █ █████"],
                 ["█████   █████"],
                 ["█████████████"]]
    
    #6x13
    unlockedTemp = [["     ██████  "],
                    ["          ██ "],
                    ["█████████████"],
                    ["█████   █████"],
                    ["█████   █████"],
                    ["█████████████"]]
    #6x16 
    completedTemp =[["              ██"],
                    ["            ██  "],
                    ["██        ██    "],
                    [" ██     ██      "],
                    ["  ██  ██        "],
                    ["   ████         "]] 
    
    
    #the 2d lists for levels that have been locked and unlocked, aswell as levels that are completed and not completed
    locked_img = text_to_list(lockedTemp)
    
    unlocked_img = text_to_list(unlockedTemp)
    
    completed_img = text_to_list(completedTemp)
    
    
    #the 2d list above with every character of the buttons for start and guide will be converted into lists with each character as its own index
    level_one_img = text_to_list(levelOneTemp)
    
    level_two_img = text_to_list(levelTwoTemp)
    
    level_three_img = text_to_list(levelThreeTemp)
    
    level_four_img = text_to_list(levelFourTemp)
    
    level_five_img = text_to_list(levelFiveTemp)
    
    #this will render all of the levels on to the screen
    edit_screen(level_one_img,25,3,screen)
    edit_screen(level_two_img,25,10,screen)
    edit_screen(level_three_img,25,17,screen)
    edit_screen(level_four_img,25,24,screen)    
    edit_screen(level_five_img,25,31,screen)
    
    #will add symbols beside the levels if, indicating if they are completed aswell as if they are unlocked or locked
    for i in range(5):
        #for the locked levels
        if record[0][i] == "unlocked":
            edit_screen(unlocked_img,6,(3+7*i),screen)
        elif record[0][i] == "locked":
            edit_screen(locked_img,6,(3+7*i),screen)
        
        #for the completed levels
        if record[1][i] == "completed":
            edit_screen(completed_img,80,(3+7*i),screen)
        
#function for the ending of the game when every level is done to congratulate the player
def end_screen(screen):
    #temporary lists for the things to be displayed on the screen
    congratsTemp =[[" █████╗  █████╗ ███╗  ██╗ ██████╗ ██████╗  █████╗ ████████╗ ██████╗"],
                   ["██╔══██╗██╔══██╗████╗ ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝"],
                   ["██║  ╚═╝██║  ██║██╔██╗██║██║  ██╗ ██████╔╝███████║   ██║   ╚█████╗ "],
                   ["██║  ██╗██║  ██║██║╚████║██║  ╚██╗██╔══██╗██╔══██║   ██║    ╚═══██╗"],
                   ["╚█████╔╝╚█████╔╝██║ ╚███║╚██████╔╝██║  ██║██║  ██║   ██║   ██████╔╝"],
                   [" ╚════╝  ╚════╝ ╚═╝  ╚══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝ "]]
                   
    youBeatTemp = [["██╗   ██╗ █████╗ ██╗   ██╗  ██████╗ ███████╗ █████╗ ████████╗"],
                   ["╚██╗ ██╔╝██╔══██╗██║   ██║  ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝"],
                   [" ╚████╔╝ ██║  ██║██║   ██║  ██████╦╝█████╗  ███████║   ██║   "],
                   ["  ╚██╔╝  ██║  ██║██║   ██║  ██╔══██╗██╔══╝  ██╔══██║   ██║   "],
                   ["   ██║   ╚█████╔╝╚██████╔╝  ██████╦╝███████╗██║  ██║   ██║   "],
                   ["   ╚═╝    ╚════╝  ╚═════╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   "]]
                   
    theGameTemp = [["████████╗██╗  ██╗███████╗   ██████╗  █████╗ ███╗   ███╗███████╗"],
                   ["╚══██╔══╝██║  ██║██╔════╝  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝"],
                   ["   ██║   ███████║█████╗    ██║  ██╗ ███████║██╔████╔██║█████╗  "],
                   ["   ██║   ██╔══██║██╔══╝    ██║  ╚██╗██╔══██║██║╚██╔╝██║██╔══╝  "],
                   ["   ██║   ██║  ██║███████╗  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗"],
                   ["   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝"]]
    
    #lists for what will be played on the screen
    congrats_img = text_to_list(congratsTemp)
    youBeat_img = text_to_list(youBeatTemp)
    theGame_img = text_to_list(theGameTemp)
    
    clear_screen(screen)
    
    #puts the images on the screen
    edit_screen(congrats_img,16,10,screen)
    edit_screen(youBeat_img,19,18,screen)
    edit_screen(theGame_img,18,26,screen)
    
    print_screen(screen)

#function will clear the screen and will remove any characters
def clear_screen(screen):
    #this for loop and nested for loop will iterate through every character on the screen and make it a space
    for i in range(len(screen)):
        for j in range(len(screen[0])):
            #checks if the current character they are on is one of the wall and if it is not then it will make it a space meaning clear it
            if i != 0 and i != 39 and j != 0 and j != 99:
                screen[i][j] = " "
            #"┏","┓","┗","┛","━","┃"
            elif i == 0 and j == 0:
                screen[i][j] = "┏"
            elif i == 0 and j > 0 and j < 99:
                screen[i][j] = "━"
            elif i == 0 and j == 99:
                screen[i][j] = "┓"
            elif i > 0 and i < 39 and (j == 0 or j == 99):
                screen[i][j] = "┃"
            elif i == 39 and j == 0:
                screen[i][j] = "┗"
            elif i == 39 and j > 0 and j < 99:
                screen[i][j] = "━"
            elif i == 39 and j == 99:
                screen[i][j] = "┛"
                
            
#this function will clear an image on the screen
def clear_img(height,width,x,y,screen):
    
    #iterates through every character in the img on the screen and makes it into a space
    for i in range(height):
        for j in range(width):
            screen[y+i][x+j] = " "


#function to print out the screen
def print_screen(screen):
    #clears the screen first before printing out the screen
    os.system("clear")
    
    val = ""
    #prints the screen out
    for i in range(40):
        for j in range(100):
            val = val + screen[i][j]
        print(val)
        val = ""

#a function that will return what the users choices on based on the button they chose
#heights and widths are for the dimensions of the imgs, x and y are the location of the buttons on the screen and quantity is the amount of buttons on the screen 
#the buttons work that if the set is vertical the top most button is x = 0 or if horizontal the left is x = 0
#the characters are for what the outline of the button is made of those are the default if none are put in
def button(heights,widths,x,y,quantity,button_names,screen,characters = ["┏","┓","┗","┛","━","┃"," "]):
    #the variable used to see what button the user is on right now
    n = 0
    #variable used to contain the characters for the button
    button_list = []
    while True:
        ####################
        #this value stores the what the old button looked like without the outline of the button
        old_button_list = []
        
        #gets the old values into the list
        #this value will be used later to delete the outline around the part under the list
        for i in range((heights[n])):
            old_button_list.append([])
        
        for i in range((heights[n])):
            for j in range((widths[n])):
                old_button_list[i].append(screen[(y[n]+i)][(x[n]+j)])
        
        ####################
        #variable used to contain the characters for the button
        button_list = []
        
        #prints button on n = 0 and each time the while loop iterates this changes to the new value of n
        
        #adds 2 more then the amount of the height to the list
        for i in range((heights[n]+2)):
            button_list.append([])
            
        #adds the first row
        button_list[0].append(characters[0])
        for i in range(widths[n]):
            button_list[0].append(characters[4])
        button_list[0].append(characters[1])
        
        
        #adds the rows in between the first and last row the button
        for i in range(heights[n]):
            for j in range(widths[n]+2):
                if j == 0 or j == (widths[n]+1):
                    button_list[i+1].append(characters[5])
                else:
                    button_list[i+1].append(characters[6])
        
        #adds the last row in the buttons list
        button_list[-1].append(characters[2])
        for i in range(widths[n]):
            button_list[-1].append(characters[4])
        button_list[-1].append(characters[3])
        
        edit_screen(button_list,(x[n]-1),(y[n]-1),screen)
        print_screen(screen)
        #####################
        #asks the user to go, w for up, s for down, or q for picking that option
        user_input = input("").lower()
        
        #these if statements keep track of what button the user is on aswell the one they select
        if user_input == "w" or user_input == "a":
            #clears the button from the screen along with the image under it
            clear_img((heights[n]+2),(widths[n]+2),(x[n]-1),(y[n]-1),screen)
            #adds the old image back
            edit_screen(old_button_list,x[n],y[n],screen)
            
            n = n - 1
            #checks if n went lower then 0 and brings it back to the top
            if n < 0:
                n = quantity - 1
        elif user_input == "s" or user_input == "d":
            #clears the button from the screen along with the image under it
            clear_img((heights[n]+2),(widths[n]+2),(x[n]-1),(y[n]-1),screen)
            #adds the old image back
            edit_screen(old_button_list,x[n],y[n],screen)
            
            n = n + 1
            #checks if n went over the amount of buttons and brings it back to the top
            if n == quantity:
                n = 0
            
        elif user_input == "q":
            #clears the button from the screen along with the image under it
            clear_img((heights[n]+2),(widths[n]+2),(x[n]-1),(y[n]-1),screen)
            #adds the old image back
            edit_screen(old_button_list,x[n],y[n],screen)
            break
    
    #this is the name of the choice the user picked from the buttons
    choice = button_names[n]
    
    return choice


################################################################################
#makes a list for what everyone will see on the console which is a 100x40 character image
screen = []

#will add 50 rows to the screen to make it 100 by 40
for i in range(40):
    screen.append([])

screen[0].append("┏")
#adds the top of the list with a length of 100
for i in range(98):
    screen[0].append("━")
screen[0].append("┓")
    
#adds the sides and empty middle of the screen with a height of 40
for i in range(38):
    
    screen[i+1].append("┃")
    
    for p in range(98):
        screen[i+1].append(" ")
        
    screen[i+1].append("┃")


screen[39].append("┗")
#adds the bottem of the list with a length of 100
for i in range(98):
    screen[39].append("━")
screen[39].append("┛")



################################################################################
#everything to do with the classes po pokemon
#the type of each of the pokemon
class Type:
    def __init__(self, name, name_list):
        self.name = name
        self.name_list = name_list
    #returns the multiplier of what the base damage of a move is mulitplied, basically seeing if the attack will be nuetral meaning doing base damage, not effective of super effective
    #when called the pokemon being attacked is passed to find the type
    def multiplier(self, pokemonAttacked):
        
        #a list of every type name as a string
        type_list = ["Electric","Water","Fire","Grass","Fighting","Psychic","Steel","Rock","Flying","Dragon","Dark","Ground","Poison","Ice","Ghost"]
        
        
        #link to the effectiveness chart: https://docs.google.com/spreadsheets/d/1AypuRxZUQs6FiQgufvqdKj3beOzAQ-5sWzvIDStlVTU/edit#gid=0
        #a list that is used to find the multiplier of the move on the defending oppoisng pokemon
        effective_list = [[1/2,2,1,1/2,1,1,1,1,2,1/2,1,0,1,1,1], 
                        [1,1/2,2,1/2,1,1,1,2,1,1/2,1,2,1,1,1], 
                        [1,1/2,1/2,2,1,1,2,1/2,1,1/2,1,1,1,2,1], 
                        [1,2,1/2,1/2,1,1,1/2,2,1/2,1/2,1,2,1/2,1,1], 
                        [1,1,1,1,1,1/2,2,2,1/2,1,2,1,1/2,2,0], 
                        [1,1,1,1,2,1,1/2,1,1,1,0,1,2,1,1], 
                        [1/2,1/2,1/2,1,1,1,1/2,2,1,1,1,1,1,2,1], 
                        [1,1,2,1,1/2,1,1/2,1,2,1,1,1/2,1,2,1], 
                        [1/2,1,1,2,2,1,1/2,1/2,1,1,1,1,1,1,1], 
                        [1,1,1,1,1,1,1/2,1,1,2,1,1,1,1,1], 
                        [1,1,1,1,1/2,2,1,1,1,1,1/2,1,1,1,2], 
                        [2,1,2,1/2,1,1,2,2,0,1,1,1,2,1,1], 
                        [1,1,1,2,1,1,0,1/2,1,1,1,1,1/2,1,1/2], 
                        [1,1/2,1/2,2,1,1,1/2,1,2,2,1,2,1,1/2,1], 
                        [1,1,1,1,1,2,1,1,1,1,1/2,1,1,1,2]]
        
        
        #finds the x value of the 2d list used below to find the multiplier
        for i in range(15):
            #checks if the name of this type is the same name as the one of this index in a list and asigns x to the index value
            if self.name == type_list[i]:
                x = i
        
        for i in range(15):
            #checks if the name of the type of pokemon first type is the same name as the one of this index in a list and asigns y to the index value
            if pokemonAttacked.pokemon_type.name == type_list[i]:
                y1 = i
                
        #checks if the pokemon being attacked has a second type by seing if the name of type in the place as there second move is null
        if pokemonAttacked.pokemon_type_two.name != "null":
            for i in range(15):
                #checks if the name of the type of pokemon first type is the same name as the one of this index in a list and asigns y to the index value
                if pokemonAttacked.pokemon_type_two.name == type_list[i]:
                    y2 = i
        
        #gets the multiplier value for this move on that specific pokemon from the list
        multiplier = effective_list[x][y1]
        #checks if there is a second type and if there is then mulitplies the mulitplier value above with the effectiveness of the move on the other type to get the actual value
        if pokemonAttacked.pokemon_type_two.name != "null":
            multiplier = multiplier*effective_list[x][y2]
        
        return multiplier
        

#class of the moves the pokemon use to battle  
class Move:
    
    def __init__(self, name, moveType, baseDamage,name_list):
        self.name = name
        self.move_type = moveType
        self.base_damage = baseDamage
        self.name_list = name_list
    
#class of pokemon, the things used to battle with
class Pokemon:
    
    #everything that makes everyone pokemon unique is used in this constructer
    #each stat will determine how it is used in battle
    def __init__(self, moves, health, speed, pokemonType,pokemonType2,name,awake,name_list):
        self.attack_one = moves[0]
        self.attack_two = moves[1]
        self.pokemon_type =  pokemonType
        self.pokemon_type_two = pokemonType2
        self.health = health
        self.speed = speed
        self.name = name
        self.awake = awake
        self.name_list = name_list

    
    #function for attacks between pokemon
    #passes pokemon being attacked, aswell as the attack choice and if the user is attacked
    def attack(self, pokemonAttacked, attackChoice,before_img, userAttack = False):
        #these are temporary texts that will be displayed on the screen
        usedTemp = [["█ █ █▀ █▀▀ █▀▄"],
                    ["█▄█ ▄█ ██▄ █▄▀"]]
        
        superEffectiveTemp = [["█ ▀█▀   █ █ █ ▄▀█ █▀   █▀ █ █ █▀█ █▀▀ █▀█   █▀▀ █▀▀ █▀▀ █▀▀ █▀▀ ▀█▀ █ █ █ █▀▀"],
                              ["█  █    ▀▄▀▄▀ █▀█ ▄█   ▄█ █▄█ █▀▀ ██▄ █▀▄   ██▄ █▀  █▀  ██▄ █▄▄  █  █ ▀▄▀ ██▄"]]
    
        notVeryEffectiveTemp =[["█ ▀█▀   █ █ █ ▄▀█ █▀   █▄ █ █▀█ ▀█▀   █ █ █▀▀ █▀█ █▄█   █▀▀ █▀▀ █▀▀ █▀▀ █▀▀ ▀█▀ █ █ █ █▀▀"],
                               ["█  █    ▀▄▀▄▀ █▀█ ▄█   █ ▀█ █▄█  █    ▀▄▀ ██▄ █▀▄  █    ██▄ █▀  █▀  ██▄ █▄▄  █  █ ▀▄▀ ██▄"]]
    
        noEffectTemp = [["█ ▀█▀   █ █ ▄▀█ █▀▄   █▄ █ █▀█   █▀▀ █▀▀ █▀▀ █▀▀ █▀▀ ▀█▀"],
                        ["█  █    █▀█ █▀█ █▄▀   █ ▀█ █▄█   ██▄ █▀  █▀  ██▄ █▄▄  █ "]]
    
        faintedTemp =  [["█▀▀ ▄▀█ █ █▄ █ ▀█▀ █▀▀ █▀▄"],
                        ["█▀  █▀█ █ █ ▀█  █  ██▄ █▄▀"]]
                        
        fixTemp = [["┃██████████████████████████████████████████████████████████████████████████████████████████████████┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██████████████████████████████████████████████████████████████████████████████████████████████████┃"]]
        
        #this will be displayed on the screen
        used_img = text_to_list(usedTemp)
        superEffective_img = text_to_list(superEffectiveTemp)
        notVeryEffective_img = text_to_list(notVeryEffectiveTemp)
        noEffect_img = text_to_list(noEffectTemp)
        fainted_img = text_to_list(faintedTemp)
        fix_img = text_to_list(fixTemp)
        
        #if statements get the new value of health for the pokemon after attacked
        if attackChoice == 0:
            #changes the value of the pokemon being attacked by the base damage of the move times the multiplier based on the attacking moves type and the pokemon thats attacked type
            pokemonAttacked.health = int(pokemonAttacked.health - self.attack_one.base_damage*self.attack_one.move_type.multiplier(pokemonAttacked))
            #this code will show on the screen the move used, and its effectiveness
            edit_screen(before_img,0,0,screen,[])
            edit_screen(fix_img,0,26,screen,[])
            
            edit_screen(self.name_list,5,28,screen)
            edit_screen(used_img,7+len(self.name_list[0]),28,screen)
            
            if 9+len(self.name_list[0])+len(used_img[0])+len(self.attack_one.name_list[0]) >= 97:
                edit_screen(self.attack_one.name_list,5,32,screen)
            else:
                edit_screen(self.attack_one.name_list,9+len(self.name_list[0])+len(used_img[0]),28,screen)
            
            print_screen(screen)
            time.sleep(2)
            
            edit_screen(fix_img,0,26,screen,[])
            
            if self.attack_one.move_type.multiplier(pokemonAttacked) == 2 or self.attack_one.move_type.multiplier(pokemonAttacked) == 4:
                edit_screen(superEffective_img,5,28,screen)
            elif self.attack_one.move_type.multiplier(pokemonAttacked) == 1/2 or self.attack_one.move_type.multiplier(pokemonAttacked) == 1/4:
                edit_screen(notVeryEffective_img,5,28,screen)
            elif self.attack_one.move_type.multiplier(pokemonAttacked) == 0:
                edit_screen(noEffect_img,5,28,screen)
            
            if self.attack_one.move_type.multiplier(pokemonAttacked) != 1:
                print_screen(screen)
                time.sleep(2)
            
        elif attackChoice == 1:
            #changes the value of the pokemon being attacked by the base damage of the move times the multiplier based on the attacking moves type and the pokemon thats attacked type
            pokemonAttacked.health = int(pokemonAttacked.health - self.attack_two.base_damage*self.attack_two.move_type.multiplier(pokemonAttacked))
            #this code will show on the screen the move used, and its effectiveness
            edit_screen(before_img,0,0,screen,[])
            edit_screen(fix_img,0,26,screen,[])
            
            edit_screen(self.name_list,5,28,screen)
            edit_screen(used_img,7+len(self.name_list[0]),28,screen)
            
            if 9+len(self.name_list[0])+len(used_img[0])+len(self.attack_two.name_list[0]) >= 97:
                edit_screen(self.attack_two.name_list,5,32,screen)
            else:
                edit_screen(self.attack_two.name_list,9+len(self.name_list[0])+len(used_img[0]),28,screen)
            
            print_screen(screen)
            time.sleep(2)
            
            edit_screen(fix_img,0,26,screen,[])
            
            if self.attack_two.move_type.multiplier(pokemonAttacked) == 2 or self.attack_two.move_type.multiplier(pokemonAttacked) == 4:
                edit_screen(superEffective_img,5,28,screen)
            elif self.attack_two.move_type.multiplier(pokemonAttacked) == 1/2 or self.attack_two.move_type.multiplier(pokemonAttacked) == 1/4:
                edit_screen(notVeryEffective_img,5,28,screen)
            elif self.attack_two.move_type.multiplier(pokemonAttacked) == 0:
                edit_screen(noEffect_img,5,28,screen)
            
            if self.attack_two.move_type.multiplier(pokemonAttacked) != 1:
                print_screen(screen)
                time.sleep(2)
        
        
        #checks to see if pokemon has fainted by checking its hp points
        if pokemonAttacked.health <= 0:
            pokemonAttacked.health = 0
            pokemonAttacked.awake = False
            #will type on the screen that this pokemon has fainted
            edit_screen(before_img,0,0,screen,[])
            edit_screen(fix_img,0,26,screen,[])
            
            edit_screen(pokemonAttacked.name_list,5,28,screen)
            edit_screen(fainted_img,7+len(pokemonAttacked.name_list[0]),28,screen)
            print_screen(screen)
            time.sleep(3)
################################################################################
#a function to run a battle sequence
#it takes the users team aswell as the computers selected team
def battle(user_team,comp_team,number_list,screen):
    #it will create a list that will have the bottem secition of the screen where the attack and switch will be
    #temporary lists that will be displayed on the screen
    #13x98 location x:1 y:26
    bottom_screenTemp = [["██████████████████████████████████████████████████████████████████████████████████████████████████"],
                         ["██                                                                                              ██"],
                         ["██████████████████████████████████████████████████████████████████████████████████████████████████"],
                         ["██ ██                                         ██  ██                                         ██ ██"],
                         ["██ ██                                         ██  ██                                         ██ ██"],
                         ["██ ██                                         ██  ██                                         ██ ██"],
                         ["██ ██                                         ██  ██                                         ██ ██"],
                         ["██ ██                                         ██  ██                                         ██ ██"],
                         ["██ ██                                         ██  ██                                         ██ ██"],
                         ["██ ██                                         ██  ██                                         ██ ██"],
                         ["██████████████████████████████████████████████████████████████████████████████████████████████████"],
                         ["██                                                                                              ██"],
                         ["██████████████████████████████████████████████████████████████████████████████████████████████████"]]
    #28x40 "┏","┓","┗","┛","━","┃"," "
    switch_selectionTemp = [["┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┃                                      ┃"],
                            ["┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"]]
    
    #2x23
    attackTemp = [["▄▀█ ▀█▀ ▀█▀ ▄▀█ █▀▀ █▄▀"],
                  ["█▀█  █   █  █▀█ █▄▄ █ █"]]
    #2x22
    switchTemp = [["█▀ █ █ █ █ ▀█▀ █▀▀ █ █"],
                  ["▄█ ▀▄▀▄▀ █  █  █▄▄ █▀█"]]
                  
    switchedTemp = [["█▀ █ █ █ █ ▀█▀ █▀▀ █ █ █▀▀ █▀▄"],
                    ["▄█ ▀▄▀▄▀ █  █  █▄▄ █▀█ ██▄ █▄▀"]]
    
    youTemp = [["█▄█ █▀█ █ █"],
               [" █  █▄█ █▄█"]]
    
    toTemp = [["▀█▀ █▀█"],
              [" █  █▄█"]]
    
    opponenetTemp = [["█▀█ █▀█ █▀█ █▀█ █▄ █ █▀▀ █▄ █ ▀█▀"],
                     ["█▄█ █▀▀ █▀▀ █▄█ █ ▀█ ██▄ █ ▀█  █ "]]
    
    hpTemp = [["█  █  █▀▀█"],
              ["█▀▀█  █▄▄█"],
              ["█  █  █   "]]
              
              
    backTemp = [["█▄▄ ▄▀█ █▀▀ █▄▀"],
                ["█▄█ █▀█ █▄▄ █ █"]]
    
    backAttackTemp = [["███████████████████████"],
                      ["██                   ██"],
                      ["██  █▄▄ ▄▀█ █▀▀ █▄▀  ██"],
                      ["██  █▄█ █▀█ █▄▄ █ █  ██"],
                      ["██                   ██"]]

    
                  
    fixTemp = [["┃██████████████████████████████████████████████████████████████████████████████████████████████████┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██                                                                                              ██┃"],
                   ["┃██████████████████████████████████████████████████████████████████████████████████████████████████┃"]]

 
    #images that will be on the screen
    bottom_screen_img = text_to_list(bottom_screenTemp)
    attack_img = text_to_list(attackTemp)
    switch_img = text_to_list(switchTemp)
    you_img = text_to_list(youTemp)
    opponent_img = text_to_list(opponenetTemp)
    bracket_img =[[" "," ","▄","▀"],
                  ["▄","▀"," "," "]]
    hp_img = text_to_list(hpTemp)
    back_img = text_to_list(backTemp)
    
    switch_selection_img = text_to_list(switch_selectionTemp)
    backAttack_img = text_to_list(backAttackTemp)
    switched_img = text_to_list(switchedTemp)
    
    fix_img = text_to_list(fixTemp)
    to_img = text_to_list(toTemp)
    #runs until the battle end
    while True:
        #clears the screen
        clear_screen(screen)
        #adds the bottom screen with holes for where the button goes
        edit_screen(bottom_screen_img,1,26,screen,[])
        #adds the attakc button
        edit_screen(attack_img,15,31,screen)
        #adds the switch button
        edit_screen(switch_img,63,31,screen)
        
        #will show the your pokemon and its stats, aswell the opponents pokemon and its stats
        #your pokemon part
        edit_screen(you_img,1,1,screen)
        edit_screen(user_team[0].name_list,1,4,screen)
        edit_screen(user_team[0].pokemon_type.name_list,1,7,screen)
        #checks to see if your pokemon has a second type and if it does adds it to the screen aswell
        if user_team[0].pokemon_type_two.name != "null":
            #adds a bracket in between the two types
            edit_screen(bracket_img,(len(user_team[0].pokemon_type.name_list[0])+2),7,screen)
            edit_screen(user_team[0].pokemon_type_two.name_list,1,10,screen)
            edit_screen(hp_img,1,13,screen)
            for i in range(len(str(user_team[0].health))):
                value = str(user_team[0].health)
                value = int(value[i])
                num_img = number_list[value]
                edit_screen(num_img,13+i*5,13,screen)
        else:
            edit_screen(hp_img,1,10,screen)
            for i in range(len(str(user_team[0].health))):
                value = str(user_team[0].health)
                value = int(value[i])
                num_img = number_list[value]
                edit_screen(num_img,13+i*5,10,screen)
        #opponent pokemon part
        
        edit_screen(opponent_img,66,1,screen)
        edit_screen(comp_team[0].name_list,99-len(comp_team[0].name_list[0]),4,screen)
        
        #checks to see if opponents pokemon has a second type and if it does adds it to the screen aswell
        if comp_team[0].pokemon_type_two.name != "null":
            edit_screen(comp_team[0].pokemon_type.name_list,93-len(comp_team[0].pokemon_type.name_list[0]),7,screen)
            #adds a bracket in between the two types
            edit_screen(bracket_img,98-(len(bracket_img[0])),7,screen)
            edit_screen(comp_team[0].pokemon_type_two.name_list,99-len(comp_team[0].pokemon_type_two.name_list[0]),10,screen)
        
            edit_screen(hp_img,97-5*len(str(comp_team[0].health))-len(hp_img[0]),13,screen)
            
            for i in range(len(str(comp_team[0].health))):
                value = str(comp_team[0].health)
                value = int(value[i])
                num_img = number_list[value]
                edit_screen(num_img,99-5*len(str(comp_team[0].health))+i*5,13,screen)
        
        else:
            edit_screen(comp_team[0].pokemon_type.name_list,99-len(comp_team[0].pokemon_type.name_list[0]),7,screen)
            edit_screen(hp_img,97-5*len(str(comp_team[0].health))-len(hp_img[0]),10,screen)
            for i in range(len(str(comp_team[0].health))):
                value = str(comp_team[0].health)
                value = int(value[i])
                num_img = number_list[value]
                edit_screen(num_img,99-5*len(str(comp_team[0].health))+i*5,10,screen)
        
        
        
        #sees if the user wants to attack with the current pokemon or switch to another
        userChoice = button([2,2],[25,25],[14,62],[31,31],2,["attack","switch"],screen)
        
        #checks if the user entered attack and will show the options to attack with
        if userChoice == "attack":
            #this will copy what the part above the text bubble looked like into a list
            beforeAttack_img = []
            for i in range(26):
                beforeAttack_img.append([])
            for i in range(26):
                for j in range(100):
                    beforeAttack_img[i].append(screen[i][j])
            
            #clears attack and switch from where the two moves used to attack will be
            clear_img(7,92,4,29,screen)
            
            #adds all the buttons onto the screen, the moves of the pokemon aswell as the back button
            edit_screen(user_team[0].attack_one.name_list,(91-len(user_team[0].attack_one.name_list[0])-len(user_team[0].attack_two.name_list[0]))//2+3,31,screen)
            edit_screen(user_team[0].attack_two.name_list,math.ceil((91-len(user_team[0].attack_one.name_list[0])-len(user_team[0].attack_two.name_list[0]))/2)+6+len(user_team[0].attack_one.name_list[0]),31,screen)
            edit_screen(backAttack_img,38,21,screen)
            
            #puts the types on the screen underneath the moves
            edit_screen(user_team[0].attack_one.move_type.name_list,((91-len(user_team[0].attack_one.name_list[0])-len(user_team[0].attack_two.name_list[0]))//2+3)+len(user_team[0].attack_one.name_list[0])-len(user_team[0].attack_one.move_type.name_list[0]),34,screen)
            edit_screen(user_team[0].attack_two.move_type.name_list,math.ceil((91-len(user_team[0].attack_one.name_list[0])-len(user_team[0].attack_two.name_list[0]))/2)+6+len(user_team[0].attack_one.name_list[0]),34,screen)
            
            attackChoice = button([2,2,2],[len(user_team[0].attack_one.name_list[0])+2,len(user_team[0].attack_two.name_list[0])+2,17],[(91-len(user_team[0].attack_one.name_list[0])-len(user_team[0].attack_two.name_list[0]))//2+2,math.ceil((91-len(user_team[0].attack_one.name_list[0])-len(user_team[0].attack_two.name_list[0]))/2)+5+len(user_team[0].attack_one.name_list[0]),41],[31,31,23],3,[user_team[0].attack_one.name,user_team[0].attack_two.name,"back"],screen)
            
            #goes back to the top of the loop if the user clicks this
            if attackChoice == "back":
                continue
            
            #this voluntary switch is taking up a spot for an attack so the computer still gets to attack, and will do the one with the most damage
            firstMoveDamage = int(comp_team[0].attack_one.base_damage*comp_team[0].attack_one.move_type.multiplier(user_team[0]))
            secondMoveDamage = int(comp_team[0].attack_two.base_damage*comp_team[0].attack_two.move_type.multiplier(user_team[0]))
            
            #checks if first move does more damage then the second and vice versa to pick an attack
            if firstMoveDamage > secondMoveDamage:
                compAttackNum = 0
            else:
                compAttackNum = 1
                
            #attacks the attack choice of the user based on their choice
            if attackChoice == user_team[0].attack_one.name:
                userAttackNum = 0
            elif attackChoice == user_team[0].attack_two.name:
                userAttackNum = 1
            
            randFirstMove = 2
            #checks which pokemon is faster the users or the opponents and determines who goes first
            if user_team[0].speed == comp_team[0].speed:
                randFirstMove = random.randint(0,1)
                
            if user_team[0].speed > comp_team[0].speed or randFirstMove == 0:
                user_team[0].attack(comp_team[0],userAttackNum,beforeAttack_img,True)
                #checks if the pokemon attacked is still alive in if they are they can attack
                if comp_team[0].awake == True:
                    comp_team[0].attack(user_team[0],compAttackNum,beforeAttack_img)
                    
            elif user_team[0].speed < comp_team[0].speed or randFirstMove == 1:
                comp_team[0].attack(user_team[0],compAttackNum,beforeAttack_img)
                #checks if the pokemon attacked is still alive in if they are they can attack
                if user_team[0].awake == True:
                    user_team[0].attack(comp_team[0],userAttackNum,beforeAttack_img,True)
                    
        #checks if the user entered switch and will show the pokemon you can switch to right now
        elif userChoice == "switch":
            #this will copy what the part above the text bubble looked like into a list
            beforeSwitch_img = []
            for i in range(26):
                beforeSwitch_img.append([])
            for i in range(26):
                for j in range(100):
                    beforeSwitch_img[i].append(screen[i][j])
            #28x40
            edit_screen(switch_selection_img,30,6,screen,[])
            
            #the variables used in the button to switch to that pokemon
            switch_heights = []
            switch_widths = []
            switch_x = []
            switch_y = []
            amount = 0
            switch_button_names = []
            
            #will add the text for the buttons on the panel for switching, this includes the pokemon in your team and back button
            for i in range(len(user_team)):
                edit_screen(user_team[i].name_list,30+((40-len(user_team[i].name_list[0]))//2),9+i*4,screen)
                if user_team[i].awake == True and i != 0:
                    switch_heights.append(2)
                    switch_widths.append(len(user_team[i].name_list[0]))
                    switch_x.append(30+((40-len(user_team[i].name_list[0]))//2))
                    switch_y.append(9+i*4)
                    amount = amount + 1
                    switch_button_names.append(user_team[i].name)
                    
            edit_screen(back_img,42,9+4*len(user_team),screen)
            
            switch_heights.append(2)
            switch_widths.append(len(back_img[0]))
            switch_x.append(42)
            switch_y.append(9+4*len(user_team))
            amount = amount + 1
            switch_button_names.append("back")
            
            #will add the viable pokemon to the button as well as back button, meaning the pokemon out or pokemon that have fainted wont be able to be switched to
            switch_choice = button(switch_heights,switch_widths,switch_x,switch_y,amount,switch_button_names,screen)
            
            print_screen(screen)        
            #if the user doesnt want to switch they can go back meaning the while loop will just restart use continue
            if switch_choice == "back":
                continue
            #checks to see what pokemon they want to switch to and make that the fron of the list
            else:
                for i in range(len(user_team)):
                    if user_team[i].name == switch_choice:
                        user_team[i], user_team[0] = user_team[0], user_team[i]
                        val = i
                        break
            
            #this voluntary switch is taking up a spot for an attack so the computer still gets to attack, and will do the one with the most damage
            firstMoveDamage = comp_team[0].attack_one.base_damage*comp_team[0].attack_one.move_type.multiplier(user_team[0])
            secondMoveDamage = comp_team[0].attack_two.base_damage*comp_team[0].attack_two.move_type.multiplier(user_team[0])
            
            firstMoveDamage = int(firstMoveDamage)
            secondMoveDamage = int(secondMoveDamage)
            
            #this part will say the pokemon you switched to 
            edit_screen(beforeSwitch_img,0,0,screen,[])
            edit_screen(fix_img,0,26,screen,[])
            
            edit_screen(you_img,5,28,screen)
            edit_screen(user_team[val].name_list,7+len(you_img[0]),28,screen)
            edit_screen(switched_img, 9 +len(you_img[0])+len(user_team[val].name_list[0]),28,screen)
            edit_screen(to_img,11+len(you_img[0])+len(user_team[val].name_list[0])+len(switched_img[0]),28,screen)
            edit_screen(user_team[0].name_list,5,32,screen)
            
            print_screen(screen)
            time.sleep(2)
            
            #checks if first move does more damage then the second and vice versa to pick an attack
            if firstMoveDamage > secondMoveDamage:
                comp_team[0].attack(user_team[0],0,beforeSwitch_img)
            else:
                comp_team[0].attack(user_team[0],1,beforeSwitch_img)
            
        #checks how many pokemon you have left and the computer, and if any have none then they lose
        win = ""
        userLeft = []
        compLeft = []
        for i in range(len(user_team)):
            userLeft.append(user_team[i].awake)
            compLeft.append(comp_team[i].awake)
        if True not in userLeft:
            win = "notcompleted"
            break
        elif True not in compLeft:
            win = "completed"
            break
        
    
        #if the users pokemon has fainted then they are forced to switch
        if user_team[0].awake == False:
            
            #this will copy what the part above the text bubble looked like into a list
            beforeForcedSwitch_img = []
            for i in range(26):
                beforeForcedSwitch_img.append([])
            for i in range(26):
                for j in range(100):
                    beforeForcedSwitch_img[i].append(screen[i][j])
            
            
            edit_screen(switch_selection_img,30,6,screen,[])
            
            #the variables used in the button to switch to that pokemon
            switch_heights = []
            switch_widths = []
            switch_x = []
            switch_y = []
            amount = 0
            switch_button_names = []
            
            #will add the text for the buttons on the panel for switching, this includes the pokemon in your team and back button
            for i in range(len(user_team)):
                edit_screen(user_team[i].name_list,30+((40-len(user_team[i].name_list[0]))//2),9+i*4,screen)
                if user_team[i].awake == True and i != 0:
                    switch_heights.append(2)
                    switch_widths.append(len(user_team[i].name_list[0]))
                    switch_x.append(30+((40-len(user_team[i].name_list[0]))//2))
                    switch_y.append(9+i*4)
                    amount = amount + 1
                    switch_button_names.append(user_team[i].name)
            
            #will add the viable pokemon to the button as well as back button, meaning the pokemon out or pokemon that have fainted wont be able to be switched to
            switch_choice = button(switch_heights,switch_widths,switch_x,switch_y,amount,switch_button_names,screen)
            
            
            #checks to see what pokemon they want to switch to and make that the fron of the list
            for i in range(len(user_team)):
                if user_team[i].name == switch_choice:
                    user_team[i], user_team[0] = user_team[0], user_team[i]
                    val = i
                    break
            #this part will say the pokemon you switched to 
            edit_screen(beforeForcedSwitch_img,0,0,screen,[])
            edit_screen(fix_img,0,26,screen,[])
            
            edit_screen(you_img,5,28,screen)
            edit_screen(user_team[val].name_list,7+len(you_img[0]),28,screen)
            edit_screen(switched_img, 9 +len(you_img[0])+len(user_team[val].name_list[0]),28,screen)
            edit_screen(to_img,11+len(you_img[0])+len(user_team[val].name_list[0])+len(switched_img[0]),28,screen)
            edit_screen(user_team[0].name_list,5,32,screen)
            
            print_screen(screen)
            time.sleep(2)
            
        #checks to see if the comp pokemon has fainted and will switch it with a random one on its team thats alive.
        if comp_team[0].awake == False:
            #this will copy what the part above the text bubble looked like into a list
            beforeForcedSwitch_img = []
            for i in range(26):
                beforeForcedSwitch_img.append([])
            for i in range(26):
                for j in range(100):
                    beforeForcedSwitch_img[i].append(screen[i][j])
                    
            while True:
                val = random.randint(0,(len(comp_team)-1))
                if comp_team[val].awake == True:
                    comp_team[val], comp_team[0] = comp_team[0], comp_team[val]
                    break
            #this part will say the pokemon you switched to 
            edit_screen(beforeForcedSwitch_img,0,0,screen,[])
            edit_screen(fix_img,0,26,screen,[])
            
            edit_screen(opponent_img,5,28,screen)
            edit_screen(comp_team[val].name_list,7+len(opponent_img[0]),28,screen)
            edit_screen(switched_img, 5,32,screen)
            edit_screen(to_img,7+len(switched_img[0]),32,screen)
            edit_screen(comp_team[0].name_list,9+len(switched_img[0])+len(to_img[0]),32,screen)
            
            print_screen(screen)
            time.sleep(2)


    
    #returns if you won the battle
    return win
    
#a function that lets you select the pokemon you want in your team
#it takes the amount of pokemon per team, and the list with every pokemon in it aswell as the screen
def pokemon_selection_screen(num_team,pokemon_list,screen):
    
    #temp list for the select word to be displayed on the screen
    selectTemp = [[" ██████╗███████╗██╗     ███████╗ █████╗ ████████╗"],
                  ["██╔════╝██╔════╝██║     ██╔════╝██╔══██╗╚══██╔══╝"],
                  ["╚█████╗ █████╗  ██║     █████╗  ██║  ╚═╝   ██║   "],
                  [" ╚═══██╗██╔══╝  ██║     ██╔══╝  ██║  ██╗   ██║   "],
                  ["██████╔╝███████╗███████╗███████╗╚█████╔╝   ██║   "],
                  ["╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚════╝    ╚═╝   "]]
    
    
    #a temporary list for the numbers that will be displaying how many pokemon you can pick 
    
    number1Temp = [["  ███╗  "],
                   [" ████║  "],
                   ["██╔██║  "],
                   ["╚═╝██║  "],
                   ["███████╗"],
                   ["╚══════╝"]]
                   
    number2Temp = [["██████╗ "],
                   ["╚════██╗"],
                   ["  ███╔═╝"],
                   ["██╔══╝  "],
                   ["███████╗"],
                   ["╚══════╝"]]
                   
    number3Temp = [["██████╗ "],
                   ["╚════██╗"],
                   [" █████╔╝"],
                   [" ╚═══██╗"],
                   ["██████╔╝"],
                   ["╚═════╝ "]]
                   
    number4Temp = [["  ██╗██╗"],
                   [" ██╔╝██║"],
                   ["██╔╝░██║"],
                   ["███████║"],
                   ["╚════██║"],
                   ["     ╚═╝"]]
                   
    number5Temp = [["███████╗"],
                   ["██╔════╝"],
                   ["██████╗ "],
                   ["╚════██╗"],
                   ["██████╔╝"],
                   ["╚═════╝ "]]
    

    #will use these lists on the screen
    select_img = text_to_list(selectTemp)
    
    number1_img = text_to_list(number1Temp)
    number2_img = text_to_list(number2Temp)
    number3_img = text_to_list(number3Temp)
    number4_img = text_to_list(number4Temp)
    number5_img = text_to_list(number5Temp)
    
    #list of every number on the screen into a list
    numbers_list = [number1_img, number2_img, number3_img, number4_img, number5_img]
    
    clear_screen(screen)
    
    #for the underline under the number and select
    underline = [[]]
    for i in range(69):
        underline[0].append("━")
    
    edit_screen(select_img,13,7,screen)
    edit_screen(underline,11,13,screen)
    
    #adds the pokemon choices to the screen
    for i in range(5):
        edit_screen(pokemon_list[i].name_list,11,19+i*4,screen)
    for i in range(5):
        edit_screen(pokemon_list[i+5].name_list,55,19+i*4,screen)
    
    #list used to store the pokemon used in the users team
    team = []
    
    #variables used in buttons for the selection screen
    heights = [2,2,2,2,2,2,2,2,2,2]
    widths = [25,31,32,25,21,31,34,29,24,31]
    x = [11,11,11,11,11,55,55,55,55,55]
    y =[19,23,27,31,35,19,23,27,31,35]
    quantity = 10
    button_names = [0,1,2,3,4,5,6,7,8,9]
    
    #this code will get the pokemon they want in their team, there can only be one copy of each pokemon
    for i in range(num_team):
        #puts the number of pokemon that can be selected currently on the screen
        clear_img(6,8,70,7,screen)
        edit_screen(numbers_list[(num_team-1-i)],70,7,screen)
        
        #what pokemon they want to have in their team
        pokemonChoice = button(heights,widths,x,y,quantity,button_names,screen)
        #adds the pokemon they wanted to the team
        team.append(copy.deepcopy(pokemon_list[pokemonChoice]))
        #gets the index because when the values are removed ferom button_names, the indexes will also change meaning if pikachu is removed the new index 0 will be blastoise
        pokemonChoice = button_names.index(pokemonChoice)
        
        #this piece of code will highlight the choice you picked
        highlighted = [[]]
        for i in range((widths[pokemonChoice]+2)):
            highlighted[0].append("━")
        
        edit_screen(highlighted,(x[pokemonChoice]-1),(y[pokemonChoice]+2),screen)
        edit_screen(highlighted,(x[pokemonChoice]-1),(y[pokemonChoice]-1),screen)
        
        print_screen(screen)
        
        #will take out the pokemon that was already picked so you can not have duplicates
        heights.pop(pokemonChoice)
        widths.pop(pokemonChoice)
        x.pop(pokemonChoice)
        y.pop(pokemonChoice)
        quantity = quantity - 1
        button_names.pop(pokemonChoice)

    
    #the team the user wanted
    return team
    
#function to make a level
#it takes the amount of pokemon per team, and the list with every pokemon in it aswell as the screen
def level(num_team,pokemon_list,numbers_list,screen):
    
    #will get the users team as list with the first in the list being the pokemon they open with
    user_team = pokemon_selection_screen(num_team,pokemon_list,screen)
    
    #the computer team will be randomly generated
    comp_team = []
    #runs until the computer has team that has the equal number of pokemon to the user aswell as there being no duplicate pokemon
    while True:
        x = random.randint(0,9)
        #checks if the pokemon number in the list is already in the list
        if x not in comp_team:
            comp_team.append(x)
        #checks if the comp_team has the same the same numb pokemon as the the level and user
        if len(comp_team) == num_team:
            for i in range(num_team):
                comp_team[i] = copy.deepcopy((pokemon_list[(comp_team[i])]))
            break
    
    #does the battle sequence with the teams
    levelOutcome = battle(user_team,comp_team,numbers_list,screen)
    
    clear_screen(screen)
    
    wonTemp = [["██╗   ██╗ █████╗ ██╗   ██╗   ██╗       ██╗ █████╗ ███╗  ██╗"],
               ["╚██╗ ██╔╝██╔══██╗██║   ██║   ██║  ██╗  ██║██╔══██╗████╗ ██║"],
               [" ╚████╔╝ ██║  ██║██║   ██║   ╚██╗████╗██╔╝██║  ██║██╔██╗██║"],
               ["  ╚██╔╝  ██║  ██║██║   ██║    ████╔═████║ ██║  ██║██║╚████║"],
               ["   ██║   ╚█████╔╝╚██████╔╝    ╚██╔╝ ╚██╔╝ ╚█████╔╝██║ ╚███║"],
               ["   ╚═╝    ╚════╝  ╚═════╝      ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚══╝"]]
               
    lostTemp = [["██╗   ██╗ █████╗ ██╗   ██╗  ██╗      █████╗  ██████╗████████╗"],
                ["╚██╗ ██╔╝██╔══██╗██║   ██║  ██║     ██╔══██╗██╔════╝╚══██╔══╝"],
                [" ╚████╔╝ ██║  ██║██║   ██║  ██║     ██║  ██║╚█████╗    ██║   "],
                ["  ╚██╔╝  ██║  ██║██║   ██║  ██║     ██║  ██║ ╚═══██╗   ██║   "],
                ["   ██║   ╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝   ██║   "],
                ["   ╚═╝    ╚════╝  ╚═════╝   ╚══════╝ ╚════╝ ╚═════╝    ╚═╝   "]]
    
    won_img = text_to_list(wonTemp)
    lost_img = text_to_list(lostTemp)
    #checks to see if you won or lost puts the img there depending on the outcome
    if levelOutcome == "completed":
        edit_screen(won_img,20,17,screen)
    elif levelOutcome == "notcompleted":
        edit_screen(lost_img,19,17,screen)
    
    #will print the screen after the person finishs the battle showing that they won or lost
    print_screen(screen)
    time.sleep(3)
    
    #returns if the you won or lost during this level
    return levelOutcome
    
    
#CREATES THE INSTANCES OF EVERY CLASS NECESSARY
################################################################################
####
#these will be used as the names in the battle sequence in the game for the pokemon below
#a temporary list for every pokemon that will be displayed to be picked
#these will be used as the names in the battle sequence in the game for the pokemon below
#a temporary list for every pokemon that will be displayed to be picked
#2x25
pikachuTemp = [["█▀█ █ █▄▀ ▄▀█ █▀▀ █ █ █ █"],
               ["█▀▀ █ █ █ █▀█ █▄▄ █▀█ █▄█"]]
#2x31
blastoiseTemp =[["█▄▄ █   ▄▀█ █▀ ▀█▀ █▀█ █ █▀ █▀▀"],
                ["█▄█ █▄▄ █▀█ ▄█  █  █▄█ █ ▄█ ██▄"]]
#2x32
charizardTemp = [["█▀▀ █ █ ▄▀█ █▀█ █ ▀█ ▄▀█ █▀█ █▀▄"],
                 ["█▄▄ █▀█ █▀█ █▀▄ █ █▄ █▀█ █▀▄ █▄▀"]]
#2x25                      
pidgeotTemp = [["█▀█ █ █▀▄ █▀▀ █▀▀ █▀█ ▀█▀"],
               ["█▀▀ █ █▄▀ █▄█ ██▄ █▄█  █ "]]
#2x21               
golemTemp = [["█▀▀ █▀█ █   █▀▀ █▀▄▀█"],
             ["█▄█ █▄█ █▄▄ ██▄ █ ▀ █"]]
#2x31             
venusaurTemp = [["█ █ █▀▀ █▄ █ █ █ █▀ ▄▀█ █ █ █▀█"],
                ["▀▄▀ ██▄ █ ▀█ █▄█ ▄█ █▀█ █▄█ █▀▄"]]
#2x34               
dragoniteTemp =[["█▀▄ █▀█ ▄▀█ █▀▀ █▀█ █▄ █ █ ▀█▀ █▀▀"],
                ["█▄▀ █▀▄ █▀█ █▄█ █▄█ █ ▀█ █  █  ██▄"]]
#2x29            
mewtwoTemp = [["█▀▄▀█ █▀▀ █ █ █ ▀█▀ █ █ █ █▀█"],
              ["█ ▀ █ ██▄ ▀▄▀▄▀  █  ▀▄▀▄▀ █▄█"]]
#2x24              
steelixTemp = [["█▀ ▀█▀ █▀▀ █▀▀ █   █ ▀▄▀"],
               ["▄█  █  ██▄ ██▄ █▄▄ █ █ █"]]
#2x31               
machampTemp = [["█▀▄▀█ ▄▀█ █▀▀ █ █ ▄▀█ █▀▄▀█ █▀█"],
               ["█ ▀ █ █▀█ █▄▄ █▀█ █▀█ █ ▀ █ █▀▀"]]


pikachu_img = text_to_list(pikachuTemp)
blastoise_img = text_to_list(blastoiseTemp)
charizard_img = text_to_list(charizardTemp)
pidgeot_img = text_to_list(pidgeotTemp)
golem_img = text_to_list(golemTemp)
venusaur_img = text_to_list(venusaurTemp)
dragonite_img = text_to_list(dragoniteTemp)
mewtwo_img = text_to_list(mewtwoTemp)
steelix_img = text_to_list(steelixTemp)
machamp_img = text_to_list(machampTemp)

#temporary list for the names of the moves
thunderboltTemp = [["▀█▀ █ █ █ █ █▄ █ █▀▄ █▀▀ █▀█ █▄▄ █▀█ █   ▀█▀"],
                   [" █  █▀█ █▄█ █ ▀█ █▄▀ ██▄ █▀▄ █▄█ █▄█ █▄▄  █ "]]
                   
shadowballTemp = [["█▀ █ █ ▄▀█ █▀▄ █▀█ █ █ █   █▄▄ ▄▀█ █   █  "],
                  ["▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀   █▄█ █▀█ █▄▄ █▄▄"]]
              
hydropumpTemp = [["█ █ █▄█ █▀▄ █▀█ █▀█   █▀█ █ █ █▀▄▀█ █▀█"],
                 ["█▀█  █  █▄▀ █▀▄ █▄█   █▀▀ █▄█ █ ▀ █ █▀▀"]]
                 
icebeamTemp = [["█ █▀▀ █▀▀   █▄▄ █▀▀ ▄▀█ █▀▄▀█"],
               ["█ █▄▄ ██▄   █▄█ ██▄ █▀█ █ ▀ █"]]
               
flamethrowerTemp = [["█▀▀ █   ▄▀█ █▀▄▀█ █▀▀ ▀█▀ █ █ █▀█ █▀█ █ █ █ █▀▀ █▀█"],
                    ["█▀  █▄▄ █▀█ █ ▀ █ ██▄  █  █▀█ █▀▄ █▄█ ▀▄▀▄▀ ██▄ █▀▄"]]
                    
wingattackTemp = [["█ █ █ █ █▄ █ █▀▀   ▄▀█ ▀█▀ ▀█▀ ▄▀█ █▀▀ █▄▀"],
                  ["▀▄▀▄▀ █ █ ▀█ █▄█   █▀█  █   █  █▀█ █▄▄ █ █"]]
                  
bravebirdTemp = [["█▄▄ █▀█ ▄▀█ █ █ █▀▀ █▄▄ █ █▀█ █▀▄"],
                 ["█▄█ █▀▄ █▀█ ▀▄▀ ██▄ █▄█ █ █▀▄ █▄▀"]]
                 
steelwingTemp = [["█▀ ▀█▀ █▀▀ █▀▀ █     █ █ █ █ █▄ █ █▀▀"],
                 ["▄█  █  ██▄ ██▄ █▄▄   ▀▄▀▄▀ █ █ ▀█ █▄█"]]
                 
rocktombTemp = [["█▀█ █▀█ █▀▀ █▄▀   ▀█▀ █▀█ █▀▄▀█ █▄▄"],
                ["█▀▄ █▄█ █▄▄ █ █    █  █▄█ █ ▀ █ █▄█"]]
                
earthquakeTemp = [["█▀▀ ▄▀█ █▀█ ▀█▀ █ █ █▀█ █ █ ▄▀█ █▄▀ █▀▀"],
                  ["██▄ █▀█ █▀▄  █  █▀█ ▀▀█ █▄█ █▀█ █ █ ██▄"]]
                  
vinewipTemp = [["█ █ █ █▄ █ █▀▀   █ █ █ █ █▀█"],
               ["▀▄▀ █ █ ▀█ ██▄   ▀▄▀▄▀ █ █▀▀"]]
               
sludgebombTemp = [["█▀ █   █ █ █▀▄ █▀▀ █▀▀   █▄▄ █▀█ █▀▄▀█ █▄▄"],
                  ["▄█ █▄▄ █▄█ █▄▀ █▄█ ██▄   █▄█ █▄█ █ ▀ █ █▄█"]]
                  
dragonrushTemp = [["█▀▄ █▀█ ▄▀█ █▀▀ █▀█ █▄ █   █▀█ █ █ █▀ █ █"],
                  ["█▄▀ █▀▄ █▀█ █▄█ █▄█ █ ▀█   █▀▄ █▄█ ▄█ █▀█"]]
                  
firefangTemp = [["█▀▀ █ █▀█ █▀▀   █▀▀ ▄▀█ █▄ █ █▀▀"],
                ["█▀  █ █▀▄ ██▄   █▀  █▀█ █ ▀█ █▄█"]]
                
psychicTemp = [["█▀█ █▀ █▄█ █▀▀ █ █ █ █▀▀"],
               ["█▀▀ ▄█  █  █▄▄ █▀█ █ █▄▄"]]
               
energyballTemp = [["█▀▀ █▄ █ █▀▀ █▀█ █▀▀ █▄█   █▄▄ ▄▀█ █   █  "],
                  ["██▄ █ ▀█ ██▄ █▀▄ █▄█  █    █▄█ █▀█ █▄▄ █▄▄"]]
                  
irontailTemp = [["█ █▀█ █▀█ █▄ █   ▀█▀ ▄▀█ █ █  "],
                ["█ █▀▄ █▄█ █ ▀█    █  █▀█ █ █▄▄"]]
                  
crunchTemp = [["█▀▀ █▀█ █ █ █▄ █ █▀▀ █ █"],
              ["█▄▄ █▀▄ █▄█ █ ▀█ █▄▄ █▀█"]]
                  
crosschopTemp = [["█▀▀ █▀█ █▀█ █▀ █▀   █▀▀ █ █ █▀█ █▀█"],
                 ["█▄▄ █▀▄ █▄█ ▄█ ▄█   █▄▄ █▀█ █▄█ █▀▀"]]
                  
dualchopTemp = [["█▀▄ █ █ ▄▀█ █     █▀▀ █ █ █▀█ █▀█"],
                ["█▄▀ █▄█ █▀█ █▄▄   █▄▄ █▀█ █▄█ █▀▀"]]

#the moves as list to be displayed
thunderbolt_img = text_to_list(thunderboltTemp)
shadowball_img = text_to_list(shadowballTemp)
hydropump_img = text_to_list(hydropumpTemp)
icebeam_img = text_to_list(icebeamTemp)
flamethrower_img = text_to_list(flamethrowerTemp)
wingattack_img = text_to_list(wingattackTemp)
bravebird_img = text_to_list(bravebirdTemp)
steelwing_img = text_to_list(steelwingTemp)
rocktomb_img = text_to_list(rocktombTemp)
earthquake_img = text_to_list(earthquakeTemp)
vinewip_img = text_to_list(vinewipTemp)
sludgebomb_img = text_to_list(sludgebombTemp)
dragonrush_img = text_to_list(dragonrushTemp)
firefang_img = text_to_list(firefangTemp)
psychic_img = text_to_list(psychicTemp)
energyball_img = text_to_list(energyballTemp)
irontail_img = text_to_list(irontailTemp)
crunch_img = text_to_list(crunchTemp)
crosschop_img = text_to_list(crosschopTemp)
dualchop_img = text_to_list(dualchopTemp)

#temporary lists for the types to be used to displayed on the screen

electricTemp = [["█▀▀ █   █▀▀ █▀▀ ▀█▀ █▀█ █ █▀▀"],
                ["██▄ █▄▄ ██▄ █▄▄  █  █▀▄ █ █▄▄"]]
              
waterTemp = [["█ █ █ ▄▀█ ▀█▀ █▀▀ █▀█"],
             ["▀▄▀▄▀ █▀█  █  ██▄ █▀▄"]]
           
fireTemp = [["█▀▀ █ █▀█ █▀▀"],
            ["█▀  █ █▀▄ ██▄"]]
          
grassTemp = [["█▀▀ █▀█ ▄▀█ █▀ █▀"],
             ["█▄█ █▀▄ █▀█ ▄█ ▄█"]]
           
fightingTemp = [["█▀▀ █ █▀▀ █ █ ▀█▀ █ █▄ █ █▀▀"],
                ["█▀  █ █▄█ █▀█  █  █ █ ▀█ █▄█"]]
              
psychicTemp = [["█▀█ █▀ █▄█ █▀▀ █ █ █ █▀▀"],
               ["█▀▀ ▄█  █  █▄▄ █▀█ █ █▄▄"]]
             
steelTemp = [["█▀ ▀█▀ █▀▀ █▀▀ █  "],
             ["▄█  █  ██▄ ██▄ █▄▄"]]
           
rockTemp = [["█▀█ █▀█ █▀▀ █▄▀"],
            ["█▀▄ █▄█ █▄▄ █ █"]]
          
flyingTemp = [["█▀▀ █   █▄█ █ █▄ █ █▀▀"],
              ["█▀  █▄▄  █  █ █ ▀█ █▄█"]]
            
dragonTemp = [["█▀▄ █▀█ ▄▀█ █▀▀ █▀█ █▄ █"],
              ["█▄▀ █▀▄ █▀█ █▄█ █▄█ █ ▀█"]]
            
darkTemp = [["█▀▄ ▄▀█ █▀█ █▄▀"],
            ["█▄▀ █▀█ █▀▄ █ █"]]
          
groundTemp = [["█▀▀ █▀█ █▀█ █ █ █▄ █ █▀▄"],
              ["█▄█ █▀▄ █▄█ █▄█ █ ▀█ █▄▀"]]
            
poisonTemp = [["█▀█ █▀█ █ █▀ █▀█ █▄ █"],
              ["█▀▀ █▄█ █ ▄█ █▄█ █ ▀█"]]
            
iceTemp = [["█ █▀▀ █▀▀"],
           ["█ █▄▄ ██▄"]]
         
ghostTemp = [["█▀▀ █ █ █▀█ █▀ ▀█▀"],
             ["█▄█ █▀█ █▄█ ▄█  █ "]]
           
nullTemp = [["█▄ █ █ █ █   █  "],
            ["█ ▀█ █▄█ █▄▄ █▄▄"]]

#lists for every type of pokemon         
electric_img = text_to_list(electricTemp)
water_img = text_to_list(waterTemp)
fire_img = text_to_list(fireTemp)
grass_img = text_to_list(grassTemp)
fighting_img = text_to_list(fightingTemp)
psychic_img = text_to_list(psychicTemp)
steel_img = text_to_list(steelTemp)
rock_img = text_to_list(rockTemp)
flying_img = text_to_list(flyingTemp)
dragon_img = text_to_list(dragonTemp)
dark_img = text_to_list(darkTemp) 
ground_img = text_to_list(groundTemp) 
poison_img = text_to_list(poisonTemp) 
ice_img = text_to_list(iceTemp) 
ghost_img = text_to_list(ghostTemp)
null_img = text_to_list(nullTemp)


#a temporary list for the numbers that will be displaying on the screen
number1Temp = [["▄█ "],
               [" █ "],
               ["▄█▄"]]
               
number2Temp = [["█▀█"],
               [" ▄▀"],
               ["█▄▄"]]
               
number3Temp = [["█▀▀█"],
               ["  ▀▄"],
               ["█▄▄█"]]
               
number4Temp = [[" █▀█"],
               ["█▄▄█"],
               ["   █"]]
               
number5Temp = [["█▀▀"],
               ["▀▀▄"],
               ["▄▄▀"]]
               
number6Temp = [["▄▀▀▄"],
               ["█▄▄ "],
               ["▀▄▄▀"]]
               
number7Temp = [["▀▀▀█"],
               ["  █ "],
               [" ▐▌ "]]
               
number8Temp = [["▄▀▀▄"],
               ["▄▀▀▄"],
               ["▀▄▄▀"]]
               
number9Temp = [["▄▀▀▄"],
               ["▀▄▄█"],
               [" ▄▄▀"]]
               
number0Temp = [["█▀▀█"],
               ["█▄▀█"],
               ["█▄▄█"]]

number1_img = text_to_list(number1Temp)
number2_img = text_to_list(number2Temp)
number3_img = text_to_list(number3Temp)
number4_img = text_to_list(number4Temp)
number5_img = text_to_list(number5Temp)
number6_img = text_to_list(number6Temp)
number7_img = text_to_list(number7Temp)
number8_img = text_to_list(number8Temp)
number9_img = text_to_list(number9Temp)
number0_img = text_to_list(number0Temp)

num_list = [number0_img,number1_img, number2_img, number3_img, number4_img, number5_img, number6_img, number7_img, number8_img, number9_img]

####

#Defines Types
electric = Type("Electric",electric_img)
water = Type("Water",water_img)
fire = Type("Fire",fire_img)
grass = Type("Grass",grass_img)
fighting = Type("Fighting",fighting_img)
psychic = Type("Psychic",psychic_img)
steel = Type("Steel",steel_img)
rock = Type("Rock",rock_img)
flying = Type("Flying",flying_img)
dragon = Type("Dragon",dragon_img)
dark = Type("Dark",dark_img)
ground = Type("Ground",ground_img)
poison  = Type("Poison",poison_img)
ice = Type("Ice",ice_img)
ghost = Type("Ghost",ghost_img)
#type used for pokemon with one type
null = Type("null",null_img)

#Defines the moves of Each Pokemon
thunderbolt = Move("Thunderbolt", electric, 20,thunderbolt_img)
shadowball = Move("Shadow Ball", ghost, 15,shadowball_img) 
hydropump = Move("Hydro Pump", water,20,hydropump_img)
icebeam = Move("Ice Beam", ice, 15,icebeam_img)
flamethrower = Move("Flamethrower", fire,20,flamethrower_img)
wingattack = Move("Wing Attack", flying,15,wingattack_img)
bravebird = Move("Bravebird",flying, 20,bravebird_img)
steelwing = Move("Steel Wing", steel, 15,steelwing_img)
rocktomb = Move("Rock Tomb", rock, 20,rocktomb_img)
earthquake = Move("Earthquake", ground, 15,earthquake_img)
vinewip = Move("Vine Wip", grass,20,vinewip_img)
sludgebomb = Move("Sludge Bomb", poison, 15,sludgebomb_img)
dragonrush = Move("Dragon Rush", dragon, 20,dragonrush_img)
firefang = Move("Fire Fang", fire,15,firefang_img)
psychic = Move("Psychic", psychic, 20,psychic_img)
energyball = Move("Energy Ball", grass, 15,energyball_img)
irontail = Move("Iron Tail", steel, 20,irontail_img)
crunch = Move("Crunch", dark, 15,crunch_img)
crosschop = Move("Cross Chop", fighting, 20,crosschop_img)
dualchop = Move("Dual Chop", dragon, 15,dualchop_img)

#Defines every Pokemon
#pokemon with the the pokemon type null as there second only has one type
pikachu = Pokemon([thunderbolt,shadowball],60,10,electric,null,"Pikachu",True,pikachu_img)
blastoise = Pokemon([hydropump,icebeam],100,4,water,null,"Blastoise",True,blastoise_img)
charizard = Pokemon([flamethrower,wingattack],80,6,fire,flying,"Charizard",True,charizard_img)
pidgeot = Pokemon([bravebird,steelwing],70,8,flying,null,"Pidgeot",True,pidgeot_img)
golem  = Pokemon([rocktomb,earthquake],120,1,rock,ground,"Golem",True,golem_img)
venusaur = Pokemon([vinewip,sludgebomb],100,2,grass,poison,"Venusaur",True,venusaur_img)
dragonite = Pokemon([dragonrush,firefang],90,5,dragon,flying,"Dragonite",True,dragonite_img)
mewtwo  = Pokemon([psychic,energyball],80,9,psychic,null,"Mewtwo",True,mewtwo_img)
steelix = Pokemon([irontail,crunch],110,3,steel,ground,"Steelix",True,steelix_img)
machamp = Pokemon([crosschop,dualchop],90,7,fighting,null,"Machamp",True,machamp_img)

################################################################################




#the list used to keep track of what levels you have completed and ones you have unlocked
level_screen_record = [["unlocked","locked","locked","locked","locked"],["notcompleted","notcompleted","notcompleted","notcompleted","notcompleted",]]

#the list with every pokemon in it in the order they were defined
pokemon_list = [pikachu, blastoise, charizard, pidgeot, golem, venusaur, dragonite, mewtwo, steelix, machamp]

#this variable is to put the way to use the keys, but only the first time u run through the while loop
firstTime = True

#will continue the game until you beat the game
while True:
    #creates the title screen
    title_screen(screen)
    
    #prints the title screen
    print_screen(screen)
    
    #shows the contorls for how to use the game, but only the first time the while loop iterates
    if firstTime == True:
        firstTime = False
        
        print("\u001b[31;1mUse 'w'/'s' Or 'a'/'d' To Move The Buttons, And 'q' To Select\u001b[0m")
        print("\u001b[31;1mMake Sure To Click 'Enter' After Each Input\u001b[0m")
        
        time.sleep(3)

    
    #a delay before putting the button on the screen
    time.sleep(0.5)
    
    #sees what the users choice is from the two options on the screen during the title screen
    title_choice = button([6,6],[42,37],[10,10],[22,30],2,["start","guide"],screen)
    
    #depending on the users choices the player will be put onto different screens, either the level selection when start is clicked or the guide to the game
    if title_choice == "start":
        #puts the levels screen on the screen list variable
        levels_screen(screen,level_screen_record)
        #prints the new screen
        print_screen(screen)
        
        #the while loop runs until a choice that is viable is chosen by the user
        while True:
            #gets the choice from the user for what level they want to pick
            level_choice = button([6,6,6,6,6],[51,51,51,51,51],[25,25,25,25,25],[3,10,17,24,31],5,[1 ,2, 3, 4, 5],screen)
            
            #checks if the level is unlocked and not completed
            if level_screen_record[0][level_choice-1] == "unlocked" and level_screen_record[1][level_choice-1] == "notcompleted":
                break
            
        #will play the level played and goes through all 5 possibiilites, meaning all 5 levels
        for i in range(5):
            if level_choice == (i+1) and level_screen_record[0][i] == "unlocked" and level_screen_record[1][i] == "notcompleted":
                #will let the player play the level selected and see if they win
                levelOutcome = level(level_choice,pokemon_list,num_list,screen)
        #checks if the level is completed and if the level they beat was not level 5 and updates the levels beaten aswell as the levels locked
        if levelOutcome == "completed" and level_choice != 5:
            level_screen_record[0][level_choice] = "unlocked"
            level_screen_record[1][level_choice - 1] = "completed"
        elif levelOutcome == "completed" and level_choice == 5:
            level_screen_record[1][level_choice - 1] = "completed"
        #will show a screen saying congratulations thank you for playing
        if "notcompleted" not in level_screen_record[1]:
            end_screen(screen)
            break
        
    elif title_choice == "guide":
        guide_screen(screen)