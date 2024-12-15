import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize fonts
font = pygame.font.SysFont("arial", 24)

# Function to draw text
def draw_text(text, x, y, font, color=(1, 1, 1)):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen = pygame.display.get_surface()
    screen.blit(text_surface, text_rect)

# Render Title Screen
def render_title_screen():
    glLoadIdentity()
    draw_text("Face Emotion Detector Music Player", 250, 300, font, color=(1, 1, 1))
    draw_text("Project by: Your Name - Roll Number", 250, 250, font, color=(1, 1, 1))
    draw_text("Guide: Your Guide Name", 250, 200, font, color=(1, 1, 1))

# Render Emotion Detection Screen
def render_emotion_detection_screen():
    glLoadIdentity()
    draw_text("Start Emotion Detection", 250, 300, font, color=(1, 1, 1))

# Render Music Player Screen
def render_music_player_screen():
    glLoadIdentity()
    draw_text("Now Playing Music Based on Emotion", 250, 300, font, color=(1, 1, 1))
