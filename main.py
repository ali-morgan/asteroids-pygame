import pygame
import constants

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    (_, failed_mod_inits) = pygame.init()
    if failed_mod_inits > 0:
        print(f"Failed to initialize {failed_mod_inits} modules.")


    window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        window.fill(color="black")
        pygame.display.flip()



if __name__ == "__main__":
    main()
