import os
import time

from snake import Snake

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)


class Game:
    def __init__(self, width: int, height: int):
        self.height: int = height
        self.width: int = width
        self.ded = False

        self.board: list[list] = None
        self.create_new_board()

        self.snake = Snake(DOWN, [(3, 2), (3, 3), (3, 4), (3, 5)])
        # self.snake = Snake(DOWN)
        self.insert_snake()

    def render(self) -> None:
        os.system("clear")
        print("height:", self.height)
        print("width:", self.width)
        print(f"+{"-" * (self.width)}+")
        for row in self.board:
            print(f"|{"".join(row)}|")
        print(f"+{"-" * (self.width)}+")

    def loop(self) -> None:
        for _ in range(20):
            if self.ded is False:
                self.render()
                self.move_snake()
                print(self.snake.head())
                time.sleep(.5)
            else:
                print("ded")
                return

    def change_direction(self):
        inp = input()
        dir = None
        match inp:
            case "w":
                dir = UP
            case "s":
                dir = DOWN
            case "D":
                dir = RIGHT
            case "A":
                dir = LEFT
        return dir

    def move_snake(self) -> None:
        snake = self.snake
        direction = snake.direction
        head = snake.head()
        new_position = (head[0] + direction[0], head[1] + direction[1])
        snake.take_step(new_position)
        if snake.head()[0] > self.height or snake.head()[0] < 0:
            self.ded = True
            return
        if snake.head()[1] > self.width or snake.head()[1] < 0:
            self.ded = True
            return
        self.create_new_board()
        self.insert_snake()

    def create_new_board(self) -> None:
        self.board = [[" " for _ in range(self.width)]
                      for _ in range(self.height)]

    def insert_snake(self) -> None:
        board = self.board
        body = self.snake.body
        head = self.snake.head()
        try:
            board[head[0]][head[1]] = "X"
            for s in body[:-1]:
                body_x = s[0]
                body_y = s[1]
                board[body_x][body_y] = "0"
        except IndexError:
            self.ded = True


if __name__ == "__main__":
    game = Game(15, 10)
    game.loop()
