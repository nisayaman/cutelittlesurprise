import pygame

# Specify the name and path of the music file
music_file = "Maxwell The Cat Theme.mp3"

# Initialize pygame
pygame.init()

# Load the music
pygame.mixer.music.load(music_file)

# Start playing the music
pygame.mixer.music.play()

# Keep the program running until the music finishes (can be exited with Ctrl+C)
while True:
    pass
