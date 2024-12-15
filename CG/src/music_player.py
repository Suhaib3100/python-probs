import pygame.mixer

# Initialize pygame mixer for audio playback
pygame.mixer.init()

def play_music(emotion):
    if emotion == "happy":
        pygame.mixer.music.load("assets/happy_music.mp3")
    elif emotion == "sad":
        pygame.mixer.music.load("assets/sad_music.mp3")
    else:
        pygame.mixer.music.load("assets/neutral_music.mp3")
    pygame.mixer.music.play(-1, 0.0)  # Loop the music

def stop_music():
    pygame.mixer.music.stop()
