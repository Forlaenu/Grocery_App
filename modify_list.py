from print_lists import *
# A user should be able to select a shopping list and then

# add items

# delete items

# view all items
# A user should be able to delete a shopping list

valid_input = ['1','2','3','q']
menu_options_output = '''Modify Menu
1 - Add item(s)
2 - Delete item(s)
3 - View item(s)
q - Quit to Main Menu
'''
def modify_list(shopping_list):
    print("- - Modifying Shopping Lists - -")

    def verify_list_exists():
        for list_names in shopping_list:
            shopping_lists_to_print = ", ".join(list_names)
        
        user_selected_list = input(f"Which list would you like to modify? ({shopping_lists_to_print}): ")