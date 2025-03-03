import config
from player import Player
import pygame


class Population:
    def __init__(self, size):
        self.players = []
        self.size = size
        for i in range(0, self.size):
            self.players.append(Player())

    def update_live_players(self, events):  # Accept events from the main loop
        for player in self.players:
            if player.alive:
                # self.manual_play(events)  # Pass the events list here
                player.look()
                player.think()
                player.draw(config.window)
                player.update(config.ground)

    def manual_play(self, events):  # Accept events from update_live_players()
        for event in events:
            if event.type == pygame.KEYDOWN:
                print(f"Key pressed: {event.key}")  # Check which key was detected
                if event.key == pygame.K_SPACE:
                    print('hi')
                    self.player.bird_flap()

    def extinct(self):
        extinct = True
        p: Player
        for p in self.players:
            if p.alive:
                return False
        return extinct
