import pygame
import sys
import random
import time
import re

from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BEIGE = (249, 167, 176)
GREY = (200,200,200)

LEFT_CLICK = (1,0,0)
RIGHT_CLICK = (0,0,1)

pygame.init()

pygame.display.set_caption("Hangman")


Display = pygame.display.set_mode((500,550),0,32)

Easy = ["BELL","STAR","PICNIC", "PIE","HAT","HEART","FLAG","HELLO","LOVE"]
Medium = ["CARPET","POPCORN","SEAFOOD","DOORBELL","COWBOY",\
          "INSIDE","OUTSIDE","RAINBOW","POSTMAN","WATERMELON",\
          "FOOTBALL","STRAWBERRY"]
Hard = ["BACKGROUND","BOOKWORM","FIREFIGHTER","SOUNDPROOF","THUNDERSTORM",\
        "CAMPGROUND","FRIENDSHIP","SKYSCRAPER","SUPERHUMAN","FINGERPRINT",\
        "MASTERPIECE", "LOUDSPEAKER"]
Color = ["BLACK","WHITE","RED","GREEN","BLUE","GREY"]

Font = pygame.font.Font("freesansbold.ttf",33)
Font2 = pygame.font.Font("freesansbold.ttf",20)

Display.fill(WHITE)

def randomNum(choice):

    RandomNum=0

    if choice==1:
        RandomNum = random.randint(0, len(Easy)-1)

    elif choice==2:
        RandomNum=random.randint(0, len(Medium)-1)

    elif choice == 3:
        RandomNum=random.randint(0, len(Hard)-1)

    elif choice == 4:
        RandomNum=random.randint(0, len(Color)-1)
        
    return RandomNum



def List(RandomNum,choice):
    if (choice == 1):
        Word = Easy[RandomNum]

    elif (choice == 2):
        Word = Medium[RandomNum]

    elif (choice == 3):
        Word = Hard[RandomNum]

    elif (choice == 4):
        Word = Color[RandomNum]
        
    return Word

def Hangman(condition):
    if (condition == 0):
        pygame.draw.line(Display, GREY, (10,400),(300,400),8)
        pygame.draw.line(Display, GREY, (50,50),(50,400),8)
        pygame.draw.line(Display, GREY, (50,60),(250,60),8)
        pygame.draw.line(Display, GREY, (150,60),(150,100),8)
        pygame.draw.circle(Display, GREY, (150,150),50,8)
        pygame.draw.line(Display, GREY, (150,200),(150,300),8)
        pygame.draw.line(Display, GREY, (150,210),(100,250),8)
        pygame.draw.line(Display, GREY, (150,210),(200,250),8)
        pygame.draw.line(Display, GREY, (150,300),(100,350),8)
        pygame.draw.line(Display, GREY, (150,300),(200,350),8)

    elif (condition == 1):
        pygame.draw.line(Display, BLACK, (10,400),(300,400),8)

    elif (condition == 2):
        pygame.draw.line(Display, BLACK, (50,50),(50,400),8)

    elif (condition == 3):
        pygame.draw.line(Display, BLACK, (50,60),(250,60),8)

    elif (condition == 4):
        pygame.draw.line(Display, BLACK, (150,60),(150,100),8)

    elif (condition == 5):
        pygame.draw.circle(Display, BLACK, (150,150),50,8)

    elif (condition == 6):
        pygame.draw.line(Display, BLACK, (150,200),(150,300),8)

    elif (condition == 7):
        pygame.draw.line(Display, BLACK, (150,210),(100,250),8)

    elif (condition == 8):
        pygame.draw.line(Display, BLACK, (150,210),(200,250),8)

    elif (condition == 9):
        pygame.draw.line(Display, BLACK, (150,300),(100,350),8)

    elif (condition == 10):
        pygame.draw.line(Display, BLACK, (150,300),(200,350),8)


    elif (condition == 11):
        pygame.draw.line(Display, BLUE, (10,400),(300,400),8)
        pygame.draw.line(Display, BLUE, (50,50),(50,400),8)
        pygame.draw.line(Display, BLUE, (50,60),(250,60),8)
        pygame.draw.line(Display, BLUE, (150,60),(150,100),8)
        pygame.draw.circle(Display, BLUE, (150,150),50,8)
        pygame.draw.line(Display, BLUE, (150,200),(150,300),8)
        pygame.draw.line(Display, BLUE, (150,210),(100,250),8)
        pygame.draw.line(Display, BLUE, (150,210),(200,250),8)
        pygame.draw.line(Display, BLUE, (150,300),(100,350),8)
        pygame.draw.line(Display, BLUE, (150,300),(200,350),8)

