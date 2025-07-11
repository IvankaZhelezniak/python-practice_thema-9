# Ми створимо клас Pokemon, що ілюструє основні принципи об'єктно-орієнтованого програмування (ООП), 
# а потім створимо об'єкт класу Pokemon - pikachu. Клас Pokemon буде містити атрибути: name, type, і health.

# Для класу ми визначимо наступні методи:

# attack (напад) - дозволяє покемону атакувати іншого покемона.
# dodge (уклон) - дає можливість уникнути атаки.
# evolve (еволюціонувати) - дозволяє покемону еволюціонувати в іншу форму.


class Pokemon:
    def __init__(self, name, type, health):
        self.name = name             # Ініціалізація атрибута імені
        self.type = type              # Ініціалізація атрибута типу
        self.health = health         # Ініціалізація атрибута здоров'я

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form

# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")
