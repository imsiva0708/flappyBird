import pygame
from sys import exit
import config
from components import Pipes
import population

p: Pipes
pygame.init()
clock = pygame.time.Clock()
population = population.Population()


def generate_pipes():
    config.pipes.append(Pipes(config.WIN_WIDTH))


def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def main():
    pipes_spawn_time = 10

    while True:
        # quit_game()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        config.window.fill((0, 0, 0))

        # Spawn Ground
        config.ground.draw(config.window)

        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1
        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)
        
        population.update_live_players(events)

        clock.tick(90)
        pygame.display.flip()


if __name__ == '__main__':
    main()
