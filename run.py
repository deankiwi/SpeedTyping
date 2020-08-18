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
DisplayHeight = 300

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
n = 0
text = ''
previousUserWords = ['']
wordSelect = random.choice(list(words.keys()))
nextWord = random.choice(list(words.keys()))



def blit_text(surface, text, pos, font, currentUserLocation, color=pygame.Color('black')):
    #https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    upto = 0
    for line in words:
        for word in line:
            upto += 1
            if upto > currentUserLocation:
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

longtext = "This is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
       "in the sentence, but that's because the text is too long to fit the screen.\nIt can look strange sometimes.\n" \
       "This function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
       "text will disappear underneath the surface"


previousWordColour = RED

currentUserLocation = 10

while True:  # making a loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key in (pygame.K_RETURN, pygame.K_BACKSPACE, pygame.K_SPACE):
                currentUserLocation += 1
                if text.lower() == wordSelect.lower():
                    previousWordColour = GREEN
                else:
                    previousWordColour = RED
                previousUserWords.append(text)
                text = ''
                wordSelect = nextWord
                nextWord = random.choice(list(words.keys()))



            else:
                text += event.unicode
                if text.lower() not in wordSelect.lower():
                    previousUserWords.append(text)
                    text = ''
                    wordSelect = nextWord
                    nextWord = random.choice(list(words.keys()))
                    previousWordColour = RED







    DISPLAYSURF.fill((WHITE))
    txt_surface = font.render(text, True, color)
    txt_previous = font.render(previousUserWords[-1],True,previousWordColour)
    txt_spell_word = font.render(wordSelect,True,color)
    txt_nextWord = font.render(nextWord,True,color)

    blit_text(DISPLAYSURF, longtext, (20,20),font,currentUserLocation)

    DISPLAYSURF.blit(txt_surface,(DisplayWidth//2,DisplayHeight//2))
    DISPLAYSURF.blit(txt_previous,(DisplayWidth//20,DisplayHeight//2))
    DISPLAYSURF.blit(txt_spell_word, (DisplayWidth // 2, DisplayHeight // 3))
    DISPLAYSURF.blit(txt_nextWord, (3* DisplayWidth // 4, DisplayHeight // 3))

    pygame.display.flip()
    FramePerSec.tick(FPS)

