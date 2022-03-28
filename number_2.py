# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, p: float):
        self.p = p

    @abstractmethod
    def consumption(self):
        pass


class Coat (Clothes):

    @property
    def consumption(self):
        return round(self.p/6.5 + 0.5, 2)


class Costume (Clothes):

    @property
    def consumption(self):
        return round(self.p*2 + 0.3, 2)


class Total_consumption(Clothes):
    def __init__(self, children: list):
        self.children = children

    @property
    def consumption(self):
        answer = 0
        for item in self.children:
            answer += item.consumption
        return answer

coat = Coat(42)
costume = Costume(1.80)
total = Total_consumption([coat, costume])

print('Пальто: ', coat.consumption)
print('Костюм: ', costume.consumption)
print('Пальто+Костюм', total.consumption)