class Snake:
    def __init__(self, init_body, init_direction, length: int = 3):
        self.length: int = length
        self.body: list[tuple] = init_body
        self.direction: tuple = init_direction

    def take_step(self, position):
        self.body.insert(0, position)
        self.body.pop()

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[0]


snake = Snake([(1, 1), (1, 2), (1, 3)], (2, 2))