def PreHangMan():
    pygame.draw.line(Display, GREEN, (10,420),(190,420),8)
    pygame.draw.line(Display, GREEN, (30,110),(30,420),8)
    pygame.draw.line(Display, GREEN, (30,120),(160,120),8)
    pygame.draw.line(Display, GREEN, (100,120),(100,140),8)
    pygame.draw.circle(Display, GREEN, (100,190),50,8)
    pygame.draw.line(Display, GREEN, (100,240),(100,340),8)
    pygame.draw.line(Display, GREEN, (100,250),(50,290),8)
    pygame.draw.line(Display, GREEN, (100,250),(150,290),8)
    pygame.draw.line(Display, GREEN, (100,340),(50,380),8)
    pygame.draw.line(Display, GREEN, (100,340),(150,380),8)
		
def StartScreen():
    Display.blit(pygame.font.Font("freesansbold.ttf",40).render("HANGMAN",True, RED), (150,20))
    Display.blit(Font.render("By: Abhijeet",True,BLUE), (155,50) )
    Display.blit(Font.render("Level Difficulty",True,BLACK), (200,150))
    Display.blit(Font2.render("1-Easy",True,BLACK), (200,200))
    Display.blit(Font2.render("2-Medium",True,BLACK), (200,250))
    Display.blit(Font2.render("3-Hard",True,BLACK), (200,300))
    Display.blit(Font2.render("4-Color",True,BLACK), (200,350))
          
