from ball import Ball

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
            self.drag_line.append(self.current_pos)

            drag_distance = (
                (self.current_pos[0] - mouse_pos[0]) ** 2
                + (self.current_pos[1] - mouse_pos[1]) ** 2
            ) ** 0.5

            # Define minimum and maximum aiming line lengths
            min_aiming_line_length = 10  # Set your desired minimum length here
            max_aiming_line_length = 40  # Set your desired maximum length here

            if drag_distance < min_aiming_line_length:
                # Ensure minimum aiming line length
                drag_distance = min_aiming_line_length
            elif drag_distance > max_aiming_line_length:
                # Cap aiming line length to the maximum
                drag_distance = max_aiming_line_length

            drag_direction = [
                self.current_pos[0] - mouse_pos[0],
                self.current_pos[1] - mouse_pos[1],
            ]

            if drag_distance != 0:
                drag_direction = [i / drag_distance for i in drag_direction]
                # Calculate the velocity
                calculated_velocity = [
                    i * drag_distance * 0.05
                    for i in drag_direction
                ]

                self.velocity = calculated_velocity  # Update the ball's velocity
            else:
                self.velocity = [0, 0]

            self.dragging = False

        self.current_pos[0] += self.velocity[0] * 0.08
        self.current_pos[1] += self.velocity[1] * 0.08
        self.velocity[0] *= 0.99
        self.velocity[1] *= 0.99

    def handle_collision(self, screen_width, screen_height, obstacles):
        for obstacle in obstacles:
            if (
                self.current_pos[0] + self.radius >= obstacle.x - self.radius
                and self.current_pos[0] - self.radius
                <= obstacle.x + obstacle.width + self.radius
                and self.current_pos[1] + self.radius >= obstacle.y - self.radius
                and self.current_pos[1] - self.radius
                <= obstacle.y + obstacle.height + self.radius
            ):
                self.velocity = [0, 0]
                break 

    def set_speed_multiplier(self, multiplier: int):
        self.speed_multiplier = multiplier
