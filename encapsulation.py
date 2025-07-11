class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self) -> str:
        return f"Hi {self.name}"

p = Person("Boris", 34)

# Клас Person має два поля name та age та метод greeting, до яких можна вільно доступатися 
# з будь-якого місця у програмі. В Python вони не мають спеціального префіксу. 
# Такі методи та поля називають публічними (public), тобто вони доступні для прямого читання та зміни ззовні класу.

class Person1:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"
        # Поле _is_active має префікс _, що вказує на те, що це поле призначене для внутрішнього використання.
        # Це не є суворим правилом, але вказує на те, що доступ до цього поля ззовні класу не рекомендується.
    def is_active(self):
        return self._is_active
        # Метод is_active дозволяє отримати доступ до захищеного поля _is_active.
    def set_active(self, active: bool):
        self._is_active = active
        # Метод set_active дозволяє змінити значення захищеного поля _is_active.
p = Person1("Boris", 34, True)
print(p.name, p.age, p._is_active)
print(p.name, p.age, p.is_active())
print(p.greeting())
print(p.name, p.age, p._is_active)

# Поле _is_active має провідне нижнє підкреслення, щоб показати, що воно призначене для того, щоб бути захищеним. 
# Поганою практикою в цьому контексті вважається доступ або зміна захищених атрибутів класу p._is_active ззовні цього класу 
# або ззовні його нащадків. Що нами і зроблено але тільки в рамках демонстрації!

# Якщо ми хочемо взаємодіяти з захищеними полями об'єкту ззовні, необхідно впровадити правильний підхід до інкапсуляції 
# у класі Person та слід використовувати методи для взаємодії з такими атрибутами об'єкту




# В Python не існує справжньої приватності для атрибутів класів, як це реалізовано, наприклад, у Java. 
# Python використовує так зване "перетворення імен" для забезпечення цього рівня інкапсуляції. 
# Атрибути, що вважаються приватними позначаються двома підкресленнями __ і не можуть бути доступні безпосередньо ззовні класу.

class Person2:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p2 = Person2("Boris", 34, True, False)
# print(p2.__is_admin)

# Як видно з прикладу , доступу за допомогою p2.__is_admin немає.
# Насправді було лише змінене ім'я поля, щоб запобігти випадковому доступу до нього, але воно 
# все одно доступно ззовні класу. Змінене ім'я формується як знак підкреслювання, ім'я класу та ім'я змінної.

class Person3:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p3 = Person3("Boris", 34, True, False)
print(p3._Person3__is_admin)   # Доступ до приватного атрибута через змінене ім'я
# Виводить:
# False

# Тож можна, за бажанням, отримати доступ до поля __is_admin через вираз p3._Person3__is_admin, що загалом нічого не захищає.



# Щоб реалізувати методи доступу до приватного поля __is_admin у класі Person, 
# ми можемо використати той самий підхід, що і до захищеного поля _is_active

class Person4:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin

        
p4 = Person4("Boris", 34, True, False)
print(p4.get_is_admin())
p4.set_is_admin(True)
print(p4.get_is_admin())
