import os

from snake import Snake

UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)


class Game:
    def __init__(self, width: int, height: int):
        self.height: int = height
        self.width: int = width

        self.board: list[list] = None
        self._create_new_board()

        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], UP)
        self._insert_snake()

    def render(self) -> None:
        os.system("clear")
        print("height:", self.height)
        print("width:", self.width)
        print(f"+{"-" * (self.width)}+")
        for row in self.board:
            print(f"|{"".join(row)}|")
        print(f"+{"-" * (self.width)}+")

    def _create_new_board(self) -> None:
        self.board = [[" " for _ in range(self.width)]
                      for _ in range(self.height)]

    def _insert_snake(self) -> None:
        board = self.board
        body = self.snake.body

        head_x = body[0][0]
        head_y = body[0][0]
        board[head_x][head_y] = "X"
        for s in range(1, len(self.snake.body)):
            body_x = body[s][0]
            body_y = body[s][1]
            board[body_x][body_y] = "O"


game = Game(5, 7)
game.render()
