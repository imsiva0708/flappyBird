import config
from player import Player
import pygame

class Population:
    def __init__(self):
        self.player = Player()

    def update_live_players(self, events):  # Accept events from the main loop
        if self.player.alive:
            self.manual_play(events)  # Pass the events list here
            self.player.draw(config.window)
            self.player.update(config.ground)

    def manual_play(self, events):  # Accept events from update_live_players()
        # print("Detected events:", events)  # Debugging step
        for event in events:
            if event.type == pygame.KEYDOWN:
                print(f"Key pressed: {event.key}")  # Check which key was detected
                if event.key == pygame.K_SPACE:
                    print('hi')
                    self.player.bird_flap()
