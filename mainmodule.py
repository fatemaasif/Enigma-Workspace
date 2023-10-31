
# importing pygame and relevant modules 
import pygame
from pygame import display, image, font, mouse, draw, rect

import assisting_dictionaries
from assisting_dictionaries import*

# initializing pygame 
pygame.init()

# global helper variables that will stay consistent throughout the program
# initializing pygame and setting up GUI console
screen_width = 818
screen_height = 694
EnigmaDisplay = display.set_mode((screen_width, screen_height))
display.set_caption('Wehrmacht Enigma I: A Simulation Project by Fatema Asif (MTS 41 B)') 
console_icon = image.load('console icon.png')
display.set_icon(console_icon)

white = (255,255,255)
black =(0,0,0)

rotor_permutations = {}
#creating the main menu and the simulation loops
#--------------------------------------------------------------------
#this will be the first screen seen that has several options you can choose from
def main_menu():
    mainmenu_open = True
    while mainmenu_open:

        #setting the graphics for the screen
        EnigmaDisplay.fill(black)
        background_img =  image.load('Enigma.png')
        EnigmaDisplay.blit(background_img,(0, 0))

        titletext_centerx = int(screen_width/2)
        titletext_centery = int(screen_height*0.2)
        titletext = get_text("THE ENIGMA I", 40, True , white, (titletext_centerx, titletext_centery), 'EnigmaSans.ttf')
        titletext_centery+=45
        titletext = get_text("A PYTHON SIMULATION", 40, True , white, (titletext_centerx, titletext_centery), 'EnigmaSans.ttf')
        credittxt = get_text("A Project by Fatema Asif", 30, False, white, (int(screen_width*0.7),int(screen_height*0.95)), 'EnigmaSans.ttf')
        
        #reference rectangle coordinates for the button
        rect = pygame.Rect(int(screen_width/2), int(screen_height*0.4), 350, 50)
        rect.centerx = titletext.centerx #align the center x position of the title text and buttons

        txtsize = 30
        #option 1
        open_simulator_button = makebutton(rect, "Start Simulater", txtsize, 'EnigmaSans.ttf')
        #adds some units to the y position of the rect for more buttons
        rect.y += 100  
        #option 2
        information_button = makebutton(rect, "Information centre", txtsize, 'EnigmaSans.ttf')
        mousepos = mouse.get_pos()
        
        #responding to events in the main menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainmenu_open = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 1: #checked if mouse button is clicked and left button is clicked
                     if open_simulator_button.collidepoint(mousepos):
                         opensettings()
                     if information_button.collidepoint(mousepos):
                         informationcentre()
            
        display.flip()

