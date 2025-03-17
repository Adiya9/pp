import pygame

pygame.init()
screen = pygame.display.set_mode((500,700))
caption = pygame.display.set_caption("red ball")
pos_x = 30
pos_y = 30


flag = True
while flag:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            flag = False
            pygame.quit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                pos_x += 20
            elif i.key == pygame.K_LEFT:
                pos_x -= 20
            elif i.key == pygame.K_UP:
                pos_y -= 20
            elif i.key == pygame.K_DOWN:
                pos_y += 20
    screen.fill('pink')
    ball = pygame.draw.circle(screen, "red", (pos_x, pos_y), 25)
    pygame.display.update()



