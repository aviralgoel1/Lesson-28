import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Colour changing Sprite")

    colours = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "purple": (128, 0, 128),
        "white": (255, 255, 255)
    }
    current_colour = colours['white']

    x, y = 30, 30
    sprite_width, sprite_height = 50, 50
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Check key states every frame (not just on events)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= 3
        if pressed[pygame.K_RIGHT]:
            x += 3
        if pressed[pygame.K_UP]:
            y -= 3
        if pressed[pygame.K_DOWN]:
            y += 3

        # Keep sprite within screen bounds
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        # Change colour based on position
        if x == 0:
            current_colour = colours['red']
        elif x == screen_width - sprite_width:
            current_colour = colours['green']
        elif y == 0:
            current_colour = colours['blue']
        elif y == screen_height - sprite_height:
            current_colour = colours['yellow']
        elif x == y:
            current_colour = colours['purple']
        else:
            current_colour = colours['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_colour, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == "__main__":
    main()