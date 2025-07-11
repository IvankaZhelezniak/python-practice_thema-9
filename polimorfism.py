# Поліморфізм - це один із ключових концептів ООП, який дозволяє об'єктам мати різні форми або поведінку, базуючись на їх типах.

# Поліморфізм походить від грецьких слів "polys" (багато) та "morph" (форма). 
# У контексті ООП, це відноситься до здатності різних класів використовувати методи з однаковою назвою, 
# але з різною реалізацією. Це дозволяє використовувати один інтерфейс для різних типів даних.

# Коли ми розглядали наслідування у прикладі з тваринами, ми вже бачили динамічний поліморфізм:

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)

# Тут make_sound - це метод, що використовується у кожному класі, але його реалізація різна для Cat та Dog. 
# Це дозволяє нам викликати make_sound на екземплярі Animal, не знаючи точно, чи це Cat, Dog, чи інший підклас Animal. 
# Ми створили функцію animal_sounds яка приймає список тварин і в принципі не важливо якого вони типу, головне, 
# щоб вони реалізували метод make_sound:

# Отже поліморфізм дозволяє обробляти об'єкти різних класів, 
# які є похідними від одного базового класу, через спільний інтерфейс (тобто через однакові методи).


# З поліморфізмом тісно пов'язано поняття качина типізація.

# Качина типізація (Duck Typing) - це концепція в програмуванні, яка відіграє важливу роль в динамічно типізованих мовах, 
# таких як Python. Назва походить від англійського вислову "Якщо це ходить як качка і крякає як качка, то це, ймовірно, качка".

# У контексті програмування, качина типізація означає, що замість перевірки типу об'єкта перед його використанням, 
# важливіше зосередитися на тому, чи має об'єкт потрібні методи чи властивості, які вимагаються для виконання певної функції або операції.

# Механізм Python дозволяє використовувати будь-які об'єкти один замість іншого, аби в обох були потрібні методи та поля. 
# Інтерпретатор не перевіряє, що у функцію або метод був переданий об'єкт потрібного або дочірнього класу, 
# достатньо щоб в об'єкта були потрібні методи і все буде працювати.

class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def make_it_quack(duck):
    duck.quack()

duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)

# У цьому прикладі, функція make_it_quack приймає параметр duck, але фактично не перевіряє, 
# чи це дійсно об'єкт класу Duck. Замість цього, вона просто викликає метод quack на переданому об'єкті. 
# Якщо об'єкт має метод quack, він може бути використаний функцією make_it_quack незалежно від його фактичного типу. 
# Це і є сутність качиної типізації. Головне, щоб атрибут називався так само і приймав ті самі аргументи (якщо це метод).

# У Python можна використовувати статичну типізацію для анотації типів 
# і одночасно покладатися на качину типізацію для поліморфізму та гнучкої поведінки об'єктів.

class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
# У цьому прикладі, качина типізація дозволяє нам передавати будь-який об'єкт, який має метод speak,
#  у функцію make_it_speak, не зважаючи на його конкретний клас.
#  Але, що стосується типу параметру speaker для функції make_it_speak?

# Щоб занотувати тип параметра функції speaker ми можемо використати typing.Protocol, який визначає набір методів, 
# які цей параметр має виконувати, не прив'язуючись до конкретного класу.

# Створимо інтерфейс, використовуючи typing.Protocol, для об'єктів, які можуть "говорити". 
# Ми хочемо, щоб будь-який об'єкт, який має метод speak, вважався сумісним з цим інтерфейсом.
from typing import Protocol

class Speaker(Protocol):
    def speak(self) -> str:
        pass

class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop

# Результат буде той самий але статична типізація за допомогою typing.Protocol використовується для вказівки, 
# що параметр speaker повинен відповідати інтерфейсу, який має метод speak.