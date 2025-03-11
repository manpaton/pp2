import pygame
import os

pygame.init()
pygame.mixer.init()


music_folder = "music"  
playlist = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0
volume = 0.2 

if not playlist:
    print("Нет музыкальных файлов в папке 'music'.")
    exit()

def play_music():
    pygame.mixer.music.load(os.path.join(music_folder, playlist[current_track]))
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

def change_volume(delta):
    global volume
    volume = max(0.0, min(1.0, volume + delta)) 
    pygame.mixer.music.set_volume(volume)

play_music()

# Создаем окно
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")
background = pygame.image.load("tvgirl.jpg")
background = pygame.transform.scale(background, (400, 300))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0)) 
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
            elif event.key == pygame.K_n or event.key == pygame.K_LEFT: 
                next_track()
            elif event.key == pygame.K_p or event.key == pygame.K_RIGHT: 
                prev_track()
            elif event.key == pygame.K_UP: 
                change_volume(0.1)
            elif event.key == pygame.K_DOWN:  
                change_volume(-0.1)

pygame.quit()