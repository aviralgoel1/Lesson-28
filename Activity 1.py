import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
done=False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    rect=pygame.draw.rect(screen,(125,125,225), pygame.Rect(200,150,100,60))
    pygame.display.flip()