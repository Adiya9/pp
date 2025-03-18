import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Red Ball")

pos_x = 25
pos_y = 25
radius = 25

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pos_x += 20
            elif event.key == pygame.K_LEFT:
                pos_x -= 20
            elif event.key == pygame.K_UP:
                pos_y -= 20
            elif event.key == pygame.K_DOWN:
                pos_y += 20

    pos_x = max(radius, min(500 - radius, pos_x))
    pos_y = max(radius, min(500 - radius, pos_y))

    screen.fill("pink")

    pygame.draw.circle(screen, "red", (pos_x, pos_y), radius)

    pygame.display.update()
