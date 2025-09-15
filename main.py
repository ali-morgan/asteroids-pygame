import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import constants
from player import Player
import player
from shot import Shot

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
    shots_group = pygame.sprite.Group()

    Shot.containers = (shots_group, updatable_group, drawable_group)
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

        for asteroid in asteroid_group:
            if asteroid.is_colliding(p):
                print("Game Over!")
                return
            for shot in shots_group:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

        window.fill(color="black")
        # p.draw(window)
        for drawable in drawable_group:
            drawable.draw(window)
        pygame.display.flip()

        dtMillis = clock.tick(constants.TARGET_FPS)
        deltaTime = dtMillis / 1000



if __name__ == "__main__":
    main()
