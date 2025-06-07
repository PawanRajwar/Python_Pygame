import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 250
y = 250
radius = 15
vel_x = 10
vel_y = 10
jump = False

run = True
while run:
    
    win.fill((0,0,0))
    pygame.draw.circle(win,(255,255,255),(int(x), int(y)), radius)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
    user_Input = pygame.key.get_pressed()
    
    if user_Input[pygame.K_LEFT] and x > 0:
        x -= vel_x     
    if user_Input[pygame.K_RIGHT] and x < 500:
        x += vel_x
    
    if jump is False and user_Input[pygame.K_SPACE]:
        jump = True
    
    if jump is True:
        y -= vel_y  * 4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10
        
        
        
        
        
   # if user_Input[pygame.K_UP] and y > 0:
    #    y -= vel  
    #if user_Input[pygame.K_DOWN] and y < 500:
     #   y += vel    
    
    pygame.time.delay(25)
        
    pygame.display.update()