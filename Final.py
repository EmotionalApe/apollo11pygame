#main module
import pygame,sys

#imports pygame variables
from pygame.locals import *

#math for calculations
import math

#imports variables from moviepy which is used to video clips
from moviepy.editor import *

#imports module used to for GUI
from tkinter import *

#for storing inputted data in SQL
#import mysql.connector

#for plotting
import matplotlib.pyplot as pl

#for calculations
import numpy as np
    

#initialising the tkinter window
root = Tk()
root.geometry('500x500')
root.title("Input Speed")

#variables for Tkinter
Fullname=StringVar()
spd1 = IntVar()
spd2= IntVar()

#mysql connection
'''con=mysql.connector.connect (host="localhost", user= "root", password = "admin", database="maruf", auth_plugin='mysql_native_password')
csr=con.cursor()'''

#initailise module pygame
pygame.init()

#define window size
displayX=900
displayY=600

#frames displayed in a second.
FPS=30
#calculates time passed since last frame, used to determine framerate
fpsClock=pygame.time.Clock()

#defines a surface on display to copy and blit everything on.
displaysurf=pygame.display.set_mode((displayX,displayY),0,32)  

#display on top of window
pygame.display.set_caption('apollo11') 

#initialising colors in RGB
white=(255,255,255)
green=(0,255,0)
black=(0,0,0)
blue=(0,0,255)
sky=(135,206,235)

#white dot for transorbital maneuvers
img=pygame.image.load('transor.png')   
img1=pygame.image.load('transor.png')

#eagle lander image
eagle=pygame.image.load('eagle.jpeg')

#rocket, stage 1 image
rocketimg=pygame.image.load('rocket11.jpg')

#rocket, stage 2 image
rocketimgS2=pygame.image.load('stage2.png')

#earth image
earthimg=pygame.image.load('earth.jpg')

#transition upper and lower images
transU=pygame.image.load('transU.png')
transD=pygame.image.load('transD.png')

#spacecraft
spacecraft=pygame.image.load ('spacecraft.png')

#lunar injection
lunarInject = pygame.image.load ('tli.jpg')

#touchdown
touch=pygame.image.load ('Touchdown.png')

#moon image
moon=pygame.image.load ('moon.jpg')

#launch Clip, Armstrong Clip

launch=VideoFileClip('s.mp4')
armstrong=VideoFileClip('armstrong.mp4')

imgx=300
imgy=300
direction='right'

img1x=120
img1y=480

earthimgx=320
earthimgy=170

rocketx=200
rockety=600

rocketS2x=200
rocketS2y=600

transUx=305
transUy=100

transDx=300
transDy=275

craftx=50
crafty=300

Eaglex=300
Eagley=20

#font definition
font = pygame.font.Font('freesansbold.ttf', 32)

#main loop, white the condition is true (default), it runs.

