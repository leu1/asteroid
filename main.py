import pygame
from constants import *
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock() # frames per second
    dt = 0 # delta time in seconds

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0 # 60 frames per second 
if __name__ == "__main__":
    main()
