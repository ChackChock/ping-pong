from scripts.sprite import Sprite


class Rocket(Sprite):
    def __init__(self, center, image, speed):
        super().__init__(center, image)

        self.speed = speed
        self.is_moving_up = False
        self.is_moving_down = False

    def update(self, display_height):
        if self.is_moving_up is not self.is_moving_down:
            if self.is_moving_up:
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > display_height:
            self.rect.bottom = display_height
