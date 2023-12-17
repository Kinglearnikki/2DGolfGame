import pygame


class BackButton:
    def __init__(self, x, y, width, height, color, text, text_color):
        self.rect = pygame.Rect(x, y, width, height)
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

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    # def back_to_main(self, game_state):
    #     if pygame.mouse.get_pressed()[0]:
    #         game_state="scoreboard"
            
    # def back_to_main(self, game_state, mouse_pos):
    #     if pygame.mouse.get_pressed()[0] and self.is_clicked(mouse_pos):
    #         game_state.change_state("scoreboard")
            

    # back_button_font = pygame.font.Font(None, 30)
    #     back_button_text = back_button_font.render("Back", True, (255, 255, 255))
    #     back_button_rect = back_button_text.get_rect()
    #     back_button_rect.x = 50
    #     back_button_rect.y = height - 60
    #     pygame.draw.rect(
    #         screen, (0, 128, 255), back_button_rect.inflate(20, 20)
    #     )  # Blue button
    #     screen.blit(back_button_text, back_button_rect)

    #     pygame.display.flip()

    #     # Handle events for the "Back" button
    #     running = True
    #     while running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False
    #                 pygame.quit()
    #                 sys.exit()
    #             elif event.type == pygame.MOUSEBUTTONDOWN:
    #                 mouse_pos = event.pos
    #                 if back_button_rect.inflate(20, 20).collidepoint(mouse_pos):
    #                     self.state = "intro"
    #                     running = False



    # mouse_pos = pygame.mouse.get_pos()
    #         if mainMenu_button.is_clicked(mouse_pos):
    #             game_state.change_state("main_menu")