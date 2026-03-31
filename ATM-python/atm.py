from option_menu import OptionMenu


def introduction():
    print("Welcome to the ATM Project!")


def main():
    option_menu = OptionMenu()
    introduction()
    option_menu.main_menu()


if __name__ == "__main__":
    main()