#clicking on option 1 - set rotor settings-----------------------------------------
def opensettings():

    # initiating the rotor settings buttons

    w_rot = 45
    h_rot = 45
    ypos = 200
    rotortype_sr = 0
    rotortype_mr = 1
    rotortype_fr = 2
    s_xpos = 42
    srotor_rect = pygame.Rect(s_xpos, ypos, w_rot, h_rot)
    m_xpos = s_xpos + 140
    mrotor_rect = pygame.Rect(m_xpos, ypos, w_rot, h_rot)
    f_xpos = m_xpos + 140 
    frotor_rect = pygame.Rect(f_xpos, ypos, w_rot, h_rot)

    #initializing the list to be used to store the plugboard letters that have been joined
    plugrect_list = []
    plug_list = []
    draw_plug_bool = False

    settings_open = True
    while settings_open:
        #setting up the interface
        EnigmaDisplay.fill(black)
        titletext_centerx = int(screen_width/2)
        titletext_centery = int(screen_height*0.08)
        titletext = get_text("Welcome to the simulator!", 30, True , white, (titletext_centerx, titletext_centery), 'EnigmaSans.ttf')
        titletext_centery+=30
        titletext = get_text("Choose your settings to proceed", 30, True , white, (titletext_centerx, titletext_centery), 'EnigmaSans.ttf')
        
        back = get_text("Back", 15, True, white, (777,18))

        #loading images for the settings interface
        steckerbrett_img = image.load('m1_steckerbrett.png')
        EnigmaDisplay.blit(steckerbrett_img,(0, int(screen_height*0.5)))

        # draw the rotor settings buttons on the interface
        slowrotor_setting = rotors((s_xpos, ypos), rotortype_sr, white, False)
        get_text("Rotor 1", 20, True, white, (srotor_rect.centerx, ypos-30), 'EnigmaSans.ttf')
        mediumrotor_setting = rotors((m_xpos, ypos), rotortype_mr, white, False)
        get_text("Rotor 2", 20, True, white, (mrotor_rect.centerx, ypos-30), 'EnigmaSans.ttf')
        fastrotor_setting = rotors((f_xpos, ypos), rotortype_fr,white,False)
        get_text("Rotor 3", 20, True, white, (frotor_rect.centerx, ypos-30), 'EnigmaSans.ttf')

         # make buttons to direct to the simulations 
        button_x = 464
        button_y = 145
        button1 = makebutton((button_x, button_y, 350, 50), 'Get the Enigma Experiece', 20, 'EnigmaSans.ttf')
        button2 = makebutton((button_x, button_y+70, 350, 50), 'Encode Text', 20, 'EnigmaSans.ttf')

        #pass rotor settings
        getdictaccordingtosettings(rotortype_sr, rotortype_mr, rotortype_fr)
       
        #draw the existing plugs and an additional one upon each click
        if draw_plug_bool:
            drawplug(plugrect_list,plug_list,0)

        mouse_position = mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_open = False
                quit()
            #on left key press, within the bounds of the rotor buttons, give the rotortype for each rotor position
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back.collidepoint(mouse_position):
                        settings_open = False
                    # rotor handling
                    if srotor_rect.collidepoint(mouse_position): 
                            rotortype_sr += 1
                    if mrotor_rect.collidepoint(mouse_position):
                            rotortype_mr += 1
                    if frotor_rect.collidepoint(mouse_position):
                            rotortype_fr += 1

                    #plug handling
                    for plug, plugrect in steckerbrettdict.items():
                        if plugrect.collidepoint(mouse_position):
                            plugrect_list.append(plugrect)
                            plug_list.append(plug)
                            draw_plug_bool = True

                    #button direction handling
                    if button1.collidepoint(mouse_position):
                        simulation(plug_list)
                    if button2.collidepoint(mouse_position):
                        stringsimulation(plug_list)
         #the letternumbs should be between 0 and 5 to get one of the five rotors - these will be used to determine the rotors to be used in the simulation
        if rotortype_fr == 5:
            rotortype_fr = 0
        if rotortype_mr == 5:
            rotortype_mr = 0
        if rotortype_sr == 5:
            rotortype_sr = 0

        display.flip()

