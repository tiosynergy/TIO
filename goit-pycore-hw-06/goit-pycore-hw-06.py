from collections import UserDict

# --- створюємо базовий клас для Name та Phone...
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


""" Клас Name(Field) для зберігання імені контакту.
 Обов'язкове поле."""
class Name(Field):
    pass


""" Клас Phone(Field) для зберігання номера телефону. 
Має валідацію формату (10 цифр)."""
class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Невірний номер телефону, помвинно бути 10 цифр")
        super().__init__(value)


"""Клас Record для зберігання інформації про контакт, 
включно з іменем та списком телефонів."""
class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone_number: str) -> None:
        """Додає новий номер телефону до запису"""
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number: str) -> None:
        """Видаляє номер телефону за значенням"""
        for i, phone in enumerate(self.phones):
            if phone.value == phone_number:
                self.phones.pop(i)
                return
        raise ValueError(f"Phone {phone_number} not found in contact {self.name}")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Замінює один номер телефону на інший"""
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)  # створюємо новий об'єкт з валідацією
                return
        raise ValueError(f"Phone {old_phone} not found in contact {self.name}")

    def find_phone(self, phone_number: str) -> Phone | None:
        """Шукає об'єкт Phone за номером або повертає None"""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones) if self.phones else "no phones"
        return f"Contact name: {self.name.value}, phones: {phones_str}"


"""Клас AddressBook(UserDict) для зберігання записів
 та керування ними.
ключ — ім'я, значення — об'єкт Record"""
class AddressBook(UserDict):

#--- метод add_record, який додає запис до self.data за ім'ям (ключ)
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

# ---метод find, який знаходить запис за ім'ям
    def find(self, name: str) -> Record | None:
        return self.data.get(name)

# --- метод delete, який видаляє запис за ім'ям
    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

#------  ВИКОРИСТАННЯ --------

if __name__ == "__main__":
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # находження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    # Пошук конкретного телефону в записі John
    found = john.find_phone("5555555555")
    if found:
        print(f"{john.name}: {found}")

    # Видалення запису Jane
    book.delete("Jane")

    print("\nПісля видалення Jane:")
    for name, record in book.data.items():
        print(record)