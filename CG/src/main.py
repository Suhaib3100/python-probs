import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from opengl_utils import *

# Initialize pygame
pygame.init()
pygame.font.init()

# Set up the display window
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)

# Set up OpenGL settings
glClearColor(0, 0, 0, 1)  # Set background color to black
glEnable(GL_DEPTH_TEST)

# Main loop to run the screens
def main():
    running = True
    screen_state = "title"  # Track the current screen state

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Handle different screen states
        if screen_state == "title":
            render_title_screen()
        elif screen_state == "emotion":
            render_emotion_detection_screen()
        elif screen_state == "music":
            render_music_player_screen()

        # Update the screen
        pygame.display.flip()

        # Handle keyboard inputs to switch screens (for example)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            screen_state = "title"
        elif keys[pygame.K_2]:
            screen_state = "emotion"
        elif keys[pygame.K_3]:
            screen_state = "music"

    pygame.quit()

if __name__ == "__main__":
    main()
