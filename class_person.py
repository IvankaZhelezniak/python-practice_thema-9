# У будь-якого методу класу завжди повинен бути, принаймні, один аргумент self, 
# це вимога синтаксису Python, оскільки інтерпретатор під час виклику методу 
# обов'язково передасть першим аргументом сам об'єкт, а потім уже всі аргументи, які були передані під час виклику.

class Person:
    count = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.count += 1

    def say_name(self) -> None:
        return f"Hi! I am {self.name} and I am {self.age} years old."

    def set_age(self, age: int) -> None:
        self.age = age

    def how_many_persons(self) -> None:
        print(f"Кількість людей зараз {Person.count}")

bob = Person('Boris', 34)
bob.how_many_persons()
print(bob.say_name())
bob.set_age(25)
bob.say_name()

alex = Person('Alex', 20)
bob.how_many_persons()
