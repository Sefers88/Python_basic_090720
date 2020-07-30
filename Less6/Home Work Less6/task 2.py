class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05   #Указывается толщина покрытия в метрах, 0,05 соответствует 5 см
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Нужно {intake} тонн для строительства дороги по текущему плану')

road_to_city17 = Road(20000, 6)
road_to_city17.intake()
r = MassCount(20, 5000, 25)
