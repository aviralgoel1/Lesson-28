import pygame
pygame.init()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
white = (255, 255, 255)

width = 640
height = 480

window = pygame.display.set_caption("game screen")
window = pygame.display.set_mode((width, height))
window.fill(white)

pygame.draw.rect(window, red, (width//2-100, height//2-50, 200, 100))
pygame.font.Font(None, 36)
font = pygame.font.Font(None, 36)
text = font.render("Hello, Pygame!", True, blue)
text_rect = text.get_rect(center=(width//2, height//2))
window.blit(text, text_rect)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()