#the enigma simulation in gui, option 1a--------------------------------------------
def simulation(pluglist):
    
    #rotor size
    w_rot = 24
    h_rot = 26

    #the letters that will be shown on the rotor
    global letterindex_sr
    global letterindex_mr
    global letterindex_fr
    letterindex_sr = 0
    letterindex_mr = 0
    letterindex_fr = 0

    #rotor rects to check for mouse collission 
    srotor_rect = pygame.Rect(233, 83, w_rot, h_rot)
    mrotor_rect = pygame.Rect(318, 83, w_rot, h_rot)
    frotor_rect = pygame.Rect(401, 83, w_rot, h_rot)

    #get the default rotor settings on what rotor is to be used for the encryption
    if len(rotor_permutations) == 0:
        getdictaccordingtosettings(0,1,2)

    #setting up sounds for the simulation
    typingsound = pygame.mixer.Sound("key sound.wav") 

    #get the pluglist and break it down into seperate lists of two
    user_pluglist = breaklist(pluglist)
    letterexcchanged = False

    simulation_open = True
    while simulation_open:
        
        # setting up graphics for the simulation
        enigma_background = image.load('EnigmaTopView.png')
        EnigmaDisplay.blit(enigma_background, (0,0))
        back = get_text("Back", 15, True, white, (777,18))
        mouse_position = mouse.get_pos()

        # drawing the keys for the keyboards and putting them in a dictionary for efficient use in function later 
        letterkeys = {}
        for k, v in letterkeydict.items():
            lk = drawletterkey(k,v)
            letterkeys.update({k : lk})

        # draws font on the created letter keys 
        for letter, key in letterkeys.items():
            fontonletterkey(letter,key.center,(204,204,204))

        # draw the lamps
        for letter, center in lampdict.items():
            lamp(letter,center)

        # draw rotors
        fastrotor = rotors((401, 83), letterindex_fr)            
        slowrotor = rotors((233, 83), letterindex_sr) 
        mediumrotor = rotors((318, 83), letterindex_mr)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simulation_open = False
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if back.collidepoint(mouse_position):
                        simulation_open = False
                    for letter, key in letterkeys.items():
                        #get events and upon mouse press on the letter keys of the keyboard, change font of letter, turn the lamp on and rotate the rotors
                        if key.collidepoint(mouse_position):
                            #sound played
                            pygame.mixer.Sound.play(typingsound)
                            #font changed to red
                            fontonletterkey(letter,key.center,(204,51,51))
                            #check if the letter is in the plugboard settings and exchange it with the letter against it
                            print(letter, ":", end = '')
                            if len(user_pluglist) > 0:
                                for lists in user_pluglist:
                                    if letter in lists:
                                        letter = exchange(lists, letter)
                            #lamp lights up
                            encryptedletter = on_encryptionpathway(letter)
                            # the encrypted letter needs to be exchanged with its counterpart again so that the right letter shows during decoding
                            for lists in user_pluglist:
                                if encryptedletter in lists:
                                    encryptedletter = exchange(lists, encryptedletter)
                            for letter, center in lampdict.items():
                                if letter == encryptedletter:
                                    lamp(encryptedletter, center, True)
                            print(" ",encryptedletter)
                            letterindex_fr += 1
                    #if rotors are clicked, rotate them - this is to set initial position of rotors
                    if srotor_rect.collidepoint(mouse_position):
                        letterindex_sr += 1
                    if mrotor_rect.collidepoint(mouse_position):
                        letterindex_mr += 1
                    if frotor_rect.collidepoint(mouse_position):
                        letterindex_fr += 1
                    

        #the rotor index is in integers so we need to wrap them around so that a rotate after Z points to an a
        if letterindex_fr == 26:
            letterindex_fr = 0
            fr_rotationcomplete = True
            if fr_rotationcomplete == True:
                letterindex_mr += 1
                fr_rotationcomplete = False
        if letterindex_mr == 26:
            letterindex_mr = 0
            mr_rotationcomplete = True
            if mr_rotationcomplete == True:
                letterindex_sr += 1
                mr_rotationcomplete = False
        if letterindex_sr == 26:
            letterindex_sr = 0
                            
                            
        display.flip()
        
