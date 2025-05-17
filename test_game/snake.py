import curses
from random import randint

# Configuration
DELAY = 100  # milliseconds between movements


class SnakeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.window = curses.newwin(self.height, self.width, 0, 0)
        self.window.keypad(True)
        self.window.timeout(DELAY)
        curses.curs_set(0)

        self.snake = [
            [self.height // 2, self.width // 2 + 1],
            [self.height // 2, self.width // 2],
            [self.height // 2, self.width // 2 - 1],
        ]
        self.direction = curses.KEY_RIGHT
        self.food = self._create_food()
        self.score = 0

    def _create_food(self):
        while True:
            food = [randint(1, self.height - 2), randint(1, self.width - 2)]
            if food not in self.snake:
                return food

    def play(self):
        for y, x in self.snake:
            self.window.addch(y, x, curses.ACS_CKBOARD)
        self.window.addch(self.food[0], self.food[1], curses.ACS_PI)

        while True:
            key = self.window.getch()
            if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
                self.direction = key
            elif key in (ord('q'), ord('Q')):
                break

            head = [self.snake[0][0], self.snake[0][1]]
            if self.direction == curses.KEY_RIGHT:
                head[1] += 1
            elif self.direction == curses.KEY_LEFT:
                head[1] -= 1
            elif self.direction == curses.KEY_UP:
                head[0] -= 1
            elif self.direction == curses.KEY_DOWN:
                head[0] += 1

            # Collision with borders or self
            if (
                head[0] in [0, self.height] or
                head[1] in [0, self.width] or
                head in self.snake
            ):
                self._game_over()
                break

            self.snake.insert(0, head)

            if head == self.food:
                self.score += 1
                self.food = self._create_food()
                self.window.addch(self.food[0], self.food[1], curses.ACS_PI)
            else:
                tail = self.snake.pop()
                self.window.addch(tail[0], tail[1], ' ')

            self.window.addch(head[0], head[1], curses.ACS_CKBOARD)

    def _game_over(self):
 codex/-ln3esm
        msg = f"Game Over! Score: {self.score} - Press any key"

 codex/-alima1
        msg = f"Game Over! Score: {self.score} - Press any key"

        msg = f"Game Over! Score: {self.score} - Press any key".
 main
 main
        self.window.clear()
        self.window.addstr(self.height // 2, (self.width - len(msg)) // 2, msg)
        self.window.nodelay(False)
        self.window.getch()


if __name__ == '__main__':
    curses.wrapper(lambda stdscr: SnakeGame(stdscr).play())
