from typing import Tuple, List, Dict

#-------Декоратор для обработки ошибок ввода.
def input_error(func: function) -> function: #---- func - оборачивваемая функция 
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
    return inner  #------возвращаем обернутую функция, которая возвращает результат исходной функции-------


def parse_input(user_input: str) -> Tuple:
    """ разделяем ввод пользователя на команду и аргументы """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error #-----оборачиваем декоратором функцию add_contact
def add_contact(args: List, contacts: Dict) -> str:
    """ Добавляет новый контакт в словарь, имя и телефон """
    name, phone = args
    contacts[name] = phone
    return "Контакт добавлен"


@input_error
def change_contact(args: List, contacts: Dict) -> str:
    """ Изменяет телефон существующего контакта """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт изменен"
    else:
        return "Контакт не найден"


@input_error
def phone_username(args: List, contacts: Dict) -> str:
    """ Возвращает номер телефона по имени """
    if len(args) != 1:
        raise IndexError
    name = args[0]
    phone = contacts[name]
    return f"Номер телефона {name}: {phone}"


def show_all(contacts: Dict) -> str:
    """ Возвращает все контакты в f строке """
    if not contacts:
        return "Контактов еще нет"
    return "\n".join(f"{name}: {phone}" for name, phone in sorted(contacts.items()))


def main() -> None:
    """ Основная функция бота """
    contacts: Dict = {
        "John": "123-456-7890",
        "Alice": "987-654-3210",
        "Bob": "555-123-4567",
        "Eva": "444-888-9999",
        "Michael": "111-222-3333",
        "Sophia": "777-888-9999",
        "David": "222-333-4444",
        "Olivia": "333-444-5555",
        "James": "444-555-6666",
        "Emma": "555-666-7777"
    }

    print("Welcome to the assistant bot!")
   
    while True:
        try:
            user_input: str = input("Enter a command: ").strip()
            if not user_input:
                continue

            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                if not args:
                    print("Enter the argument for the command")
                    continue
                result = add_contact(args, contacts)
                print(result)

            elif command == "change":
                if not args:
                    print("Enter the argument for the command")
                    continue
                result = change_contact(args, contacts)
                print(result)

            elif command == "phone":
                if not args:
                    print("Enter the argument for the command")
                    continue
                result = phone_username(args, contacts)
                print(result)

            elif command == "all":
                print(show_all(contacts))

            else:
                print("Invalid command.")

        except KeyboardInterrupt:
            print("\nGood bye!")
            break

# конструкция прямого вызова--------
if __name__ == "__main__":
    main()