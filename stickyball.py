from ball import Ball
# import random


class StickyBall(Ball):
    def __init__(
        self,
        x: int,
        y: int,
        radius: int,
        color: tuple,
        special_attribute: str,
        speed_multiplier=1,
    ):
        super().__init__(x, y, radius, color)
        self.special_attribute = special_attribute
        self.initial_speed_multiplier = speed_multiplier
        self.speed_multiplier = speed_multiplier

    def special_method(self):
        print(f"This is a special ball with attribute: {self.special_attribute}")

    def handle_release(self, mouse_pos):
        if self.dragging and (self.velocity[0] ** 2 + self.velocity[1] ** 2 < 1):
            # Add current ball position to drag_line list
            self.drag_line.append(self.current_pos)

            # Calculate the distance and direction of the mouse drag
            drag_distance = (
                (self.current_pos[0] - mouse_pos[0]) ** 2
                + (self.current_pos[1] - mouse_pos[1]) ** 2
            ) ** 0.5

            drag_direction = [
                self.current_pos[0] - mouse_pos[0],
                self.current_pos[1] - mouse_pos[1],
            ]

            # Check if drag_distance is not zero
            if drag_distance != 0:
                # Normalize the direction vector
                drag_direction = [i / drag_distance for i in drag_direction]
                # Make the velocity proportional to the drag distance and in the direction of the drag
                self.velocity = [
                    i * drag_distance * 0.05 * self.speed_multiplier
                    for i in drag_direction
                ]
            else:
                self.velocity = [0, 0]

            self.dragging = False

    def handle_collision(self, screen_width, screen_height, obstacles):
        # Check collision with screen boundaries
        if (
                self.current_pos[0] - self.radius < 0
                or self.current_pos[0] + self.radius > screen_width
        ):
            self.velocity[0] = 0  # Stop horizontal movement

        if (
                self.current_pos[1] - self.radius < 0
                or self.current_pos[1] + self.radius > screen_height
        ):
            self.velocity[1] = 0  # Stop vertical movement

        # Check collision with obstacles
        for obstacle in obstacles:
            if (
                    self.current_pos[0] + self.radius >= obstacle.x
                    and self.current_pos[0] - self.radius <= obstacle.x + obstacle.width
                    and self.current_pos[1] + self.radius >= obstacle.y
                    and self.current_pos[1] - self.radius <= obstacle.y + obstacle.height
            ):
                # Determine the direction of the overlap
                overlap_x = max(
                    0,
                    min(
                        self.current_pos[0] + self.radius - obstacle.x,
                        obstacle.x + obstacle.width - (self.current_pos[0] - self.radius),
                        ),
                )
                overlap_y = max(
                    0,
                    min(
                        self.current_pos[1] + self.radius - obstacle.y,
                        obstacle.y + obstacle.height - (self.current_pos[1] - self.radius),
                        ),
                )

                # Determine the direction of the overlap
                if overlap_x < overlap_y:
                    # Resolve collision in the x-direction
                    if self.velocity[0] > 0:
                        self.current_pos[0] = obstacle.x - self.radius
                    else:
                        self.current_pos[0] = obstacle.x + obstacle.width + self.radius
                    self.velocity[0] = 0  # Stop horizontal movement
                else:
                    # Resolve collision in the y-direction
                    if self.velocity[1] > 0:
                        self.current_pos[1] = obstacle.y - self.radius
                    else:
                        self.current_pos[1] = obstacle.y + obstacle.height + self.radius
                    self.velocity[1] = 0  # Stop vertical movement

    def set_speed_multiplier(self, multiplier: int):
        self.speed_multiplier = multiplier
