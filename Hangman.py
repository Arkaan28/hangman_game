import pygame
import os
import math

# setup display
pygame.init()
WIDTH,HEIGHT = 900, 600
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HANGMAN GAME")


# fonts
LETTER_FONT = pygame.font.SysFont("calibri", 30)
WORD_FONT = pygame.font.SysFont("Arial", 40)

# load images
images = []
for i in range(7):
    path = r"images/hangman"
    image=pygame.image.load(path + str(i)+".png")
    images.append(image)

# print(images)


# button variables
DIAMETER = 40
GAP = 20
A = 65
letters = []
xstart = int((WIDTH-((DIAMETER+GAP)*12+DIAMETER))/2) + GAP
ystart = HEIGHT-((GAP+DIAMETER)*2)

# x =  xstart
y =  ystart
for i in range(26):
    x = xstart + (i%13)*(DIAMETER + GAP)
    y = ystart + ((DIAMETER + GAP)*int(i/13))
    letters.append([x, y, chr(A + i), True])


# game variables
hangman_status=0
word = "ARKAAN"
guessed = []


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# setup game loop
FPS = 60
clock = pygame.time.Clock()

def draw():
    win.fill(WHITE)

    disp_word=""
    for l in word:
        if l in guessed:
            disp_word = disp_word + l + " "
        else:
            disp_word = disp_word + "_ "
        
        text_word = WORD_FONT.render(disp_word, 1, BLACK)
        win.blit(text_word, (450,200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), DIAMETER/2, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    win.blit(images[hangman_status], (150,100))
    pygame.display.update()


# win/lose display
def message_out(message):
    won_text = WORD_FONT.render(message, 1, BLACK)
    win.fill(WHITE)
    win.blit(won_text, (WIDTH/2 - won_text.get_width()/2, HEIGHT/2 - won_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(6000)


run = True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((m_x-x)**2 +(m_y-y)**2)
                    if dis < DIAMETER/2:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
        
    draw()
            
    won = True
    for every_letter in word:
        if every_letter not in guessed:
            won = False
            break 
            
    if won:
        message_out("You Won!")
        break

    if hangman_status == 6:
        message_out("You Lost!")
        break

pygame.quit() 