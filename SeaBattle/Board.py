# Самый важный класс во внутренней логике — класс Board — игровая доска. Доска описывается параметрами:
#
# Двумерный список, в котором хранятся состояния каждой из клеток.
# Список кораблей доски.
# Параметр hid типа bool — информация о том, нужно ли скрывать корабли на доске (для вывода доски врага) или нет (для своей доски).
# Количество живых кораблей на доске.
# И имеет методы:
#
# Метод add_ship, который ставит корабль на доску (если ставить не получается, выбрасываем исключения).
# Метод contour, который обводит корабль по контуру. Он будет полезен и в ходе самой игры, и в при расстановке кораблей
# (помечает соседние точки, где корабля по правилам быть не может).
# Метод, который выводит доску в консоль в зависимости от параметра hid.
# Метод out, который для точки (объекта класса Dot) возвращает True, если точка выходит за пределы поля, и False, если не выходит.
# Метод shot, который делает выстрел по доске (если есть попытка выстрелить за пределы и в использованную точку, нужно выбрасывать исключения).

from Dot import Dot


class Board:

    def __init__(self, xy=Dot(1, 1), count_ship=[0], count_ship_life=[0], hid=True):
        self.xy = xy
        self.count_ship = count_ship
        self.count_ship_life = count_ship_life
        self.hid = hid

    def create_boar(self, count):
        board = [['[ ]' for _ in range(count)] for _ in range(count)]
        return board




a = Board(xy=Dot(1, 2))

print(*(a.create_boar(4)))

# print(a.xy.get_xy())


def print_board(count,board, board_ai):
    # board = [['[ ]' for _ in range(count)] for _ in range(count)]
    # board_ai = [['[ ]' for _ in range(count)] for _ in range(count)]
    print("Мое поле")
    print('', *[_ for _ in range(count)], ' ', *[_ for _ in range(count)], sep='   ', )
    for _ in range(count):
        print(str(_), *board[_], ' ', str(_), *board_ai[_])


# print_board(10)

print()
