import os
import pygame
from ball import Ball

# import random


class StickyBall(Ball):
    def __init__(
        self,
        x: int,
        y: int,
        radius: int,
        image_filename: str,
        special_attribute: str,
        speed_multiplier=1,
    ):
        super().__init__(x, y, radius, (255, 255, 255))
        self.special_attribute = special_attribute
        self.initial_speed_multiplier = speed_multiplier
        self.speed_multiplier = speed_multiplier

        current_directory = os.getcwd()
        image_path = os.path.join(current_directory, "images", image_filename)

        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (radius*2, radius*2))
        except pygame.error as e:
            print("Error loading image:", e)

    def draw(self, screen):
        screen.blit(self.image, (self.current_pos[0] - self.radius, self.current_pos[1] - self.radius))

    def special_method(self):
        print(f"This is a special ball with attribute: {self.special_attribute}")

    def handle_collision(self, screen_width, screen_height, obstacles):
        # Check collision with obstacles
        # Check collision with obstacles
        for obstacle in obstacles:
            if (
                self.current_pos[0] + self.radius >= obstacle.x - self.radius
                and self.current_pos[0] - self.radius
                <= obstacle.x + obstacle.width + self.radius
                and self.current_pos[1] + self.radius >= obstacle.y - self.radius
                and self.current_pos[1] - self.radius
                <= obstacle.y + obstacle.height + self.radius
            ):
                self.speed = [0, 0]  # Stop movement
                break  # Exit the loop after the first collision

    def set_speed_multiplier(self, multiplier: int):
        self.speed_multiplier = multiplier