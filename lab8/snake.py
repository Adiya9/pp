import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

font = pygame.font.Font(None, 25)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
WHITE = (255, 255, 255)

BLOCK_SIZE = 20
SPEED = 5

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

class SnakeGame:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h

        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.direction = Direction.RIGHT
        self.head = Point(self.w // 2, self.h // 2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)
        ]

        self.score = 0
        self.level = 1
        self.speed = SPEED

        self.food = None
        self._place_food()

    def _place_food(self):
        while True:
            x = random.randint(0, (self.w // BLOCK_SIZE) - 1) * BLOCK_SIZE
            y = random.randint(0, (self.h // BLOCK_SIZE) - 1) * BLOCK_SIZE
            self.food = Point(x, y)
            if self.food not in self.snake:
                break

    def play_step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN

        self._move(self.direction)
        self.snake.insert(0, self.head)

        if self._is_collision():
            return True, self.score

        if self.head == self.food:
            self.score += 1
            self._place_food()
            self._update_speed()
        else:
            self.snake.pop()

        self._update_ui()
        self.clock.tick(self.speed)

        return False, self.score

    def _is_collision(self):
        if self.head.x < 0 or self.head.x >= self.w or self.head.y < 0 or self.head.y >= self.h:
            return True

        if self.head in self.snake[1:]:
            return True

        return False

    def _move(self, direction):
        x = self.head.x
        y = self.head.y

        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE

        self.head = Point(x, y)

    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render(f"Score: {self.score}  Level: {self.level}", True, WHITE)
        self.display.blit(text, [10, 10])

        pygame.display.flip()

    def _update_speed(self):
        if self.score % 3 == 0:
            self.level += 1
            self.speed += 1


if __name__ == '__main__':
    game = SnakeGame()

    while True:
        game_over, score = game.play_step()
        if game_over:
            break

    print(f'Final Score: {score}')
    pygame.quit()
