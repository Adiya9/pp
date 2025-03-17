import pygame
import datetime
import time

pygame.init()
per = pygame.time.Clock()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Micky clock")
icon = pygame.image.load("images/micky.jpeg")
pygame.display.set_icon(icon)

background = pygame.image.load("images/mainclock.png")
background = pygame.transform.scale(background,(700,500))

rhand = pygame.image.load("images/righthand.png")
lhand = pygame.image.load("images/lefthand.png")
x = 350
y = 250
hand_stay1 = rhand.get_rect(center=(x,y))
hand_stay2 = lhand.get_rect(center=(x,y))
lhand = pygame.transform.scale(lhand,(37,450))

flag = True
while flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            flag = False
            pygame.quit()

    time = datetime.datetime.now()
    minute_angle = -6 * time.minute
    second_angle = -6 * time.second
    rot_r = pygame.transform.rotate(rhand,minute_angle)
    rot_l = pygame.transform.rotate(lhand,second_angle)
    stay1 = rot_r.get_rect(center = (x,y))
    stay2 = rot_l.get_rect(center = (x,y))

    screen.blit(background, (0, 0))
    screen.blit(rot_r,stay1)
    screen.blit(rot_l,stay2)

    pygame.display.update()
    per.tick(60)
