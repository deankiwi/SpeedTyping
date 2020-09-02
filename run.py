import random, time, keyboard, pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

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

words = {
    'Consistent': 'description',
    'Hyphen': 'description',
    'Architect': 'description',
    'Satisfy': 'description',
    'verify': 'description',
    'Cinnamon': 'description',
    'Atrium': 'description',
    'vehicle': 'description',
    'beginning': 'description',
    'connoisseur': 'description',
    'requirements': 'description',
    'Finalized': 'description',
    'license': 'description',
    'innovative ': 'description',
    'opinion': 'description',
    'variety': 'description',
    'padawan': 'description',
    'inconvenience': 'description',
    'apologize': 'description',
    'fabulous': 'description',
    'necessary': 'description',
    'claims': 'description'
}

dean = {
    'correct': []
}

longtext = "This is a a break " \
       "in the screen.\nIt can look strange sometimes.\n" \
       "e surface though, so sometimes " \
       "text urface"

n = 0
text = ''
previousUserWords = ['']
wordSelect = longtext.split(' ')[0]




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
    if currentWord:
        return currentword[0]
    else:
        return False








currentUserLocation = 0
start = time.process_time()

while True:  # making a loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key in (pygame.K_RETURN, pygame.K_SPACE):


                if text == currentWord:
                    currentUserLocation += 1
                    text = ''


            elif event.key ==  pygame.K_BACKSPACE:
                if len(text)>0:
                    text = text[0:-1]

            else:
                text += event.unicode



    DISPLAYSURF.fill((WHITE))
    currentWord = blit_text(DISPLAYSURF, longtext, (20,20),font,currentUserLocation)
    txt_current = font.render(text, True, color)
    txt_spell_word = font.render(currentWord,True,color)




    DISPLAYSURF.blit(txt_current,(DisplayWidth//2,5*DisplayHeight//6))

    DISPLAYSURF.blit(txt_spell_word, (DisplayWidth // 2, 2*DisplayHeight // 3))


    pygame.display.flip()
    FramePerSec.tick(FPS)

