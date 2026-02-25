def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Контакт добавлен"


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт изменен"
    else:
        return "Контакт не найден"


def phone_username(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Номер телефона {name}: {contacts[name]}"
    else:
        return "Контакт не найден"


def show_all(contacts):
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return result


def main():
    contacts = {
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
        user_input:str = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add=add_contact(args, contacts)
            print(add)
        elif command == "change":
            print(change_contact(args, contacts))
            print(contacts)
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

# конструкция прямого вызова--------
if __name__ == "__main__":
#  вызов фунуции-----------
    main()
