import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 480))
pygame.display.set_caption("Music Player")

musics = [
    "images/mahabatym.mp3",
    "images/kelkel.mp3",
    "images/ИК.mp3"
]
images = [
    "images/moldanaz.png",
    "images/kelkel.jpeg",
    "images/IK.jpeg"
]

curr_music = 0

pygame.mixer.music.load(musics[curr_music])
img_ik = pygame.image.load(images[curr_music])
img_ik = pygame.transform.scale(img_ik, (400, 400))

image_play = pygame.image.load("images/play.png")
image_play = pygame.transform.scale(image_play, (400, 180))
image_pause = pygame.image.load("images/pause.png")
image_pause = pygame.transform.scale(image_pause, (140, 60))

music_run = False

def change_song(direction):
    global curr_music, music_run, img_ik

    if direction == "next":
        curr_music = (curr_music + 1) % len(musics)
    elif direction == "prev":
        curr_music = (curr_music - 1) % len(musics)

    pygame.mixer.music.load(musics[curr_music])
    img_ik = pygame.image.load(images[curr_music])
    img_ik = pygame.transform.scale(img_ik, (400, 400))

    if music_run:
        pygame.mixer.music.play()

flag = True
while flag:
    screen.blit(img_ik, (0, 0))
    screen.blit(image_play, (0, 300))

    if music_run:
        screen.blit(image_pause, (130, 360))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music_run:
                    pygame.mixer.music.pause()
                else:
                    if pygame.mixer.music.get_pos() > 0:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.play()

                music_run = not music_run

            elif event.key == pygame.K_RIGHT:
                change_song("next")

            elif event.key == pygame.K_LEFT:
                change_song("prev")
