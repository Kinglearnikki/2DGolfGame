class Obstacle:
    def __init__(self, x, y, width, height, color, orientation="vertical"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.orientation = orientation

    def draw(self, screen, pygame): 
        if self.orientation == "vertical":
            pygame.draw.rect(
                screen, self.color, (self.x, self.y, self.width, self.height)
            )
        elif self.orientation == "horizontal":
            pygame.draw.rect(
                screen, self.color, (self.x, self.y, self.height, self.width)
            )
