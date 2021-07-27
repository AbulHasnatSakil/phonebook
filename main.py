from contacts import phonebook
import sys
def main():
    while True:
        f = phonebook()
        f.menu()
        choice = int(input("Enter your choice:"))
        if choice == 1:
            name = input("Enter the name to add:")
            phone = input("Enter the phone Number to add:")
            email = input("Enter the email address to add:")
            d = {"name": name, "phone": phone, "email": email}
            f.add(d)
            print('Contacts added.')
        elif choice == 2:
            f.display()
        elif choice == 3:
            name = input("Enter the name you want to search for:")
            f.search(name)
        elif choice == 4:
            name = input("Enter the name of contacts you want to delete")
            f.delete(name)
        elif choice == 5:
            print("Exiting.")
            sys.exit()
        else:
            print("Invalid choice.")

main()

