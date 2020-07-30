class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
    def get_full_name(self):
        return self.name + self.surname
    def get_full_profit(self):
        self.__income = {'Оклад': self.profit, 'Премия': self.bonus}
        return self.__income

manager = Position('Ivan', 'Serdukov', 'manager', 5500, 1900)
print(f'Имя и Фамилия работниа: {manager.name, manager.surname}, оклад и премия работник: {manager.profit, manager.bonus}' )
