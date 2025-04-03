import pygame
import os


pygame.mixer.init()
pygame.init()


MUSIC_FOLDER = "C:/Users/quant/Desktop/pygame/music"


playlist = [os.path.join(MUSIC_FOLDER, f) for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]


current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

play_music()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill((30, 30, 30))
    

    track_name = os.path.basename(playlist[current_track])
    text_surface = font.render(f"Now Playing: {track_name}", True, (255, 255, 255))
    screen.blit(text_surface, (50, 50))

    controls_text = font.render("SPACE: Play/Pause | S: Stop | N: Next | P: Previous", True, (200, 200, 200))
    screen.blit(controls_text, (50, 100))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()

pygame.quit()
