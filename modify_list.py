from print_lists import *
# A user should be able to select a shopping list and then

# add items

# delete items

# view all items
# A user should be able to delete a shopping list

menu_options_output = '''Modify Menu
1 - Add item(s)
2 - Delete item(s)
3 - View item(s)
q - Quit to Main Menu
'''
valid_input = ['1','2','3','q']
def is_valid(user_input):
    if user_input in valid_input:
        return True
    else:
        return False
        
def modify_list(shopping_list):
    print("- - Modifying Shopping Lists - -")

    def verify_list_exists():
        shopping_lists_to_print = []
        for key,value in shopping_list.items():
            shopping_lists_to_print.append(key)
        shopping_lists_to_print_string = ', '.join(shopping_lists_to_print)
        
        user_selected_list = input(f"Which list would you like to modify? ({shopping_lists_to_print_string}): ")
        if user_selected_list in shopping_list:
            print(f"Modifying {user_selected_list}")
            modify_this_list(user_selected_list)
        else:
            print("ERROR: Verify spelling and capitalization, try again")
            verify_list_exists()

    def modify_this_list(list_name):
        # We have a valid list name, use that to access the items in list

        # have to be careful here when to loop thru this function.
        # the way that might work best is calling the function after each modify action is complete
        # that way the user can modify until they enter 'q' to quit
        print(menu_options_output)
        user_input = input(": ")
        if is_valid(user_input):
            if user_input == '1':
                print("Add items")
                modify_this_list(list_name)
            if user_input == '2':
                print("Delete items")
                modify_this_list(list_name)
            if user_input == '3':
                print("View items")
                modify_this_list(list_name)
            if user_input == 'q':
                print("- - Returning to Main Menu - -")
        else:
            # Telling the user its wrong and to try again. Running function from start
            print(f"\nERROR: Invalid input. Valid Options: {valid_input}. Try again\n")
            modify_this_list(list_name)


    #Calling base function
    verify_list_exists()
