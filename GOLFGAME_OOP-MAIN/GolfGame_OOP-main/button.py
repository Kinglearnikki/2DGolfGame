import pygame


class Button:
    def __init__(self, x, y, width, height, color, text, text_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2)
        )
        screen.blit(text, text_rect)

    def handle_click(self, mouse_pos, reset_ball):
        if (self.x <= mouse_pos[0] <= self.x + self.width) and (
            self.y <= mouse_pos[1] <= self.y + self.height
        ):
            reset_ball()