# string encoding clicking on option 1b-------------------------------------------
def stringsimulation(pluglist):

    # copying the settings from the simulation function
    #rotor size
    w_rot = 24
    h_rot = 26
    #the letters that will be shown on the rotor
    global letterindex_sr
    global letterindex_mr
    global letterindex_fr
    letterindex_sr = 0
    letterindex_mr = 0
    letterindex_fr = 0
    #rotor rects to check for mouse collission 
    srotor_rect = pygame.Rect(233, 83, w_rot, h_rot)
    mrotor_rect = pygame.Rect(318, 83, w_rot, h_rot)
    frotor_rect = pygame.Rect(401, 83, w_rot, h_rot)
    #get the default rotor settings on what rotor is to be used for the encryption
    if len(rotor_permutations) == 0:
        getdictaccordingtosettings(0,1,2)
    #get the pluglist and break it down into seperate lists of two
    user_pluglist = breaklist(pluglist)

    inputtext = ""
    #the output string
    decodedtext = []

    stringencoder = True
    while stringencoder:
        
        # Graphical setup for console
        enigma_background = image.load('EnigmaTopView.png')
        EnigmaDisplay.blit(enigma_background, (0,0))
        back = get_text("Back", 15, True, white, (777,18))

         # draw the lamps
        for letter, center in lampdict.items():
            lamp(letter,center)
        # draw rotors
        fastrotor = rotors((401, 83), letterindex_fr)            
        slowrotor = rotors((233, 83), letterindex_sr) 
        mediumrotor = rotors((318, 83), letterindex_mr)

        inputtextrect = draw.rect(EnigmaDisplay, (211,211,211), ((10, 444), (798, 230)))

        textrect_active = False

        mouse_position = mouse.get_pos()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stringencoder = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back.collidepoint(mouse_position):
                        stringencoder = False
                    if srotor_rect.collidepoint(mouse_position):
                        letterindex_sr += 1
                    if mrotor_rect.collidepoint(mouse_position):
                        letterindex_mr += 1
                    if frotor_rect.collidepoint(mouse_position):
                        letterindex_fr += 1
                    if inputtextrect.collidepoint(mouse_position):
                        textrect_active = True
            if event.type == pygame.KEYDOWN:
                #if textrect_active:
                if event.key == pygame.K_RETURN:
                    if all(x.isalpha() or x.isspace() for x in inputtext) is False:
                        inputtext = ''
                    for letter in inputtext:
                        if letter != ' ':
                            if len(user_pluglist) > 0:
                                for lists in user_pluglist:
                                    if letter in lists:
                                        letter = exchange(lists, letter)
                            encryptedletter = on_encryptionpathway(letter)
                            for lists in user_pluglist:
                                if encryptedletter in lists:
                                    encryptedletter = exchange(lists, encryptedletter)
                            for letter, center in lampdict.items():
                                if letter == encryptedletter:
                                    lamp(encryptedletter, center, True)
                            decodedtext.append(encryptedletter)
                            letterindex_fr += 1
                        else:
                            decodedtext.append(' ')
                    inputtext = ''
                    
                elif event.key == pygame.K_BACKSPACE:
                    inputtext = inputtext[:-1]
                else:
                    inputtext += event.unicode
        inputtext = inputtext.upper()
        # prints the input text on the console in the grey box
        get_text(inputtext, 25, False, black, inputtextrect.center)
        # prints the output text on the console in the grey box
        outputtext = ' '.join(decodedtext)
        get_text(outputtext, 25, False, black, (inputtextrect.centerx, inputtextrect.centery+20))

        get_text("Click on text window to clear screen", 15, False, black, (inputtextrect.centerx, inputtextrect.y+20))
        if textrect_active is True:
            decodedtext = []

        if letterindex_fr == 26:
            letterindex_fr = 0
            fr_rotationcomplete = True
            if fr_rotationcomplete == True:
                letterindex_mr += 1
                fr_rotationcomplete = False
        if letterindex_mr == 26:
            letterindex_mr = 0
            mr_rotationcomplete = True
            if mr_rotationcomplete == True:
                letterindex_sr += 1
                mr_rotationcomplete = False
        if letterindex_sr == 26:
            letterindex_sr = 0
        
        display.flip()
    



#clicking on option 2------------------------------------------------------------
def informationcentre():
    informationcentre_open = True
    while informationcentre_open:
        EnigmaDisplay.fill(black)
        back = get_text("Back", 15, True, white, (777,18))

        ypos = 50
        string = "Enigma I (Roman '1') is an electromechanical cipher machine developed in 1927/29 by Chriffrier­maschinen AG in Berlin (Germany) for the German Army (Wehrmacht). The machine was used throughout WWII to carry coded military communications by ciphering and deciphering each letter of the alphabet. This project aims to simulate the workings of the machine using Python as the coding language. This project is for entertainment (and an A in FoP) purposes only and I do not take any liability for its misuse."
        startofstring = 0
        endofstring = 59
        for x in range(len(string)):
            intro = get_text(string[startofstring:endofstring],20, True, white, (int(screen_width/2),ypos),'EnigmaSans.ttf')
            ypos += 40
            startofstring = endofstring
            endofstring += 59
            x += 59
        ypos = 426
        get_text("Instructions on using the simulations:", 24,True, white, (intro.centerx,ypos),'EnigmaSans.ttf')
        ypos += 40
        startofstring = 0
        endofstring = 59
        string = "1. The rotor and plugboard settings are set to default. You may set them to what you want"
        for x in range(len(string)):
            intro = get_text(string[startofstring:endofstring],15,True, white, (int(screen_width/2),ypos),'EnigmaSans.ttf')
            ypos += 25
            startofstring = endofstring
            endofstring += 59
            x += 59
        ypos = 517
        startofstring = 0
        endofstring = 59
        string = "2. Thereafter, try out the Enigma simulation or to encode an entire script, click on the second option: Encode text"
        for x in range(len(string)):
            intro = get_text(string[startofstring:endofstring],15, True, white, (int(screen_width/2),ypos),'EnigmaSans.ttf')
            ypos += 25
            startofstring = endofstring
            endofstring += 59
            x += 59
        ypos = 577
        startofstring = 0
        endofstring = 59
        string = "3. The Encode text option will not allow for encoding of numbers. Press 'Enter' to code or decode your letters. Press 'Backspace' key to delete"
        for x in range(len(string)):
            intro = get_text(string[startofstring:endofstring],15, True, white, (int(screen_width/2),ypos),'EnigmaSans.ttf')
            ypos += 25
            startofstring = endofstring
            endofstring += 59
            x += 59
        ypos = 657
        get_text("4. Enjoy!",15, True, white, (int(screen_width/2),ypos),'EnigmaSans.ttf')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                informationcentre_open = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back.collidepoint(mouse.get_pos()):
                        informationcentre_open = False

        display.flip()

