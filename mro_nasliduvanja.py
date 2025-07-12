# Багаторівневе наслідування - це коли клас наслідує від іншого класу, який вже є похідним класом. 
# Це створює "ланцюжок" наслідування, де можливості передаються через декілька рівнів.

# Уявімо, що ми маємо клас Bird і хочемо створити клас Parrot, який наслідує від Bird. 
# Але потім ми вирішуємо створити новий клас TalkingParrot, який наслідується вже від Parrot.

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

class Parrot(Bird):
    def can_fly(self):
        return True

class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"

my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase("Hello, World!"))
# У цьому прикладі TalkingParrot наслідує від Parrot, який, в свою чергу, наслідує від Bird.
# Таким чином, TalkingParrot має доступ до методів і властивостей як Bird


# Як ми бачимо наслідування дуже потужний інструмент. Але наслідуватися можна не тільки від одного класу, 
# а можна одразу від кількох. Таким чином можна отримувати об'єкти, що поєднують у собі властивості багатьох класів. 
# Тут повинно виникнути питання, а що буде, якщо кілька класів мають атрибути з однаковим ім'ям?

# Для відповіді на це питання потрібно зрозуміти, як Python шукає атрибути (поля або методи) в об'єктах.

# MRO (Method Resolution Order) в Python, визначає порядок, за яким класи будуть переглядатися під час пошуку методів.

# Ви можете переглянути MRO для будь-якого класу використовуючи метод mro() або атрибут __mro__. Наприклад:

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # Виведе порядок розв'язання методів для класу D
print(D.__mro__)  # Виведе те ж саме, що і D.mro()
# Виведе: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Це порядок MRO для класу D який означає, що Python спочатку шукатиме методи в D, потім у B, за ними в C, потім в A, 
# і, нарешті, в вбудованому базовому класі object, який є предком всіх класів.

# Давайте розберемо це на більш наочному прикладі. Де буде брати значення для поля name екземпляр класу C?

class A:
    name = "Я клас A"

class B:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"

class C(A, B):
    property = "Я знаходжусь в класі C"

c = C()
print(c.name)
print(c.property)
# Виведе:
# Я клас A  
# Я знаходжусь в класі C

# З цього прикладу видно, що у класі C поле name береться з A класу. 
# Якщо ж в цьому самому прикладі змінити список батьків з C(A, B) на C(B, A), то отримаємо:
class A:
    name = "Я клас A"

class B:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"

class C(B, A):
    property = "Я знаходжусь в класі C"

c = C()
print(c.name)
print(c.property)
# Виведе:
# Я клас B
# Я знаходжусь в класі C
# Тепер у класі C поле name береться з B класу.
