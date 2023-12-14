import pygame
import os
from ball import Ball
from button import Button
from hole import Hole
from obstacles import Obstacle
from gamestate import GameState
from stickyball import StickyBall
from normalBall import NormalBall

# from slipperyball import SlipperyBall

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
ball = NormalBall(width // 2, height // 2, 20, (255, 255, 255), 1)


# Reset ball function
def resetball(game_state):
    ball.x = width // 2
    ball.y = height // 2
    ball.current_pos = [ball.x, ball.y]
    ball.speed = [0, 0]
    ball.drag_line = []

    game_state.reset_strokes()


reset_ball = resetball

# Create hole object
hole = Hole(396, 80, 25, (0, 0, 0))

# Create obstacles
obstacles = [
    Obstacle(130, 290, 50, 100, (0, 0, 0), orientation="vertical"),
    Obstacle(400, 400, 50, 100, (0, 0, 0), orientation="horizontal")
    # Add more obstacles here as needed
]

# Create reset button object
reset_button = Button(10, 10, 100, 50, (0, 255, 0), "Reset", (255, 255, 255))

# Set game state
game_state = GameState()

# Set running flag
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse button down event
            game_state.handle_mouse_button_down(
                event, ball, reset_button, reset_ball, game_state
            )
        elif event.type == pygame.MOUSEBUTTONUP:
            # Handle mouse button up event
            game_state.handle_mouse_button_up(event, ball)

    game_state.state_manager(
        ball, obstacles, screen, hole, reset_button, font, width, height, reset_ball
    )

    pygame.display.flip()

pygame.quit()