#Helper functions-------------------------------------------------

#writes the font on the surface
def get_text(text, txtsize, bold, fontclr, textcenterpos, fonttype = 'HelveticaNeueBold.ttf'):
    fontobj = font.Font(fonttype, txtsize)
    letter_surface = fontobj.render(text, bold, fontclr)
    getrectcoord_lettersurface = letter_surface.get_rect()
    getrectcoord_lettersurface.center = textcenterpos
    EnigmaDisplay.blit(letter_surface, getrectcoord_lettersurface)
    return getrectcoord_lettersurface

#creates a button that animates upon mouse hovering
def makebutton(rect, text, txtsize, txttype = 'HelveticaNeueBold.ttf'):
    buttonrect = pygame.draw.rect(EnigmaDisplay, (102, 102, 102), rect)
    txtclr = (204, 204, 204)
    buttonsound = pygame.mixer.Sound("key sound.wav") 
    
    #check if mouse hovers over button, enlarge the text for animation
    if buttonrect.collidepoint(mouse.get_pos()):
        textonbutton = get_text(text, txtsize + 3, True, txtclr, buttonrect.center, txttype)
        pygame.mixer.Sound.play(buttonsound)
        pygame.time.wait(20)
        pygame.mixer.Sound.stop(buttonsound)
        pygame.time.wait(100)
    else:
        textonbutton = get_text(text, txtsize, True, txtclr, buttonrect.center, txttype)

    return buttonrect

#creates a round letterkey
def drawletterkey(letter, center):
    circle_rad = 20
    fontclr = (204, 51, 51)
    textsize = 28
    get_text(letter, textsize, True, fontclr, center)
    return pygame.draw.circle(EnigmaDisplay, (102, 102, 102), center, circle_rad)

#function to manipulate font on the letterkey when it is clicked and when it isnt
def fontonletterkey(letter, center, fontclr = (204, 204, 204)):
    drawletterkey(letter, center)
    textsize = 28
    get_text(letter, textsize, True, fontclr, center)

#create a lamp graphical object
def lamp(letter, center, lightup = False):
    #add functionality for when lightup = True
    circle_rad = 23
    lampclr = black
    txtsize = 24
    fontclr = (102, 102, 102)
    pygame.draw.circle(EnigmaDisplay, lampclr, center, circle_rad, 1)
    if lightup == True:
        pygame.draw.circle(EnigmaDisplay, (255, 255, 153), center, circle_rad)
    get_text(letter, txtsize, True, fontclr, center)

#create the rotors to be used both in simulation and settings page 
def rotors(position, letternumb, rotor_bgclr = (187, 170, 119), letters = True):
    rotor_txtclr = black
    if letters == True:
        rotor_txtsize = 24
        width = 24
        height = 26
        movable_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        rotor_txtsize = 35
        width = 45
        height = 45
        movable_letters = ['I','II','III','IV','V']
    rotor_rect = pygame.draw.rect(EnigmaDisplay, rotor_bgclr, (position, (width, height)))
    letteronrotor = movable_letters[letternumb]
    get_text(letteronrotor, rotor_txtsize, False, rotor_txtclr, rotor_rect.center)

#function to convert the values of the dictionary to a list
def dictvalues_tolist(dict):
    return list(dict.values())

