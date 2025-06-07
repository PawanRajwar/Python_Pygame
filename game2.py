import pygame
pygame.init()

win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Second Game")
bg_img = pygame.image.load('Background.png')
bg = pygame.transform.scale(bg_img, (1000, 500))
width = 1000
i= 0

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0,0,0))
    win.blit(bg, (i,0))
    win.blit(bg, (width+i, 0))
    i = i - 1
    if i <= -width:
        i = 0 
    pygame.display.update()
    
pygame.time.delay(25)