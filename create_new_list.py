def create_new_list(shopping_list):
    print("- - Creating a new shopping list - -")

    def new_list():
        user_input = input("Name for the new list: ")
        user_confirmation = input(f"Creating new list, is {user_input} correct? (y/n): ")
        # this currently feels like the easiest and fastest user_input verification process (y/n)
        if user_confirmation == 'y':
            # this creates the new dictionary key 'user_input' with value of an empty list
            shopping_list[user_input] = []
            print("Done")
        elif user_confirmation == 'n':
            print("Okay. Lets try again!")
            new_list()
        else:
            print("ERROR: Input invalid. Expected 'y' or 'n'. Try again!")
            new_list()
    new_list()