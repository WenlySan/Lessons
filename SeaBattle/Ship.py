# Следующим идёт класс Ship — корабль на игровом поле, который описывается параметрами:
#
# Длина.
# Точка, где размещён нос корабля.
# Направление корабля (вертикальное/горизонтальное).
# Количеством жизней (сколько точек корабля ещё не подбито).
# И имеет метод dots, который возвращает список всех точек корабля.
from Dot import Dot

class Ship:  # •
    def __init__(self, name, xy=Dot(x=1, y=1), rotation=90, length=1, mark="■", hp=1):
        self.name = name
        self.xy = xy
        self.rotation = rotation
        self.length = length
        self.mark = mark
        self.hp = hp

    def get_length(self):
        return self.length * list(self.mark)

    def parking(self):
        for _ in self.get_length():
            return self.get_length()


shipka = Ship(name="Ks", length=2, mark="■")

print(shipka.parking())
