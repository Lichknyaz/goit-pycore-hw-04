
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def change_contact(args, contacts):
    if len (args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Phone number updated."
        else:
            return "No such name"
    else:
        return "Not correct entry"

def add_contact(args, contacts):
    if len (args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added"
    else:
        return "Not correct entry"

def show_phone (args: list, contacts: dict):
    if len (args) == 1:
        phone = contacts.get(args[0])
        if phone == None:
            return "No such name" 
        return phone
    else:
        return "Not correct entry"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "phone":
                print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
