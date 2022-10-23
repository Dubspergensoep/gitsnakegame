import snake as sn
import numpy as np
import pygame
import sys

class snakegame():
    def __init__(self, game_size=17, tile_size=30):
        # input parameters
        self.game_size = game_size  # same size as google snake game
        self.tile_size = tile_size
        self.snake_color = (0, 255, 0)  # green
        self.apple_color = (255, 0, 0)  # red
        self.background_color = (0, 0, 0)  # black
        self.waiting_time = 200  # in ms
        self.clear_count_max = 10
        self.clear_count = 0

        # other parameters
        self.screen = None
        self.snake = None
        # dataset variables
        self.save_data = False
        snakehistory = np.array([])
        directionhistory = np.array([])

    def run(self):
        # setup game
        self.__initialise_game()

        # Run game
        print("game starts running")
        while self.snake.SnakeAlive:
            # update snake game
            self.__update_game()
            # change direction of snake
            self.__handle_input()
            # draw screen
            self.__draw()
        sys.exit()


    def __initialise_game(self):
        # initialize snake object
        self.snake = sn.Snake(self.game_size)
        # initializing Pygame
        pygame.init()
        width  = self.game_size * self.tile_size
        heigth = self.game_size * self.tile_size
        size = [width, heigth]
        self.screen = pygame.display.set_mode(size)
        return 0

    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.snake.ChangeDirection("u")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.snake.ChangeDirection("d")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.snake.ChangeDirection("r")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.snake.ChangeDirection("l")
        return 0

    def __update_game(self):
        # update snake game
        self.snake.Update()
        SnakeArr = self.snake.GetSnakeArray()
        return 0

    def __draw(self):
        # drawing snakeGame
        self.screen.fill(self.background_color)
        for snakepart in self.snake.snakeArr:
            pygame.draw.rect(self.screen, self.snake_color,
                             (snakepart[0] * self.tile_size, snakepart[1] * self.tile_size, self.tile_size,
                              self.tile_size))
        Apple = self.snake.GetApple()
        pygame.draw.rect(self.screen, self.apple_color,
                         (Apple[0] * self.tile_size, Apple[1] * self.tile_size, self.tile_size, self.tile_size))
        pygame.display.flip()

        # Waiting
        pygame.time.wait(self.waiting_time)
        return 0

    def __save_data(self):
        # Save game data
        if self.save_data:
            snakehistory = np.append(self.snakehistory, self.snake.snakeArr)
            directionhistory = np.append(self.directionhistory, self.snake.GetDir())
            print([self.snake.snakeArr, self.snake.GetDir()])