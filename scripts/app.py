import os
import pygame

from scripts.ball import Ball
from scripts.rocket import Rocket


class App:
    def __init__(self):
        self.running = True
        self.maxFPS = 60
        self.display_size = pygame.Vector2(900, 600)
        self.score = [0, 0]

        self.display = pygame.display.set_mode(self.display_size)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 64)

        image = pygame.Surface((50, 100))
        image.fill((255, 255, 255))

        self.left_rocket = Rocket((50, self.display_size.y/2), image, 5)
        self.right_rocket = Rocket((self.display_size.x - 50, self.display_size.y/2), image, 5)

        image = pygame.Surface((20, 20))
        pygame.draw.circle(image, (255, 255, 255), (10, 10), 10)
        image.set_colorkey((0, 0, 0))

        self.ball = Ball(self.display_size/2, image, 5)
        self.ball.reset(self.display_size/2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.left_rocket.is_moving_up = True
                elif event.key == pygame.K_s:
                    self.left_rocket.is_moving_down = True
                elif event.key == pygame.K_UP:
                    self.right_rocket.is_moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.right_rocket.is_moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.left_rocket.is_moving_up = False
                elif event.key == pygame.K_s:
                    self.left_rocket.is_moving_down = False
                elif event.key == pygame.K_UP:
                    self.right_rocket.is_moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.right_rocket.is_moving_down = False

    def update(self):
        self.left_rocket.update(self.display_size.y)
        self.right_rocket.update(self.display_size.y)
        self.ball.update(self.display_size.y)

        if self.ball.collide_sprite(self.left_rocket):
            self.ball.bounce(self.left_rocket)
        if self.ball.collide_sprite(self.right_rocket):
            self.ball.bounce(self.right_rocket)

        if self.ball.rect.right >= self.display_size.x:
            self.ball.reset(self.display_size/2)
            self.score[0] += 1
        if self.ball.rect.left <= 0:
            self.ball.reset(self.display_size/2)
            self.score[1] += 1

    def render(self):
        self.display.fill((0, 0, 0))

        pygame.draw.line(
            self.display, (200, 200, 200),
            (self.display_size.x/2, 0), (self.display_size.x/2, self.display_size.y),
            5
        )
        pygame.draw.circle(self.display, (0, 0, 0), self.display_size/2, 30)
        pygame.draw.circle(self.display, (200, 200, 200), self.display_size/2, 30, 5)

        self.left_rocket.render(self.display)
        self.right_rocket.render(self.display)
        self.ball.render(self.display)

        text = f"{self.score[0]}  {self.score[1]}"
        text_image = self.font.render(text, True, (255, 255, 255))
        self.display.blit(text_image, text_image.get_rect(midtop=(self.display_size.x/2, 10)))

        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            self.clock.tick(self.maxFPS)
