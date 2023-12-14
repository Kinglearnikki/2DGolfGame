import pygame


class Ball:
    def __init__(self, x: int, y: int, radius: int, color: tuple):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = [0, 0]
        self.current_pos = [x, y]
        self.dragging = False
        self.drag_line = []

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.current_pos[0]), int(self.current_pos[1])),
            self.radius,
        )

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

    def update_position(self, screen, width, height):
        if self.dragging:
            if not self.drag_line:
                self.drag_line.append(self.current_pos)

            if self.drag_line:
                pygame.draw.line(
                    screen, (0, 0, 0), self.drag_line[0], pygame.mouse.get_pos(), 5
                )

        self.current_pos[0] += self.velocity[0] * 0.08 
        self.current_pos[1] += self.velocity[1] * 0.08  
        self.velocity[0] *= 0.99  
        self.velocity[1] *= 0.99 

        if self.velocity[0] ** 2 + self.velocity[1] ** 2 < 0.01**2:
            self.velocity = [0, 0]

        if self.current_pos[0] - self.radius <= 0:
            self.current_pos[0] = self.radius 
            self.velocity[0] *= -1 
        elif self.current_pos[0] + self.radius >= width:
            self.current_pos[0] = (
                width - self.radius
            )
            self.velocity[0] *= -1 

        if self.current_pos[1] - self.radius <= 0:
            self.current_pos[1] = self.radius
            self.velocity[1] *= -1 
        elif self.current_pos[1] + self.radius >= height:
            self.current_pos[1] = (
                height - self.radius
            )  
            self.velocity[1] *= -1 
