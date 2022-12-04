import pygame
import random
from settings import *
from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.orientation = 0
        self.paused = False
        self.score = 0
        self.still_playing = True

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.head = Snake(self, 10, 10)
        self.snake_body = []
        self.snake_body.append(Snake(self, 9, 10))
        self.snake_body.append(Snake(self, 8, 10))

        self.food = Food(self, 10, 15)

    def is_in_body_part(self):
        x = random.randint(0, GRIDWIDTH - 1)
        y = random.randint(0, GRIDHEIGHT - 1)
        for body in self.snake_body:
            if x == body.x and y == body.y:
                x = self.is_in_body_part()
                y = self.is_in_body_part()
        return x, y

    def run(self):
        self.still_playing = True
        while self.still_playing:
            self.clock.tick(SPEED)
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        quit(0)

    def update(self):
        if self.paused == False:
            if self.food.food_collision() == True:
                x = self.is_in_body_part()
                y = self.is_in_body_part()
                self.food.x = x
                self.food.y = y
                self.snake_body.append(
                    Snake(self, self.snake_body[-1].x, self.snake_body[-1].y))
                self.food.x = random.randint(0, GRIDWIDTH - 1)
                self.food.y = random.randint(0, GRIDHEIGHT - 1)
                self.score += 1

            self.all_sprites.update()

            x = self.head.x
            y = self.head.y
            for body in self.snake_body:
                temp_x = body.x
                temp_y = body.y
                body.x = x
                body.y = y
                x = temp_x
                y = temp_y
            if self.orientation == 0:
                self.head.x += 1
            elif self.orientation == 1:
                self.head.y -= 1
            elif self.orientation == 2:
                self.head.x -= 1
            elif self.orientation == 3:
                self.head.y += 1

            for body in self.snake_body:
                if body.body_collision() == True:
                    self.still_playing = False

            if self.head.x > GRIDWIDTH - 1:
                self.head.x = 0
            elif self.head.x < 0:
                self.head.x = GRIDWIDTH
            elif self.head.y > GRIDHEIGHT - 1:
                self.head.y = 0
            elif self.head.y < 0:
                self.head.y = GRIDHEIGHT

    def draw(self):
        self.screen.fill(DARKGREY)
        self.draw_grid()
        self.all_sprites.draw(self.screen)

        if self.paused == True:
            pause_text = Text(8, 9, "PAUSED")
            pause_text.draw(self.screen, 150)

        pygame.display.flip()

    def draw_grid(self):
        for column in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, BLACK,
                             (0, column), (WIDTH, column))

        for row in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, BLACK, (row, 0), (row, HEIGHT))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.orientation != 3:
                    self.orientation = 1
                if event.key == pygame.K_s and self.orientation != 1:
                    self.orientation = 3
                if event.key == pygame.K_a and self.orientation != 0:
                    self.orientation = 2
                if event.key == pygame.K_d and self.orientation != 2:
                    self.orientation = 0
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused

    def main_screeen(self):
        self.screen.fill(BLACK)
        if self.still_playing == False:
            snake_game_text = Text(9, 7, "Game Over")
            snake_game_text.draw(self.screen, 100)

            snake_game_text = Text(14, 13, f"Score: {self.score}")
            snake_game_text.draw(self.screen, 30)
        else:
            snake_game_text = Text(9, 7, "Snake Game")
            snake_game_text.draw(self.screen, 100)

        self.start_button = Button(
            self, BLACK, WHITE, WIDTH / 2 - (150/2), 470, 150, 50, "START")
        self.start_button.draw(self.screen)

        self.quit_button = Button(
            self, BLACK, WHITE, WIDTH / 2 - (150/2), 545, 150, 50, "QUIT")
        self.quit_button.draw(self.screen)
        pygame.display.flip()
        self.wait()

    def wait(self):
        waiting = True
        while waiting:
            self.start_button.draw(self.screen)
            self.quit_button.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_over(mouse_x, mouse_y):
                        self.start_button.colour = LIGHTGREY
                    else:
                        self.start_button.colour = BLACK
                    if self.quit_button.is_over(mouse_x, mouse_y):
                        self.quit_button.colour = LIGHTGREY
                    else:
                        self.quit_button.colour = BLACK
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_over(mouse_x, mouse_y):
                        waiting = False
                    if self.quit_button.is_over(mouse_x, mouse_y):
                        self.quit()


game = Game()

while True:
    game.main_screeen()
    game.new()
    game.run()
