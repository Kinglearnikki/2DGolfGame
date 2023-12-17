import os
import pygame
from ball import Ball

class NormalBall(Ball):
    def __init__(
        self,
        x: int,
        y: int,
        radius: int,
        image_filename: str,
        speed_multiplier=1
    ):
        super().__init__(x, y, radius, (255, 255, 255))
        self.speed_multiplier = speed_multiplier

        current_directory = os.getcwd()
        image_path = os.path.join(current_directory, "2DGolfGame\images", image_filename)

        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        except pygame.error as e:
            print("Error loading image:", e)

    def update_position(self, screen, width, height):
        self.current_pos[0] += self.speed[0] * self.speed_multiplier * 0.08
        self.current_pos[1] += self.speed[1] * self.speed_multiplier * 0.08
        super().update_position(screen, width, height)

    def set_speed_multiplier(self, multiplier: float):
        self.speed_multiplier = multiplier

    def draw(self, screen):
        screen.blit(self.image, (self.current_pos[0] - self.radius, self.current_pos[1] - self.radius))
