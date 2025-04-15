import pygame
import random
import sys
import psycopg2
from config import load_conf

pygame.init()

WIDTH = 650
HEIGHT = 430
snake_size = 30
snake_width = WIDTH // snake_size
snake_height = HEIGHT // snake_size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake_game")

conn = psycopg2.connect(
    dbname='suppliers1',
    user='postgres',
    password='87087214958adiya',
    host='localhost'
)
cursor = conn.cursor()

PURPLE = (160, 32, 240)
PINK = ( 255, 102, 204)
RED = (255, 0, 0)
DPURPLE = (54, 1, 63)

class Snake:
    def __init__(self):
        self.body = [(snake_size // 2, snake_height // 2)]
        self.direction = (1, 0)
        self.player_name = None
        self.user_id = None
        self.paused = False

    def get_player_name(self):
        input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
        font = pygame.font.Font(None, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color(DPURPLE)
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.fill(PINK)
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()

        self.player_name = text

    def move(self):
        global score, speed, level
        if not self.paused:
            head = self.body[0]
            x = (head[0] + self.direction[0]) % snake_width
            y = (head[1] + self.direction[1]) % snake_height
            new_head = (x, y)
            if new_head in self.body[1:] or new_head in walls:
                return False
            self.body.insert(0, new_head)
            if new_head == food.position:
                score += 1
                if score % 5 == 0:
                    level += 1
                    speed += 1
                food.spawn()
            else:
                self.body.pop()
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.weight = 30
        self.timer = 0
        self.spawn()

    def spawn(self):
        while True:
            x = random.randint(0, snake_width - 1)
            y = random.randint(0, snake_height - 1)
            if (x, y) not in snake.body and (x, y) not in walls:
                self.position = (x, y)
                self.weight = self.weight
                self.timer = pygame.time.get_ticks() + 10000
                break

    def update(self):
        if pygame.time.get_ticks() - self.timer > 0:
            self.spawn()

def load_last_score(user_name):
    sql = """SELECT score, level FROM snake
             WHERE user_name = %s
             ORDER BY played_at DESC
             LIMIT 1;"""
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (user_name,))
            result = cur.fetchone()
            if result:
                return result
    except Exception as error:
        print("error", error)
    return (0, 0)

def insert_user(user_name, score, level):
    sql = """INSERT INTO snake(user_name, score, level)
             VALUES(%s, %s, %s);"""
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (user_name, score, level))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error", error)

walls = [(0, i) for i in range(snake_height)] + [(snake_width , i) for i in range(snake_height)] + \
        [(i, 0) for i in range(snake_width)] + [(i, snake_height) for i in range(snake_width)]

snake = Snake()
snake.get_player_name()
score, level = load_last_score(snake.player_name)
print(f"Player: {snake.player_name} | exist с: score={score}, level={level}")
food = Food()
speed = 5 + level

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(PINK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))
            elif event.key == pygame.K_SPACE:
                snake.paused = not snake.paused
            elif event.key == pygame.K_ESCAPE:
                running = False

    if not snake.move():
        running = False

    if not snake.paused:
        for segment in snake.body:
            pygame.draw.rect(screen, PURPLE, (segment[0] * snake_size, segment[1] * snake_size, snake_size, snake_size))

        x, y = food.position
        pygame.draw.rect(screen, RED, (x * snake_size, y * snake_size, food.weight, food.weight))

    font = pygame.font.SysFont(None, 25)
    text = font.render(f"score: {score}   level: {level}", True, PURPLE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    food.update()
    clock.tick(speed)

insert_user(snake.player_name, score, level)
pygame.quit()
conn.close()