import random

from board import Board
from ship import Ship
from direction import Direction
from dot import Dot
from player import User, AI

# Задаем длины кораблей, которые будут использованы в игре
SHIPS_LENGTH = [3, 2, 2, 1, 1, 1, 1] #[3, 2, 2, 1, 1, 1, 1]

# Максимальное количество попыток заполнения доски
CREATE_BOARD_MAX_RETRY_COUNT = 1000

class Game:

    def __init__(self):
        # Инициализируем игру (доски, игроков)
        user_board = self.random_board()
        ai_board = self.random_board()
        self.user_board = user_board
        self.ai_board = ai_board
        self.user = User(user_board, ai_board)
        self.ai = AI(ai_board, user_board)

    @staticmethod
    def greet():
        # Приветствие игрока перед началом игры
        print("Добро пожаловать в игру 'Морской бой'!")

    def loop(self):
        while True:
            while True:
                if self.ai_board.all_ships_hit():
                    # Если все корабли AI повреждены, то игрок User победил
                    print('Игрок User одерживает победу! ПОЗДРАВЛЯЕМ!')
                    return
                if not self.user.move():
                    # Если игрок User не может сделать ход, переходим к следующему ходу
                    break
            while True:
                if self.user_board.all_ships_hit():
                    # Если все корабли User повреждены, то AI победил
                    print('Игрок AI одерживает победу! ПОЗДРАВЛЯЕМ!')
                    return
                if not self.ai.move():
                    # Если AI не может сделать ход, переходим к следующему ходу
                    break

    @staticmethod
    def random_board():
        # Генерация случайной доски с расставленными случайным образом кораблями
        board = Board()

        create_board_retry_count = 0
        for curr_length in SHIPS_LENGTH:
            while True:
                if create_board_retry_count == CREATE_BOARD_MAX_RETRY_COUNT:
                    # Если достигнуто максимальное количество попыток, создаем новую доску и начинаем сначала
                    print('Превысили количество попыток заполнения доски, начинаем сначала!')
                    create_board_retry_count = 0
                    board = Board()
                x = random.randint(0, board.size - 1)
                y = random.randint(0, board.size - 1)
                direction = random.choice([Direction.Vertical, Direction.Horizontal])
                ship = Ship(curr_length, Dot(x, y), direction)
                try:
                    if board.add_ship(ship):
                        break
                except Exception:
                    create_board_retry_count += 1
                    continue
        return board

    def start(self):
        # Запуск игры: приветствие, вывод начальных досок и начало цикла ходов
        self.greet()
        print('Доска User-a!')
        self.user_board.print()
        print('Доска AI')
        self.ai_board.print()
        self.loop()
        print('Игра окончена!')