#function to obtain the rotor permutations according to the rotorsettings
def getdictaccordingtosettings(rotortype_sr=0, rotortype_mr=1, rotortype_fr=2):
    
    chosen_rotortype = [rotortype_sr, rotortype_mr, rotortype_fr]
    #get the rotor encryption settings based on the user defined settings
    for RotorNo, RotorTyp in enumerate(chosen_rotortype):
        if RotorNo == 0:
            if RotorTyp == 0:
                rotor_permutations.update({"s_rotor" : dictvalues_tolist(RotorI)})
                rotor_permutations.update({"s_rotor_bw" : dictvalues_tolist(RotorI_bw)})
            elif RotorTyp == 1:
                rotor_permutations.update({"s_rotor" : dictvalues_tolist(RotorII)})
                rotor_permutations.update({"s_rotor_bw" : dictvalues_tolist(RotorII_bw)})
            elif RotorTyp == 2:
                rotor_permutations.update({"s_rotor" : dictvalues_tolist(RotorIII)})
                rotor_permutations.update({"s_rotor_bw" : dictvalues_tolist(RotorIII_bw)})
            elif RotorTyp == 3:
                rotor_permutations.update({"s_rotor" : dictvalues_tolist(RotorIV)})
                rotor_permutations.update({"s_rotor_bw" : dictvalues_tolist(RotorIV_bw)})
            elif RotorTyp == 4:
                rotor_permutations.update({"s_rotor" : dictvalues_tolist(RotorV)})
                rotor_permutations.update({"s_rotor_bw" : dictvalues_tolist(RotorV_bw)})
        if RotorNo == 1:
            if RotorTyp == 0:
                rotor_permutations.update({"m_rotor" : dictvalues_tolist(RotorI)})
                rotor_permutations.update({"m_rotor_bw" : dictvalues_tolist(RotorI_bw)})
            elif RotorTyp == 1:
                rotor_permutations.update({"m_rotor" : dictvalues_tolist(RotorII)})
                rotor_permutations.update({"m_rotor_bw" : dictvalues_tolist(RotorII_bw)})
            elif RotorTyp == 2:
                rotor_permutations.update({"m_rotor" : dictvalues_tolist(RotorIII)})
                rotor_permutations.update({"m_rotor_bw" : dictvalues_tolist(RotorIII_bw)})
            elif RotorTyp == 3:
                rotor_permutations.update({"m_rotor" : dictvalues_tolist(RotorIV)})
                rotor_permutations.update({"m_rotor_bw" : dictvalues_tolist(RotorIV_bw)})
            elif RotorTyp == 4:
                rotor_permutations.update({"m_rotor" : dictvalues_tolist(RotorV)})
                rotor_permutations.update({"m_rotor_bw" : dictvalues_tolist(RotorV_bw)})
        if RotorNo == 2:
            if RotorTyp == 0:
                rotor_permutations.update({"f_rotor" : dictvalues_tolist(RotorI)})
                rotor_permutations.update({"f_rotor_bw" : dictvalues_tolist(RotorI_bw)})
            elif RotorTyp == 1:
                rotor_permutations.update({"f_rotor" : dictvalues_tolist(RotorII)})
                rotor_permutations.update({"f_rotor_bw" : dictvalues_tolist(RotorII_bw)})
            elif RotorTyp == 2:
                rotor_permutations.update({"f_rotor" : dictvalues_tolist(RotorIII)})
                rotor_permutations.update({"f_rotor_bw" : dictvalues_tolist(RotorIII_bw)})
            elif RotorTyp == 3:
                rotor_permutations.update({"f_rotor" : dictvalues_tolist(RotorIV)})
                rotor_permutations.update({"f_rotor_bw" : dictvalues_tolist(RotorIV_bw)})
            elif RotorTyp == 4:
                rotor_permutations.update({"f_rotor" : dictvalues_tolist(RotorV)})
                rotor_permutations.update({"f_rotor_bw" : dictvalues_tolist(RotorV_bw)})
    
    rotor_permutations.update({"ref" : dictvalues_tolist(Reflector)})

