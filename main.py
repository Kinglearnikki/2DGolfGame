import pygame
import os
from ball import Ball
from button import Button
from hole import Hole
from obstacles import Obstacle
from gamestate import GameState
from stickyball import StickyBall
from normalBall import NormalBall
from bigball import BigBall

# Pygame initialization
pygame.init()

# Set window dimensions
width, height = 800, 600

# Get current directory
current_directory = os.getcwd()

# Set image path
image_path = os.path.join(current_directory, "images", "bg.png")

# Create screen
screen = pygame.display.set_mode((width, height))

# Load and resize background image
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (width, height))

# Set window caption
pygame.display.set_caption("2dGolf")

# Create font object
font = pygame.font.Font(None, 30)

# Create ball object
ball_main_game = NormalBall(width // 2, height // 2, 10, "golfball.png", 1)
ball_level1 = StickyBall(width // 2, height // 2, 10, "slimeball.png", "attribute_2", 1)
ball_level2 = BigBall(width // 2, height // 2, 20, "golfball.png", 1)
ball_level3 = StickyBall(width // 2, height // 2, 10, "slimeball.png", "attribute_4", 1)

# Function to reset ball for different levels
def reset_ball(game_state, ball):
    ball.x = width // 2
    ball.y = height // 2
    ball.current_pos = [ball.x, ball.y]
    ball.speed = [0, 0]
    ball.drag_line = []
    game_state.reset_strokes()

# Reset functions for different levels
reset_ball_main_game = lambda: reset_ball(game_state, ball_main_game)
reset_ball_level1 = lambda:  reset_ball(game_state, ball_level1)
reset_ball_level2 = lambda:  reset_ball(game_state, ball_level2)
reset_ball_level3 = lambda:  reset_ball(game_state, ball_level3)

# Create hole object
hole = Hole(396, 80, 25, (0, 0, 0))

# Create obstacles
obstacles = [
    Obstacle(130, 290, 50, 100, (0, 0, 0), orientation="vertical"),
    Obstacle(400, 400, 50, 100, (0, 0, 0), orientation="horizontal")
]

# Create reset button object
reset_button = Button(10, 10, 100, 50, (0, 255, 0), "Reset", (255, 255, 255))

# Set game state
game_state = GameState()
game_state.state = "intro"

# Set running flag
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state.state == "intro":
                game_state.handle_mouse_button_down(event)
            elif game_state.state == "main_game":
                game_state.handle_mouse_button_down(
                event, ball_main_game, reset_button, reset_ball_main_game,
            )
            elif game_state.state == "level_1":
                game_state.handle_mouse_button_down(
                event, ball_level1, reset_button, reset_ball_level1,
            )
            elif game_state.state == "level_2":
                game_state.handle_mouse_button_down(
                event, ball_level2, reset_button, reset_ball_level2,
            )
            elif game_state.state == "level_3":
                game_state.handle_mouse_button_down(
                event, ball_level3, reset_button, reset_ball_level3,
            )
        elif event.type == pygame.MOUSEBUTTONUP:
            if game_state.state == "main_game":
                game_state.handle_mouse_button_up(event, ball_main_game)
            elif game_state.state == "level_1":
                game_state.handle_mouse_button_up(event, ball_level1)
            elif game_state.state == "level_2":
                game_state.handle_mouse_button_up(event, ball_level2)
            elif game_state.state == "level_3":
                game_state.handle_mouse_button_up(event, ball_level3)

    if game_state.state == "intro":
        game_state.intro(screen, width, height, font)
    elif game_state.state == "main_game":
        game_state.state_manager(
            ball_main_game, obstacles, screen, hole, reset_button, font, width, height, reset_ball_main_game
        )
    elif game_state.state == "level_1":
        game_state.state_manager(
            ball_level1, obstacles, screen, hole, reset_button, font, width, height, reset_ball_level1
        )
    elif game_state.state == "level_2":
        game_state.state_manager(
            ball_level2, obstacles, screen, hole, reset_button, font, width, height, reset_ball_level2
        )
    elif game_state.state == "level_3":
        game_state.state_manager(
            ball_level3, obstacles, screen, hole, reset_button, font, width, height, reset_ball_level3
        )

    pygame.display.flip()

pygame.quit()