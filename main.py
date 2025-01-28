import pygame

from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                return
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
                    break

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()