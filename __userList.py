# UserList - це клас, який дозволяє створювати власні версії списків з додатковими функціями. 
# Ви можете додавати нові методи або змінювати ті, що вже існують, щоб вони працювали по-іншому. 
# Це корисно, коли вам потрібен список, який робить щось спеціальне, чого не робить звичайний список Python.

from collections import UserList

class MyList(UserList):
    # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)

# Створення екземпляру MyList
my_list = MyList([1, 2, 3])
print("Оригінальний список:", my_list)

# Додавання елементу, якщо він не існує
my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
print("Оновлений список:", my_list)


# Наступний приклад:
class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))

countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum())

# У цьому прикладі ми створили клас, який поводиться як список, але в ньому є метод sum , 
# який повертає суму всього вмісту цього класу, при цьому перетворюючи рядки на цілі числа.
