import pygame
window=pygame.display.set_mode((400,400))
window.fill((255,255,255))

green=(0,225,0)
red=(225,0,0)
blue=(0,0,225) 

pygame.draw.circle(window,green,(200,200),50)
pygame.draw.circle(window,red,(200,200),50,3)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()