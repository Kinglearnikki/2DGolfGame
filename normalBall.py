from ball import Ball


class NormalBall(Ball):
    def __init__(self, x: int, y: int, radius: int, color: tuple, speed_multiplier=1):
        super().__init__(x, y, radius, color)
        self.speed_multiplier = speed_multiplier

    def update_position(self, screen, width, height):
        # Override the update_position method to incorporate the speed multiplier
        self.current_pos[0] += self.speed[0] * self.speed_multiplier * 0.08
        self.current_pos[1] += self.speed[1] * self.speed_multiplier * 0.08

        # The rest of the collision detection remains the same as in the Ball class
        super().update_position(screen, width, height)

    def set_speed_multiplier(self, multiplier: float):
        self.speed_multiplier = multiplier