def main():
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

    GREY = (200,200,200)

    TheChoice = 0
		
    StartScreen()
		
    PreHangMan()


    pygame.mixer.music.load('Music\KM\start.mp3')
    pygame.mixer.music.play(-1,0)
    
    FirstCondi = True
    while FirstCondi:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:

                if (event.key == K_1) or (event.key == 257):
                    TheChoice = 1
                    FirstCondi = False
                    break
                elif event.key == K_2 or event.key == 258:
                    TheChoice = 2
                    FirstCondi = False
                    break
                elif event.key == K_3 or event.key == 259:
                    TheChoice = 3
                    FirstCondi = False
                    break
                elif event.key == K_4 or event.key == 260:
                    TheChoice = 4
                    FirstCondi = False
                    break

            elif event.type == MOUSEBUTTONDOWN:

                if (pygame.mouse.get_pressed() != (0,0,0)):
                    pygame.mixer.Sound('Music\Mouse Click Fast.wav').play()
                    

                if (pygame.mouse.get_pos()[0] > 200 and\
                    pygame.mouse.get_pos()[1] > 200 and\
                    pygame.mouse.get_pos()[0] < 265 and\
                    pygame.mouse.get_pos()[1] < 215):
                    TheChoice = 1
                    FirstCondi = False
                    break

                elif (pygame.mouse.get_pos()[0] > 200 and\
                      pygame.mouse.get_pos()[1] > 250 and\
                      pygame.mouse.get_pos()[0] < 295 and\
                      pygame.mouse.get_pos()[1] < 265):
                    TheChoice = 2
                    FirstCondi = False
                    break

                elif (pygame.mouse.get_pos()[0] > 200 and\
                      pygame.mouse.get_pos()[1] > 300 and\
                      pygame.mouse.get_pos()[0] < 265 and\
                      pygame.mouse.get_pos()[1] < 315):
                    TheChoice = 3
                    FirstCondi = False
                    break

                elif (pygame.mouse.get_pos()[0] > 200 and\
                      pygame.mouse.get_pos()[1] > 350 and\
                      pygame.mouse.get_pos()[0] < 270 and\
                      pygame.mouse.get_pos()[1] < 365):
                    TheChoice = 4
                    FirstCondi = False
                    break
                
        if (TheChoice!= 0):
            Display.fill(WHITE)
            
        pygame.display.update()
        pygame.time.Clock().tick(30)
    
    TheNum = randomNum(TheChoice)
    TheWord = List(TheNum, TheChoice)


    EmptyList = []

    for i in range(len(TheWord)):
        EmptyList.append('-')


    Hidden = Font.render("".join(EmptyList),True,BLACK)
    HiddenRect = Hidden.get_rect()
    HiddenRect.center = (350,250)
    Display.blit(Hidden,HiddenRect)

    Condition = 0

    Off = 0

    TheTime = 0
    Start = time.time()

    Display.blit(Font2.render("Time(s):",True,BLACK),(300,10))

    LastKeyPressed = ""

    Display.blit(pygame.font.Font("freesansbold.ttf",15).render("Press 0 to quit game",True,BLACK),(20,10))
    
    while True:
        Hangman(Condition)
        End = time.time()
        if (int(End) - int(Start) == 1):
            pygame.draw.rect(Display,WHITE,(385,0,100,50))
            TheTime = TheTime + 1 

            Timer = Font2.render(str(TheTime),True,BLACK)
            Display.blit(Timer, (400,10))
            Start = time.time()
            
        for event in pygame.event.get():


            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                pygame.mixer.Sound('Music\Keyboard.wav').play()


                LastKeyPressed = event.key
                pygame.draw.rect(Display,WHITE,(220,200,280,100))
                pygame.draw.rect(Display,WHITE,(260,50,200,100))
                UserInput = event.key

                if re.search("[a-z]",chr(event.key)):
                    if ((chr(event.key).upper() in TheWord) or (chr(event.key).lower() in TheWord)):
                        for i in range(len(TheWord)):
                            if ((TheWord[i] == (chr(event.key)).upper()) or (TheWord[i] == (chr(event.key)).lower())):
                                EmptyList[i] = TheWord[i]

                    else:
                        Condition = Condition + 1

                    Hidden = Font.render("".join(EmptyList),True,BLACK)
                    HiddenRect = Hidden.get_rect()
                    HiddenRect.center = (350,250)
                    Display.blit(Hidden,HiddenRect)

                else:
                    if (event.key == K_0 or event.key == 256):
                        Display.blit(Font.render("EXIT?",True,RED),(340,220))
                        Display.blit(Font2.render("Yes",True,BLUE),(340,270))
                        Display.blit(Font2.render("No",True,BLUE),(415,270))
                    else:
                        Input = Font2.render("INVALID INPUT!!!",True,RED)
                        InputRect = Input.get_rect()
                        InputRect.center = (350,100)
                        Display.blit(Input, InputRect)
                        Display.blit(Hidden,HiddenRect)

            elif event.type == KEYUP:
                pygame.draw.rect(Display,WHITE,(260,50,200,100))

            elif event.type == MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pressed() != (0,0,0)):
                    pygame.mixer.Sound('Music\Mouse Click Fast.wav').play()

                if (LastKeyPressed == K_0 or LastKeyPressed == 256):
                    if (pygame.mouse.get_pressed() == LEFT_CLICK):
                        #Yes
                        if (pygame.mouse.get_pos()[0] > 340 and\
                            pygame.mouse.get_pos()[1] > 270 and\
                            pygame.mouse.get_pos()[0] < 385 and\
                            pygame.mouse.get_pos()[1] < 285):
                            pygame.draw.rect(Display,WHITE,(340,270,35,25))
                            Display.blit(Font2.render("Yes",True,GREEN),(340,270))


                        elif (pygame.mouse.get_pos()[0] > 415 and\
                              pygame.mouse.get_pos()[1] > 270 and\
                              pygame.mouse.get_pos()[0] < 450 and\
                              pygame.mouse.get_pos()[1] < 285):
                            pygame.draw.rect(Display,WHITE,(415,270,35,25))
                            Display.blit(Font2.render("No",True,GREEN),(415,270))



            elif event.type == MOUSEBUTTONUP:
                if (LastKeyPressed == K_0 or LastKeyPressed == 256):
                    if (pygame.mouse.get_pos()[0] > 340 and\
                       pygame.mouse.get_pos()[1] > 270 and\
                       pygame.mouse.get_pos()[0] < 385 and\
                       pygame.mouse.get_pos()[1] < 285):

                        #quit game
                        pygame.quit()
                        sys.exit()

                    #No
                    elif (pygame.mouse.get_pos()[0] > 415 and\
                          pygame.mouse.get_pos()[1] > 270 and\
                          pygame.mouse.get_pos()[0] < 450 and\
                          pygame.mouse.get_pos()[1] < 285):
                        pygame.draw.rect(Display,WHITE,(415,270,35,25))
                        Display.blit(Font2.render("No",True,GREEN),(415,270))
                        pygame.draw.rect(Display,WHITE,(300,200,200,100))

                        Hidden = Font.render("".join(EmptyList),True,BLACK)
                        HiddenRect = Hidden.get_rect()
                        HiddenRect.center = (400,250)
                        Display.blit(Hidden,HiddenRect)

                        LastKeyPressed = ""


                    else:
                        pygame.draw.rect(Display,WHITE,(340,270,35,25))
                        Display.blit(Font2.render("Yes",True,BLUE),(340,270))
                        pygame.draw.rect(Display,WHITE,(415,270,35,25))
                        Display.blit(Font2.render("No",True,BLUE),(415,270))


        if (Condition == 10):
            Display.fill(WHITE)
            Hangman(Condition+1)
            Over = Font.render("GAME OVER!!!", True, RED)
            word = Font.render(TheWord, True, BLUE)
            OverRect = Over.get_rect()
            OverRect.center = (350,250)
            Display.blit(Over, OverRect)

            Word = Font2.render("The word is:", True, BLACK)
            WordRect = Word.get_rect()
            WordRect.center = (350, 275)
            Display.blit(Word, WordRect)

            Word2 = Font2.render(TheWord, True, BLACK)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (350, 298)
            Display.blit(Word2, Word2Rect)

            Off = 1


            pygame.mixer.music.stop()

            pygame.mixer.music.load('Music\KM\Victory.mp3')
            pygame.mixer.music.play(0,0)




        elif (TheWord == "".join(EmptyList)):
            Display.fill(WHITE)
            Cong = Font.render("CONGRATS!!!",True,GREEN)
            CongRect = Cong.get_rect()
            CongRect.center = (250,220)
            Display.blit(Cong,CongRect)
            
            Word = Font2.render("The word is:",True,BLACK)
            WordRect = Word.get_rect()
            WordRect.center = (250,250)
            Display.blit(Word,WordRect)

            Word2 = Font.render(TheWord, True, BLACK)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (250, 285)
            Display.blit(Word2, Word2Rect)
            
            Off = 1


            pygame.mixer.music.stop()

            pygame.mixer.music.load('Music\KM\Victory.mp3')
            pygame.mixer.music.play(0,0)            

        pygame.display.update()
        pygame.time.Clock().tick(30)
        
        if (Off == 1):

            time.sleep(5)

            pygame.quit()
            sys.exit()

main()
