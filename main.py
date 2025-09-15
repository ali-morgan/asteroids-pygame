import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
import constants
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    (_, failed_mod_inits) = pygame.init()
    if failed_mod_inits > 0:
        print(f"Failed to initialize {failed_mod_inits} modules.")

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    AsteroidField.containers = updatable_group
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    field = AsteroidField()

    Player.containers = (updatable_group, drawable_group)
    p = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    deltaTime = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # p.update(deltaTime)
        updatable_group.update(deltaTime)

        window.fill(color="black")
        # p.draw(window)
        for drawable in drawable_group:
            drawable.draw(window)
        pygame.display.flip()

        dtMillis = clock.tick(constants.TARGET_FPS)
        deltaTime = dtMillis / 1000



if __name__ == "__main__":
    main()
