class Snake:
    def __init__(self, init_direction: tuple, init_body: list[tuple] = [], length: int = 3):
        self.length = length
        if init_body:
            self.body = init_body
        else:
            self.body = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.direction = init_direction

    def take_step(self, position):
        self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]


snake = Snake([(1, 1), (1, 2), (1, 3)], (2, 2))
