import pygame
from pygame.locals import *

pygame.init()
images = []
index = 0
displayWidth = 500
displayHeight = 500
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
white = (255,255,255)
backgroundImage = pygame.image.load('background.png')
background_height = backgroundImage.get_rect().height
imageOne = pygame.image.load('spaceship64X64transparent.png')
spaceInvader = pygame.image.load('64x82.png')
scoreBoard = pygame.image.load('scoreBoard.png')
lineScore = pygame.image.load('lineTransparent.png')
one = pygame.image.load('oneTransparent.png')
bolt = pygame.image.load('bolt.png')
#imageOne = pygame.image.load('spaceshipBiggerEditTwoTransparent.png')

def gameIntro():
    imageLogo = pygame.image.load('LT.png')
    imageButton = pygame.image.load('startButton.png')
    imageButtonTwo = pygame.image.load('startButtonTwo.png')
    exitButton = pygame.image.load('exit.png')
    exitButtonTwo = pygame.image.load('exitTwo.png')
    helpButton = pygame.image.load('help.png')
    helpButtonTwo = pygame.image.load('helpTwo.png')
    
    intro = True
    while intro:
        for eventOne in pygame.event.get():
            print(eventOne)
            if eventOne.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(backgroundImage, (0,0))
        gameDisplay.blit(imageLogo, (90,80))
         
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 180+100 > mouse[0] > 180 and 270+20 > mouse[1] > 270:
            gameDisplay.blit(imageButtonTwo,(180,270))
            if click[0] == 1:
                intro = False
                loop()
        else:
            gameDisplay.blit(imageButton, (180,270))
        if 178+100 > mouse[0] > 180 and 350+20 > mouse[1] > 350:
            gameDisplay.blit(exitButtonTwo, (178,350))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            gameDisplay.blit(exitButton, (178,350))
        if 184+100 > mouse[0] > 184 and 310+20 > mouse[1] > 310:
            gameDisplay.blit(helpButtonTwo, (184, 310))
            if click[0] == 1:
                helpWindow()
        else:
            gameDisplay.blit(helpButton,(184,310))
        pygame.display.update()
        ##clock.tick(15)

def helpWindow():
    helpText = pygame.image.load('helpText.png')
    yellowArrow = pygame.image.load('arrowYellow.png')
    redArrow = pygame.image.load('arrowRed.png')
    helpWindow = True
    while helpWindow:
        for eventOne in pygame.event.get():
            print(eventOne)
            if eventOne.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        gameDisplay.blit(backgroundImage, (0,0))
        if 20+100 > mouse[0] > 20 and 440+50 > mouse[1] > 440:
            gameDisplay.blit(redArrow, (20,440))
            if click[0] == 1:
                helpWindow = False
                gameIntro()
        else:
            gameDisplay.blit(yellowArrow, (20,440))
        gameDisplay.blit(helpText, (10,10))
        pygame.display.update()
    

def drawRect(x,y,z,w,color, display):
    pygame.draw.rect(display,white,(x,y,z,w))
    
def mainDisplay():
    #imageOne = pygame.image.load('spaceship64X64transparent.png')
    #imageTwo = pygame.image.load('spaceship64X64TwoTransparent.png')
    #images.append(imageOne)
    #images.append(imageTwo)
    print("hello World")

def update(x,y):
    index = 0
    index += 1
    if index >= len(images):
        index = 0
    image = images[index]
    
    gameDisplay.blit(image,(x,y))
    

def loop():
    pygame.display.set_caption("Window")
    clock = pygame.time.Clock()
    gameDisplay.blit(backgroundImage, (0,0))
    gameDisplay.fill(white)
    crashed = False
    x = (displayWidth*0.45)
    y =(displayHeight * 0.8)
    xChange = 0
    yChange = 0
    x_bg = 0
    imageWidth = 64
    imageLength = 64
    index = 0
    mainDisplay()

    while not crashed:
        x_loop = x_bg % background_height
        gameDisplay.blit(backgroundImage, (0,x_loop - background_height))
        if x_loop < displayHeight:
            gameDisplay.blit(backgroundImage, (0,x_loop))
        x_bg += 10
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                print(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -5
                elif event.key == pygame.K_RIGHT:
                    xChange = 5
                elif event.key == pygame.K_UP:
                    yChange = -5
                elif event.key == pygame.K_DOWN:
                    yChange = 5
                elif event.key == pygame.K_SPACE:
                    counter = True
                    counterInt = 0
                    while counter:
                        gameDisplay.blit(bolt,(100,500-x_loop))
                        #pygame.display.update()
                        #pygame.display.flip()
                        print(x_loop)
                        counterInt += 1
                        if counterInt <= 30:
                            counter = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yChange = 0
                elif event.key == pygame.K_SPACE:
                    counter = False
                    ##if x == ##border control for objects
            
        x += xChange
        y += yChange
        if (x + xChange) > displayWidth - imageWidth or (x + xChange) < 0:
                x_ch = 0
        if (y + yChange) > displayHeight - imageLength or (y + yChange) < 0:
                yChange = 0
            
        if x > displayWidth - imageWidth:
            x = 0
        if x < 0:
            x = 484
        if y < 0:
            y = 484
        if y > displayHeight - imageLength:
            y = 0

               
        index += 1
        #index %= len(images)
        image2 = pygame.image.load('spaceship64X64transparent2.png')
        image3 = pygame.image.load('spaceship64X64transparent3.png')
        image4 = pygame.image.load('spaceship64X64transparent4.png')
        image5 = pygame.image.load('spaceship64X64transparent5.png')
        image6 = pygame.image.load('spaceship64X64transparent6.png')
        image7 = pygame.image.load('spaceship64X64transparent7.png')
        image8 = pygame.image.load('spaceship64X64transparent8.png')
        image9 = pygame.image.load('spaceship64X64transparent9.png')
        image10 = pygame.image.load('spaceship64X64transparent10.png')
        image11 = pygame.image.load('spaceship64X64transparent11.png')
        image12 = pygame.image.load('spaceship64X64transparent12.png')
        image13 = pygame.image.load('spaceship64X64transparent13.png')
        image14 = pygame.image.load('spaceship64X64transparent14.png')
        image15 = pygame.image.load('spaceship64X64transparent15.png')
        image16 = pygame.image.load('spaceship64X64transparent16.png')
        
        #images.append(imageOne)
        images.append(image2)
        images.append(image3)
        images.append(image4)
        images.append(image5)
        images.append(image6)
        images.append(image7)
        images.append(image8)
        images.append(image9)
        images.append(image10)
        images.append(image11)
        images.append(image12)
        images.append(image13)
        images.append(image14)
        images.append(image15)
        images.append(image16)
        currentImage = images[index]
        ##imageOne = pygame.image.load('spaceship64X64transparent.png')
        ##gameDisplay.blit(backgroundImage, (0,0))
        ##update(x,y)
        ##drawRect(50,50,50,50,white,gameDisplay)
        gameDisplay.blit(spaceInvader,(50,50))
        gameDisplay.blit(currentImage,(x,y))
        gameDisplay.blit(bolt,(x+50,y+50))
        gameDisplay.blit(lineScore,(430,20))
        gameDisplay.blit(scoreBoard,(430,5))
        gameDisplay.blit(one,(430,25))
        
        #mainDisplay()
        #

        pygame.display.update()
        #pygame.display.flip()
        clock.tick(60)

gameIntro()
##loop()
pygame.quit()
quit()

        