while True:

    #fills display with black colour, used as a back ground
    displaysurf.fill(black)

    #pygame,time.get_ticks get time passed since init()
    timePassed=(pygame.time.get_ticks()/1000)
    
    # 1 degree=0.01745;33, every second Theta changes
    theta=(timePassed)+0.0174533
    
    #tkinter form
    if timePassed>0 and timePassed<5:  

        #define a function to be used with Tkinter
        def database():

           #globalising all variables so that they can be used anywhere
           global speed1
           global speed2
           global name1
           global graph1
           global graph2

           name1=Fullname.get()
           graph1=spd1.get()
           graph2=spd2.get()
           
           #scaling user inputted speed 1 to what can be used with pygame
           speed1=spd1.get()
           speed1=(speed1/10)
           speed1=600/speed1
           speed1=speed1*25
           speed1=600/speed1
           
           #scaling user inputted speed 1 to what can be used with pygame
           speed2=spd2.get()
           speed2=(speed2/10)
           speed2=600/speed2
           speed2=speed2*25
           speed2=600/speed2

           #adding the user inputted speed to database 
           '''csr.execute ("insert into std1 (name,stage1,stage2) values('{}',{},{})"\
                        .format(name1, graph1,graph2))
           con.commit()'''
   
        #title
        label_0 = Label(root, text="rocket simulator",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        #"name" text before the input  box
        label_1 = Label(root, text="Name",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)
        
        #input name box
        entry_1 = Entry(root,textvar=Fullname)
        entry_1.place(x=240,y=130)
        
        #"stage 1 speed" text box
        label_2 = Label(root, text="Stage 1 speed",width=20,font=("bold", 10))
        label_2.place(x=68,y=180)
        label_2a = Label (root, text ="(ideal = 2683m/s)", width=20, font = ("bold",10))
        label_2a.place (x=68,y=200)
        
        #input speed1 box
        entry_2 = Entry(root,textvar=spd1)
        entry_2.place(x=240,y=180)

        #"stage 2 speed" text box 
        label_3 = Label(root, text="Stage 2 speed",width=20,font=("bold", 10))
        label_3.place(x=68,y=230)
        label_3a = Label (root, text ="(ideal = 994m/s)", width=20, font = ("bold",10))
        label_3a.place (x=68,y=250)

        #input speed 2 input box 
        entry_3 = Entry(root,textvar=spd2)
        entry_3.place(x=240,y=230)

        #submit box that runs command database, inputted speed goes to SQL table
        Button(root, text='Submit',width=20,bg='brown',fg='white', command=database).place(x=180,y=380)

        #Start Simulation button destroys the window and starts pygame
        Button(root, text="start simulation", command=root.destroy).pack()
        
        '''con.commit()'''

        #closes the tkinter module
        root.mainloop()
        
    #loading window, added as a buffer
    elif timePassed>= 5 and timePassed<18:
        text = font.render('Loading...', True, white, black)
        textRect = text.get_rect()
        textRect.center = (450,300)
        displaysurf.blit(text,textRect)
        
    #Apollo 11 launch clip
    elif timePassed>=18 and timePassed<=42:
        launch.subclip(8,32).preview()  

    #stage 1 
    elif timePassed>42 and timePassed<=50: 
        
        rocketimg=pygame.transform.scale(rocketimg,(500,500))
        rockety-=speed1
        

        text = font.render('Stage 1', True, white, black)
        textRect = text.get_rect()
        textRect.center = (700,300) 

        tex=font.render('68km above Earth', True, white, black)
        texRect=tex.get_rect()
        texRect.center= (700,350)
        
        displaysurf.blit (rocketimg,(rocketx,rockety))
        displaysurf.blit(text,textRect)
        displaysurf.blit(tex,texRect)

    #transitionToStage2 
    elif timePassed>50 and timePassed<=56: 
        
        transU=pygame.transform.scale(transU,(37,180))
        transD=pygame.transform.scale(transD,(50,175))
        
        transUy-=1
        transDy+=1

        text = font.render('Transtion Stage', True, white, black)
        textRect = text.get_rect()
        textRect.center = (700,300) 

        tex=font.render('Stage 1 detached', True, white, black)
        texRect=tex.get_rect()
        texRect.center= (700,350)
        
        displaysurf.blit (transU,(transUx,transUy))
        displaysurf.blit (transD,(transDx,transDy))
        displaysurf.blit(text,textRect)
        displaysurf.blit(tex,texRect)

    #stage2
    elif timePassed>56 and timePassed<=63:  
        rocketimgS2=pygame.transform.scale(rocketimgS2,(50,300))

        rocketS2y-=speed2
        

        text = font.render('Stage 2', True, white, black)
        textRect = text.get_rect()
        textRect.center = (700,300) 

        tex=font.render('166km above Earth', True, white, black)
        texRect=tex.get_rect()
        texRect.center= (700,350)
        
        displaysurf.blit (rocketimgS2,(rocketS2x,rocketS2y))
        displaysurf.blit(text,textRect)
        displaysurf.blit(tex,texRect)

    #parkingorbit text
    elif timePassed>63 and timePassed<=67:  
        
        text = font.render('The rocket knocked Apollo into a parking orbit.', True, white, black)
        textRect = text.get_rect()
        textRect.center = (450,300) 

        tex=font.render('Here, some final checks were made.', True, white, black)
        texRect=tex.get_rect()
        texRect.center= (450,350)

        text1=font.render('The rocket fired again and set course to the moon', True, white, black)
        text1Rect=text1.get_rect()
        text1Rect.center= (450,400)
        
        displaysurf.blit (text1,text1Rect)
        displaysurf.blit(text,textRect)
        displaysurf.blit(tex,texRect)    
    
    #parkingOrbit
    elif timePassed >67 and timePassed<=77 :  
        
        imgx= (displayX/1.935)+(200*math.cos(-theta))   #centerPos + (radius*cos(theta))
        imgy=(displayY/1.935)+(200*math.sin (-theta))    #centerPos + (radius*sin(theta))
       
        img=pygame.transform.scale(img,(10,10))
        earthimg=pygame.transform.scale(earthimg, (300,300))

        text1=font.render('Parking Orbit', True, white, black)
        text1Rect=text1.get_rect()
        text1Rect.center= (700,500)
        
        displaysurf.blit(text1,text1Rect)
        displaysurf.blit(earthimg, (earthimgx, earthimgy))
        displaysurf.blit(img, (imgx,imgy))

    #translunarInjection
    elif timePassed>77 and timePassed<=82:  
        lunarInject = pygame.transform.scale (lunarInject, (900,600))
        displaysurf.blit (lunarInject,(0,0))   
    
    #pathInjection
    elif timePassed>82 and timePassed<=90:  
        earthimg=pygame.transform.scale (earthimg, (150,150))
        moon=pygame.transform.scale (moon,(120,120))
        img1=pygame.transform.scale(img1,(10,10))
        img1x=img1x+2.2
        img1y=img1y-0.65
        
        displaysurf.blit(earthimg, (50,300))
        displaysurf.blit(moon,(650,300))
        displaysurf.blit(img1,(img1x,img1y))
    
    #spacecraftExplain
    elif timePassed>90 and timePassed<=98:  
        
        text = font.render('The rocket ditched the stage 3 rocket too.', True, white, black)
        textRect = text.get_rect()
        textRect.center = (450,300) 

        tex=font.render('Now only left with the Apollo Spacecraft.', True, white, black)
        texRect=tex.get_rect()
        texRect.center= (450,350)

        text1=font.render("It was pulled into the moon's orbit due to its gravity", True, white, black)
        text1Rect=text1.get_rect()
        text1Rect.center= (450,400)
        
        displaysurf.blit (text1,text1Rect)
        displaysurf.blit(text,textRect)
        displaysurf.blit(tex,texRect)  

    #spaceCraft
    elif timePassed>98 and timePassed<=103:  
        spacecraft=pygame.transform.scale (spacecraft, (300,100))
        craftx+=3
        displaysurf.blit(spacecraft, (craftx,crafty))

    #moonOrbit
    elif timePassed >103 and timePassed<=110 :  
        
        imgx= (displayX/1.935)+(200*math.cos(theta))   #centerPos + (radius*cos(theta))
        imgy=(displayY/1.935)+(200*math.sin (theta))    #centerPos + (radius*sin(theta))
       
        img=pygame.transform.scale(img,(10,10))
        moon=pygame.transform.scale(moon, (300,300))

        text1=font.render('lunar orbit', True, white, black)
        text1Rect=text1.get_rect()
        text1Rect.center= (700,500)
        
        displaysurf.blit(text1,text1Rect)
        displaysurf.blit(moon, (320, 170))
        displaysurf.blit(img, (imgx,imgy))    

    #landing explaination
    elif timePassed>110 and timePassed<=117:  
        
        text = font.render('Now, the spaceCraft split up into 2', True, white, black)
        textRect = text.get_rect()
        textRect.center = (450,300) 

        tex=font.render("the Command module, 'Columbia' and the Lander, 'Eagle'", True, white, black)
        texRect=tex.get_rect()
        texRect.center= (450,350)

        text1=font.render('Armstrong and Aldrin decended on the Moon surface.', True, white, black)
        text1Rect=text1.get_rect()
        text1Rect.center= (450,400)

        text2=font.render('Collins stayed back in the command module', True, white, black)
        text2Rect=text2.get_rect()
        text2Rect.center= (450,450)
        
        displaysurf.blit (text1,text1Rect)
        displaysurf.blit(text,textRect)
        displaysurf.blit(tex,texRect)
        displaysurf.blit(text2,text2Rect)
    
    #EagleLander
    elif timePassed>117 and timePassed<=124:  
        eagle=pygame.transform.scale (eagle, (300,300))
        Eagley+=3
        displaysurf.blit(eagle, (Eaglex,Eagley))

    #touchDown
    elif timePassed>124 and timePassed<=129:  
        touch=pygame.transform.scale (touch, (900,600))
        displaysurf.blit(touch, (0,0))    

    #Neil Armstrong clip
    elif timePassed>129 and timePassed<=143:  
        armstrong.subclip(16,).preview()

    #plotting ideal speed 1 to user inputted speed 1 graph
    elif timePassed>143 and timePassed<=160 :

        #random values 0 to 1
        x=[0,1]
        #user input
        sp1grph= [0,graph1]

        #stage 1 plot
        pl.plot(x,sp1grph, color='r', label="user's speed")
        
        pl.title("stage 1 speed graph")

        #ideal plot
        pl.plot(x,[0,2682], color = 'b', label="Apollo 11's speed")

        pl.legend(loc="upper left")
        pl.show()

    #plotting ideal speed 1 to user inputted speed 1 graph
    elif timePassed>160 and timePassed<=200:
        #random values 0 to 1 
        x=[0,1] 

         #user input values   
        sp2grph= [0,graph2]
        
        #plotting user input
        pl.plot(x,sp2grph,color = 'r', label = "user's speed")
        
        #plotting ideal
        pl.plot(x,[0,994], color = 'b', label = "Apollo 11's speed")

        #title of graph   
        pl.title ("stage 2 speed graph")

        pl.legend(loc="upper left")

        pl.show()

    #gets a list of events that happens in pygame
    for event in pygame.event.get():

        #if event is QUIT, it quits the module, X button
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    #updates the display at every frame.
    pygame.display.update()       
            
    #changes clock timing with respect to inputted framrate ie 30 FPS
    fpsClock.tick(FPS)
   
    
