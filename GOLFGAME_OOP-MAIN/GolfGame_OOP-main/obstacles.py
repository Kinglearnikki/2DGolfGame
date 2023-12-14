class Obstacle:
    def __init__(self, x, y, width, height, color, orientation):
        self.x = x
        self.y = y
        self.color = color
        self.orientation = orientation

        if(self.orientation == "vertical"):
            self.width = width
            self.height = height
        elif(self.orientation == "horizontal"):
            self.width = height
            self.height = width

    def draw(self, screen, pygame):  
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


    def calculate_corner_positions(self):
        x, y, width, height = self.x, self.y, self.width, self.height

        top_left = (x, y)
        top_right = (x + width, y)
        bottom_left = (x, y + height)
        bottom_right = (x + width, y + height)

        return top_left, top_right, bottom_left, bottom_right
