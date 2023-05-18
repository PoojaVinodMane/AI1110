import pygame
import os
import random

# Initialize 
pygame.init()
pygame.mixer.init()

# Directory containing the audio files
audio_directory = "audio_files/"

audio_files = os.listdir(audio_directory)
audio_files = ["1.mp3",
    "2.mp3",
    "3.mp3",
    "4.mp3",
    "5.mp3",
    "6.mp3",
    "7.mp3",
    "8.mp3",
    "9.mp3",
    "10.mp3",
    "11.mp3",
    "12.mp3",
    "13.mp3",
    "14.mp3",
    "15.mp3",
    "16.mp3",
    "17.mp3",
    "18.mp3",
    "19.mp3",
    "20.mp3"]
    
# Randomly shuffle the audio files
random.shuffle(audio_files)

# Create a Pygame window
window_width, window_height = 400, 200
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Random Playlist")

# Load the first audio file
index = 0
current_file = os.path.join(audio_directory, audio_files[index])
pygame.mixer.music.load(current_file)

# Play the audio file
pygame.mixer.music.play()
print(current_file)

# Game loop
running = True
paused = False
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                index = (index + 1) % len(audio_files)
                current_file = os.path.join(audio_directory, audio_files[index])
                pygame.mixer.music.load(current_file)
                pygame.mixer.music.play()
                print(current_file)
                paused = False

            if event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                index = (index - 1) % len(audio_files)
                current_file = os.path.join(audio_directory, audio_files[index])
                pygame.mixer.music.load(current_file)
                pygame.mixer.music.play()
                print(current_file)
                paused = False

    # Clear the window
    window.fill((230, 230, 250))

    # Render text on the window
    font = pygame.font.Font(None, 36)
    text = font.render("Press Space to Pause/Play", True, (0, 0, 0))
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(text, text_rect)

    # Update the window display
    pygame.display.flip()
    
    
pygame.quit()