#function to follow the encryption pathway once letter has been pressed - this function is a sub function for the on_encryptionpathway function
def getencodedletter(index, rotor_type):

    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #checks what rotor the signal is going through
    if rotor_type == "fastrotor":
        #sets the offset according to the rotor position
        offset = letterindex_fr
        #gives the right wire for that offset
        pressedkeyWire = index + offset
        #wraps around if needed
        if pressedkeyWire > 25:
            pressedkeyWire = pressedkeyWire % 26
        #returns the number at the other end of the wrire from a dictionary containing multidimensional lists
        encodedletter = rotor_permutations["f_rotor"][pressedkeyWire]
        #finally subtracts the offset from that letter, finds the letter in a list of letters from A to Z
        return s[(s.find(encodedletter) - offset) % 26]
    if rotor_type == "mediumrotor":
        offset = letterindex_mr
        pressedkeyWire = index + offset
        if pressedkeyWire > 25:
            pressedkeyWire = pressedkeyWire % 26
        encodedletter = rotor_permutations["m_rotor"][pressedkeyWire]
        return s[(s.find(encodedletter) - offset) % 26]
    if rotor_type == "slowrotor":
        offset = letterindex_sr
        pressedkeyWire = index + offset
        if pressedkeyWire > 25:
            pressedkeyWire = pressedkeyWire % 26
        encodedletter = rotor_permutations["s_rotor"][pressedkeyWire]
        return s[(s.find(encodedletter) - offset) % 26]
    if rotor_type == "reflector":
        offset = 0
        pressedkeyWire = index + offset
        if pressedkeyWire > 25:
            pressedkeyWire = pressedkeyWire % 26
        encodedletter = rotor_permutations["ref"][pressedkeyWire]
        return s[(s.find(encodedletter) - offset) % 26]
    if rotor_type == "slowrotor_bw":
        offset = letterindex_sr
        pressedkeyWire = index + offset
        if pressedkeyWire > 25:
            pressedkeyWire = pressedkeyWire % 26
        encodedletter = rotor_permutations["s_rotor_bw"][pressedkeyWire]
        return s[(s.find(encodedletter) - offset) % 26]
    if rotor_type == "mediumrotor_bw":
        offset = letterindex_mr
        pressedkeyWire = index + offset
        if pressedkeyWire > 25:
            pressedkeyWire = pressedkeyWire % 26
        encodedletter = rotor_permutations["m_rotor_bw"][pressedkeyWire]
        return s[(s.find(encodedletter) - offset) % 26]
    if rotor_type == "fastrotor_bw":
        offset = letterindex_fr
        pressedkeyWire = index + offset
        if pressedkeyWire > 25:
            pressedkeyWire = pressedkeyWire % 26
        encodedletter = rotor_permutations["f_rotor_bw"][pressedkeyWire]
        return s[(s.find(encodedletter) - offset) % 26]

#function to create an encryption pathway as the pressed letter moves along the rotors
def on_encryptionpathway(pressedletter):
   
    index = list(lampdict).index(pressedletter) #position of the pressed key
    encodedletter_fr = getencodedletter(index, "fastrotor")
    
    encodedletter_mr = getencodedletter(list(lampdict).index(encodedletter_fr), "mediumrotor")
    
    encodedletter_sr = getencodedletter(list(lampdict).index(encodedletter_mr), "slowrotor")
    
    encodedletter_ref = getencodedletter(list(lampdict).index(encodedletter_sr), "reflector")
    
    encodedletter_sr_bw = getencodedletter(list(lampdict).index(encodedletter_ref), "slowrotor_bw")
    
    encodedletter_mr_bw = getencodedletter(list(lampdict).index(encodedletter_sr_bw), "mediumrotor_bw")
    
    encodedletter_fr_bw = getencodedletter(list(lampdict).index(encodedletter_mr_bw), "fastrotor_bw")
    
    return encodedletter_fr_bw
# recursive function to draw the plugs and keep them on the screen
def drawplug(plugrects, pluglist, i):
    
    draw.rect(EnigmaDisplay, black, plugrects[i])
    get_text(pluglist[i], 20, False, white, plugrects[i].center)
    i+=1
    if len(plugrects) > i:
        drawplug(plugrects, pluglist, i)

#function that checks if the list has an even number of elements, (drops the last if not) then splits list into lists of 2 - made to use plugboard settings
def breaklist(pluglist):
    brokenlist = []
    listlength = len(pluglist)
    if listlength % 2 != 0:
        pluglist.pop(-1)
        listlength = len(pluglist)
    for x in range(0, listlength, 2):
        brokenlist.append(pluglist[x:x+2])
    return brokenlist

#function to exchange the letter with the other letter in a two member list
def exchange(listof2elements, letter):
    if letter == listof2elements[0]:
        exchangedletter = listof2elements[1]
    else:
        exchangedletter = listof2elements[0]
    return exchangedletter

# End of definitions and start of main program-----------------------
main_menu()
