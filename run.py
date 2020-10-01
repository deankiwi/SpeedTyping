import pygame
import numpy as np
import time
import cv2
import sys
import datetime
from pygame.locals import *
import os

pygame.init()

FPS = 120
FramePerSec = pygame.time.Clock()
cap0 = cv2.VideoCapture(0)
#cap1 = cv2.VideoCapture(1)
path = '/data/run'


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

color = pygame.Color('dodgerblue2')
fontSize = 32
font = pygame.font.Font(None, fontSize)

DisplayWidth = 600
DisplayHeight = 600

DISPLAYSURF = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.RESIZABLE)
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption('Spelling Game')


#longtext = "a1a2aqaza s3swsxs d4dedcd f5frfvf6ftfgfbf j7jyjhjnjujm k8kik,k l9lol.l ;0;p;/;-;[;';];="
longtext = 'this is me testing out camera side by side'
n = 0
text = ''
previousUserWords = ['']
wordSelect = longtext.split(' ')[0]
lastimages = []

userkeyboard = 'logitech g810'



def blit_text(surface, text, pos, font, currentuserlocation, color=pygame.Color('black')):
    #https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    upto = 0
    currentword = []
    for line in words:
        for word in line:
            upto += 1
            if upto > currentuserlocation:
                currentword.append(word)
                color = pygame.Color('green')

            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    if currentword:
        return currentword[0]
    else:
        return ''








currentUserLocation = 0
logger = ''

filename = 'data/spellingQuiz-'+ datetime.datetime.now().strftime("%Y-%m-%d@%H#%M#%S") + '.txt'
startgame = True

while startgame:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_SPACE):

                startgame = False

start = datetime.datetime.now()

while True:  # making a loop
    ret, frame = cap0.read()
    #ret, frame = cap1.read()


    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:


            if event.key in (pygame.K_RETURN, pygame.K_SPACE):


                if text == currentWord:
                    with open(filename, 'a') as text_file:
                        text_file.write(f'{logger}\n')
                    currentUserLocation += 1
                    text = ''
                    logger = ''


            elif event.key ==  pygame.K_BACKSPACE:
                if len(text)>0:
                    logger += f'[{datetime.datetime.now()-start},h DELETE]\t'
                    text = text[0:-1]

            else:
                ret0, frame0 = cap0.read()
                #ret1, frame1 = cap1.read()
                if ret0 == True:
                    img_name = f"data/{int(round(time.time() * 1000))}{event.unicode}"
                    img_name0 = img_name +'a.png'
                    #img_name1 = img_name + 'b.png'
                    cv2.imwrite(img_name0, frame0)
                    #scv2.imwrite(img_name1, frame1)


                logger += f'[{datetime.datetime.now()-start}, {event.unicode}]\t'
                text += event.unicode


    DISPLAYSURF.fill((WHITE))
    currentWord = blit_text(DISPLAYSURF, longtext, (20,20),font,currentUserLocation)
    txt_current = font.render(text, True, color)
    txt_spell_word = font.render(currentWord,True,color)


    DISPLAYSURF.blit(txt_current,(DisplayWidth//2,5*DisplayHeight//6))
    DISPLAYSURF.blit(txt_spell_word, (DisplayWidth // 2, 2*DisplayHeight // 3))

    pygame.display.flip()
    FramePerSec.tick(FPS)

    if currentWord == '':
        print(f'total time: {datetime.datetime.now()-start}')
        pygame.quit()
        sys.exit()


cap0.release()
out.release()
cv2.destroyAllWindows()