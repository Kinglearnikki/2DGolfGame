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

    def set_speed_multiplier(self, multiplier: int):
        self.speed_multiplier = multiplier
