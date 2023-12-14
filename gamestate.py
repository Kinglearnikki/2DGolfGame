import pygame
import sys
import os
import time
from obstacles import Obstacle

class GameState:
    def __init__(self):
        self.state = 'intro'
        self.ball_hit = False
        self.ball_stopped = True
        self.ball_was_hit = False
        self.hole_message = ""
        self.success_message = ""
        self.total_strokes = 0  # Change to instance variable
        self.timer_running = False
        self.start_time = 0
        self.elapsed_time = 0
    
    def start_timer(self):
        self.timer_running = True
        self.start_time = time.time()

    def stop_timer(self):
        self.timer_running = False
        self.elapsed_time = time.time() - self.start_time

    def update_timer(self):
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time

    def intro(self, screen, width, height):
        # Set image path
        current_directory = os.getcwd()
        image_path = os.path.join(current_directory, "images", "bg.png")

        # Load and resize background image
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (width, height))

        # Set background color or image for the intro screen
        screen.blit(image, (0, 0))
        
        # Display the title
        title_font = pygame.font.SysFont("arial", 100) #(font, size)
        title_text = title_font.render("2D Golf Game", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(width // 2, height // 3 - 50))
        screen.blit(title_text, title_rect)

        # Create a button
        button_font = pygame.font.Font(None, 30)
        button_rect = pygame.Rect(width // 2 - 50, height // 2 + 20, 100, 40)
        pygame.draw.rect(screen, (0, 128, 255), button_rect)  # Blue button
        button_text = button_font.render("Start Game", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)

        # Create the "Scoreboard" button below the current button
        scoreboard_rect = pygame.Rect(width // 2 - 50, height // 2 + 80, 100, 40)
        pygame.draw.rect(screen, (0, 128, 255), scoreboard_rect)  # Blue button
        scoreboard_text = button_font.render("Scoreboard", True, (255, 255, 255))
        scoreboard_text_rect = scoreboard_text.get_rect(center=scoreboard_rect.center)
        screen.blit(scoreboard_text, scoreboard_text_rect)

        # Check for button click
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.state = 'main_game'

        # Update the display
        pygame.display.flip()

    def main_game(self, ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball):

        # Set image path
        current_directory = os.getcwd()
        image_path = os.path.join(current_directory, "images", "bg.png")

        # Load and resize background image
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (width, height))
        button_font = pygame.font.Font(None, 30)

        # Your main game code here
        if ball.dragging:
            ball.drag_line.append(pygame.mouse.get_pos())

        if ball.speed != [0, 0]:
            ball.dragging = False
            ball.drag_line = []

        if ball.drag_line:
            for start, end in zip(ball.drag_line, ball.drag_line[1:]):
                pygame.draw.line(screen, (0, 0, 0), start, end, 5)

        for obstacle in obstacles:
            if (
                ball.current_pos[0] + ball.radius >= obstacle.x
                and ball.current_pos[0] - ball.radius <= obstacle.x + obstacle.width
                and ball.current_pos[1] + ball.radius >= obstacle.y
                and ball.current_pos[1] - ball.radius <= obstacle.y + obstacle.height
            ):
                # Adjust position based on collision with obstacle's edges
                ball.adjust_position(obstacle)

                # Reverse speed components based on the collision
                ball.reverse_speed(obstacle)

                if hasattr(ball, 'special_attribute'):
                    if ball.special_attribute == "Sticky":
                        ball.handle_collision(screen_width=width, screen_height=height, obstacles=obstacles)

        # Blit the image onto the screen
        screen.blit(image, (0, 0))

        self.update_timer()
        if self.timer_running or self.elapsed_time > 0:
            timer_text = font.render(
                f"Time: {int(self.elapsed_time)}s", True, (255, 255, 255)
            )
            timer_text_rect = timer_text.get_rect(topright=(width - 10, 30))
            screen.blit(timer_text, timer_text_rect)

        # Update ball's position and check for collisions
        ball.update_position(screen=screen, width=width, height=height)

        hole.draw(screen)
        ball.draw(screen)
        reset_button.draw(screen)

        for obstacle in obstacles:
            obstacle.draw(screen, pygame=pygame)
        
        distance_to_hole = (
            (ball.current_pos[0] - hole.x) ** 2 + (ball.current_pos[1] - hole.y) ** 2
        ) ** 0.5

        if distance_to_hole <= hole.radius:
            if distance_to_hole + ball.radius <= hole.radius:
                self.hole_message = "Ball in hole!"
                self.success_message = "Congrats!"
                ball.speed = [0, 0]

                # Increment the total strokes only for the first successful hit
                if not self.ball_hit:
                    self.stop_timer()
                    self.total_strokes += 1
                    self.ball_hit = True

                # Display the next level button
                next_level_button_rect = pygame.Rect(width // 2 - 50, height // 2 + 70, 100, 40)
                pygame.draw.rect(screen, (0, 128, 255), next_level_button_rect)  # Blue button
                next_level_text = button_font.render("Next Level", True, (255, 255, 255))
                next_level_text_rect = next_level_text.get_rect(center=next_level_button_rect.center)
                screen.blit(next_level_text, next_level_text_rect)

                # Check for button click to go to the next level
                mouse_pos = pygame.mouse.get_pos()
                if next_level_button_rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        # Reset ball position
                        ball.reset_position()
                        
                        # Go to the next level
                        if self.state == 'main_game':
                            self.state = 'level_1'
                        elif self.state == 'level_1':
                            self.state = 'level_2'
                        elif self.state == 'level_2':
                            self.state = 'level_3'
                        elif self.state == 'level_3':
                            # You can add logic for game completion or loop back to the first level
                            self.state = 'intro'

                        # Reset ball and other relevant parameters for the new level
                        self.ball_hit = False
                        self.ball_was_hit = False
                        self.hole_message = ""
                        self.success_message = ""
                        self.total_strokes = 0

            else:
                self.hole_message = "Ball partly in hole"
        else:
            self.hole_message = ""
            self.success_message = ""      

        hole_text = font.render(self.hole_message, True, (255, 255, 255))
        hole_text_rect = hole_text.get_rect(bottomleft=(10, height - 10))
        screen.blit(hole_text, hole_text_rect)

        success_text = font.render(self.success_message, True, (255, 0, 0))
        success_text_rect = success_text.get_rect(centerx=width // 2, bottom=height - 10)
        screen.blit(success_text, success_text_rect)

        # Display stroke counter
        total_strokes_text = font.render(
            f"Total Strokes: {self.total_strokes}", True, (255, 255, 255)
        )
        total_strokes_text_rect = total_strokes_text.get_rect(topright=(width - 10, 10))
        screen.blit(total_strokes_text, total_strokes_text_rect)

        mouse_pos_text = font.render(
            f"Mouse Position: {pygame.mouse.get_pos()}", True, (255, 255, 255)
        )
        mouse_pos_rect = mouse_pos_text.get_rect(bottomleft=(10, height - 40))
        screen.blit(mouse_pos_text, mouse_pos_rect)

        speed_text = font.render(f"speed: {ball.speed}", True, (255, 255, 255))
        speed_text_rect = speed_text.get_rect(bottomright=(width - 10, height - 10))
        screen.blit(speed_text, speed_text_rect)

        # Update the display
        pygame.display.flip() 
    
    def level_1(self, ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball):
        # Level 1 specific code (obstacles, hole position, ball position)

        obstacles.clear()  # Remove existing obstacles
        obstacles.append(Obstacle(300, 180, 200, 10, (0, 0, 0), orientation="vertical"))
        obstacles.append(Obstacle(300, 400, 200, 10, (0, 0, 0), orientation="vertical"))
        obstacles.append(Obstacle(300, 180, 200, 10, (0, 0, 0), orientation="horizontal"))

        # Call the common main_game method
        self.main_game(ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball)

    def level_2(self, ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball):
        # Level 2 specific code (obstacles, hole position, ball position)

        obstacles.clear()  # Remove existing obstacles
        obstacles.append(Obstacle(300, 180, 200, 10, (0, 0, 0), orientation="vertical"))
        obstacles.append(Obstacle(300, 400, 200, 10, (0, 0, 0), orientation="vertical"))
        obstacles.append(Obstacle(500, 188, 200, 10, (0, 0, 0), orientation="horizontal"))

        # Call the common main_game method
        self.main_game(ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball)

    def level_3(self, ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball):
        # Level 3 specific code (obstacles, hole position, ball position)

        obstacles.clear()  # Remove existing obstacles
        obstacles.append(Obstacle(300, 180, 200, 10, (0, 0, 0), orientation="vertical"))
        obstacles.append(Obstacle(300, 188, 200, 10, (0, 0, 0), orientation="horizontal"))
        obstacles.append(Obstacle(500, 188, 200, 10, (0, 0, 0), orientation="horizontal"))

        # Call the common main_game method
        self.main_game(ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball)

    def handle_mouse_button_down(self, event, ball, reset_button, reset_ball):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (
                ball.speed[0] ** 2 + ball.speed[1] ** 2 < 1
                and ball.dragging is False
                and (ball.current_pos[0] - event.pos[0]) ** 2
                + (ball.current_pos[1] - event.pos[1]) ** 2
                <= ball.radius**2
            ):
                ball.dragging = True
                ball.drag_line = [ball.current_pos]
                self.ball_was_hit = True

            reset_button.handle_click(pygame.mouse.get_pos(), reset_ball=reset_ball)
    
    def handle_mouse_button_up(self, event, ball):
        if event.type == pygame.MOUSEBUTTONUP:
            if (
                ball.dragging
                and ball.speed[0] ** 2 + ball.speed[1] ** 2 < 0.01**2
                and (ball.current_pos[0] - event.pos[0]) ** 2
                + (ball.current_pos[1] - event.pos[1]) ** 2
                > ball.radius**2
            ):
                if not self.timer_running:
                    self.start_timer()
                ball.handle_release(pygame.mouse.get_pos())
            
            ball.dragging = False

            if (
                self.ball_was_hit and ball.drag_line
            ):
                self.total_strokes += 1
                self.ball_was_hit = False

    def state_manager(self, ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball):
        if self.state == 'intro':
            self.intro(screen, width, height)
        elif self.state == 'main_game':
            self.main_game(ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball)
        elif self.state == 'level_1':
            self.level_1(ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball)
        elif self.state == 'level_2':
            self.level_2(ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball)
        elif self.state == 'level_3':
            self.level_3(ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball)
        else:
            print("Invalid state:", self.state)
            sys.exit()
