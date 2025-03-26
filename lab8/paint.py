import pygame

pygame.init()

WIDTH = 800
HEIGHT =  600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
ERASER_COLOR = WHITE

radius = 5
mode = 'pen'
color = BLACK
draw = False
start = None
def clear_screen():
    screen.fill(WHITE)

clear_screen()

button_rects = {
    "Red": pygame.Rect(10, 10, 50, 30),
    "Green": pygame.Rect(70, 10, 50, 30),
    "Blue": pygame.Rect(130, 10, 50, 30),
    "Eraser": pygame.Rect(190, 10, 80, 30),
    "Circle": pygame.Rect(280, 10, 80, 30),
    "Rect": pygame.Rect(370, 10, 80, 30),
    "Clear": pygame.Rect(460, 10, 80, 30),
}

def draw_buttons():
    for text, rect in button_rects.items():
        pygame.draw.rect(screen, BLACK, rect, 2)
        font = pygame.font.Font(None, 20)
        label = font.render(text, True, BLACK)
        screen.blit(label, (rect.x + 10, rect.y + 5))

flag = True
while flag:
    draw_buttons()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for text, rect in button_rects.items():
                    if rect.collidepoint(event.pos):
                        if text == "Red":
                            color = RED
                            mode = 'pen'
                        elif text == "Green":
                            color = GREEN
                            mode = 'pen'
                        elif text == "Blue":
                            color = BLUE
                            mode = 'pen'
                        elif text == "Eraser":
                            mode = 'eraser'
                        elif text == "Circle":
                            mode = 'circle'
                        elif text == "Rect":
                            mode = 'rectangle'
                        elif text == "Clear":
                            clear_screen()
                start = event.pos
                draw = True

        if event.type == pygame.MOUSEBUTTONUP:
            if mode in ['rectangle', 'circle'] and start:
                end_pos = event.pos
                if mode == 'rectangle':
                    pygame.draw.rect(screen, color, (*start, end_pos[0] - start[0], end_pos[1] - start[1]), 2)
                elif mode == 'circle':
                    radius = max(abs(end_pos[0] - start[0]), abs(end_pos[1] - start[1])) // 2
                    center = ((start[0] + end_pos[0]) // 2, (start[1] + end_pos[1]) // 2)
                    pygame.draw.circle(screen, color, center, radius, 2)
            drawing = False

        if event.type == pygame.MOUSEMOTION and draw:
            x, y = event.pos
            if mode == 'pen':
                pygame.draw.circle(screen, color, (x, y), radius)
            elif mode == 'eraser':
                pygame.draw.circle(screen, ERASER_COLOR, (x, y), radius)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
                mode = 'pen'
            elif event.key == pygame.K_g:
                color = GREEN
                mode = 'pen'
            elif event.key == pygame.K_b:
                color = BLUE
                mode = 'pen'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_t:
                mode = 'rectangle'
            elif event.key == pygame.K_SPACE:
                clear_screen()
            elif event.key == pygame.K_UP:
                radius = min(50, radius + 2)
            elif event.key == pygame.K_DOWN:
                radius = max(1, radius - 2)

