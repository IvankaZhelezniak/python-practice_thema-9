# створимо систему управління статусами замовлень для інтернет-магазину. 


# У цьому прикладі, Enum використовується для створення чітко визначеного набору статусів, 
# які може мати замовлення. 
# Ці статуси включають "Новий" (NEW), "В обробці" (PROCESSING), "Відправлено" (SHIPPED), та "Доставлено" (DELIVERED).

# Перш за все, нам потрібно визначити Enum, який буде представляти різні статуси замовлень.
from enum import Enum, auto

class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()

# Використання auto() дозволяє автоматично призначати значення членам Enum

# Тепер створимо клас Order, який буде використовувати наш перелічуваний тип даних OrderStatus для відстеження статусу замовлення.
class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")

# Тепер створимо декілька замовлень і покажемо, як можна оновити та відобразити їх статуси.
order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)

order1.display_status()
order2.display_status()
