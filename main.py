import pygame
import os
from ball import Ball
from button import Button
from hole import Hole

pygame.init()

# Set window dimensions
width = 800
height = 600

# Get current directory
current_directory = os.getcwd()

# Set image path
image_path = os.path.join(current_directory, "images", "bg.png")


# Reset ball function
def resetBall():
    ball.x = width // 2
    ball.y = height // 2
    ball.current_pos = [ball.x, ball.y]
    ball.velocity = [0, 0]
    ball.drag_line = []


# Create screen
screen = pygame.display.set_mode((width, height))

# Load and resize background image
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (width, height))

# Set window caption
pygame.display.set_caption("2dGolf")

# Create ball object
ball = Ball(width // 2, height // 2, 20, (255, 255, 255))

# Create font object
font = pygame.font.Font(None, 30)

# Set running flag
running = True

# Create reset button object
reset_button = Button(10, 10, 100, 50, (0, 255, 0), "Reset", (255, 255, 255))

# Create hole object
hole = Hole(396, 80, 25, (0, 0, 0))

# Initialize hole message and success message
hole_message = ""
success_message = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (
                ball.velocity[0] ** 2 + ball.velocity[1] ** 2 < 1
                and ball.dragging is False
                and (ball.current_pos[0] - event.pos[0]) ** 2
                + (ball.current_pos[1] - event.pos[1]) ** 2
                <= ball.radius**2
            ):
                ball.dragging = True
                ball.drag_line = [ball.current_pos]

            reset_button.handle_click(pygame.mouse.get_pos(), reset_ball=resetBall)

        elif event.type == pygame.MOUSEBUTTONUP:
            if (
                ball.dragging
                and ball.velocity[0] ** 2 + ball.velocity[1] ** 2 < 0.01**2
                and (ball.current_pos[0] - event.pos[0]) ** 2
                + (ball.current_pos[1] - event.pos[1]) ** 2
                > ball.radius**2
            ):
                ball.handle_release(pygame.mouse.get_pos())
            ball.dragging = False

    if ball.dragging:
        ball.drag_line.append(pygame.mouse.get_pos())

    if ball.velocity != [0, 0]:
        ball.dragging = False

    if ball.drag_line:
        for start, end in zip(ball.drag_line, ball.drag_line[1:]):
            pygame.draw.line(screen, (0, 0, 0), start, end, 5)

    screen.blit(image, (0, 0))

    ball.update_position(screen=screen, width=width, height=height)

    distance_to_hole = (
        (ball.current_pos[0] - hole.x) ** 2 + (ball.current_pos[1] - hole.y) ** 2
    ) ** 0.5

    if distance_to_hole <= hole.radius:
        if distance_to_hole + ball.radius <= hole.radius:
            hole_message = "Ball in hole!"
            success_message = "Congrats!"
            ball.velocity = [0, 0]
        else:
            hole_message = "Ball partly in hole!"
    else:
        hole_message = ""
        success_message = ""

    hole.draw(screen)
    ball.draw(screen)
    reset_button.draw(screen)

    hole_text = font.render(hole_message, True, (255, 255, 255))
    hole_text_rect = hole_text.get_rect(bottomleft=(10, height - 10))
    screen.blit(hole_text, hole_text_rect)

    success_text = font.render(success_message, True, (255, 0, 0))
    success_text_rect = success_text.get_rect(centerx=width // 2, bottom=height - 10)
    screen.blit(success_text, success_text_rect)

    mouse_pos_text = font.render(
        f"Mouse Position: {pygame.mouse.get_pos()}", True, (255, 255, 255)
    )
    mouse_pos_rect = mouse_pos_text.get_rect(bottomleft=(10, height - 40))
    screen.blit(mouse_pos_text, mouse_pos_rect)

    velocity_text = font.render(f"Velocity: {ball.velocity}", True, (255, 255, 255))
    velocity_text_rect = velocity_text.get_rect(bottomright=(width - 10, height - 10))
    screen.blit(velocity_text, velocity_text_rect)

    pygame.display.flip()

pygame.quit()
