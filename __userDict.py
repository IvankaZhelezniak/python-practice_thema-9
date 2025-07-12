# UserDict — це клас, що міститься в модулі collections і слугує обгорткою навколо словника. 
# Він дозволяє легше створювати власні класи словників, модифікуючи або додаючи нову поведінку до стандартних методів словника.

from collections import UserDict

class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value           # data — це атрибут UserDict, який містить словник

# Створення екземпляра власного класу
my_dict = MyDictionary({'a': 1, 'b': 2})
my_dict.add_key('c', 3)
print(my_dict)

# Ми створили клас MyDictionary, який наслідується від UserDict. 
# Це надає всю стандартну функціональність словників, а також дозволяє легко модифікувати або розширювати її. 
# Також ми додали метод add_key який демонструє, як можна додати нову поведінку для додавання елементів у словник.



# Розглянемо більш корисний приклад. Ми маємо наступний список словників:

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]

# Ми хотіли б мати можливість, щоб у словника були методи які нам показували ім'я-телефон, 
# та ім'я-email контакту. Для цього створимо клас Customer, який наслідує від UserDict з модуля collections.

class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"

# Він розширює можливості UserDict та має два методи: phone_info і email_info, кожен з яких повертає рядок з ім'ям та 
# телефонним номером або електронною адресою відповідного контакту.

# Щоб скористатися можливостями створеного класу нам необхідно створити новий список customers, 
# в якому кожен елемент списку contacts перетворюється на екземпляр класу Customer. 
# Це дозволить нам використовувати визначені в класі методи для кожного контакту.

if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("---------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("---------------------------")

    for customer in customers:
        print(customer.email_info())
# ти маєш список із 3 об’єктів Customer, кожен із яких поводиться як словник і має додаткові методи:
# customer тепер є об’єктом класу Customer, який містить ці дані як словник. Тобто ти можеш робити:
# print(customer["name"])          # Allen Raymond

# У цьому прикладі ми двічі виконуємо ітерації по списку customers: перший раз для виведення інформації 
# про телефони контактів через виклик методу phone_info, 
# а другий раз - для виведення інформації про електронні адреси через виклик методу email_info.