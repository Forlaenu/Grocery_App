''' my thoughts on how it could look

maybe a list of dictionaries in the end, so you could have multiple member's shopping lists... 
altho referencing the list of dictionaries would be... fun :)

        starts with a dictionary because the key could be the store:
shopping list = {
    'Fiesta' : [    and the value could be a list, which could easily be appended and popped
        'Milk',
        'Soda',
        'Fish'
    ],
        Dictionary number 2 here, key = Walmart, value = another list
    'Walmart' : [
        'Paper',
        'Napkins',
        'Plate',
        'Chips'
    ],
    'Sams Club' : [
        'Chicken', 'Beef', 'Eggs', 'Sugar', 'Salt', 'Pepper', 'Honey'
    ]
}
or...

global_shopping_list = {
    'Sarah_list' : {
        'Fiesta' : [
            'Milk'
            etc etc
        ]
    },
    'Caydens_list' : {
        'Walmart' : [
            'Bunny food'
            etc etc
        ]
    }
}
if you wanted to "Append" the dictionary, you could create the list or append the list later,
and use shopping_list['New Store'] = new_list !

'''
# Here are the features you need to implement:

# A user should be able to create shopping lists.

# A shopping list will have a name

# A user should be able to select a shopping list and then

# add items

# delete items

# view all items
# A user should be able to delete a shopping list

# A user should be able to view all shopping lists and their items:
# Fiesta
# Milk, Soda, Fish

# Walmart
# Paper, Napkins, Plate, Chips

# Sams Club
# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey
from create_new_list import create_new_list
from modify_list import modify_list
from print_lists import print_lists

print("\n\tWelcome to Cayden's Amazing Shopping List\n")
main_menu = """- - Main Menu - - 
Please choose an option:
1 - Create a NEW shopping list
2 - Modify existing shopping list
3 - View Shopping List(s)
q - Quit"""

valid_input = ['1', '2', '3', 'q']
shopping_list = {}

def is_valid(user_input):
    if user_input in valid_input:
        return True
    else:
        return False

def main():
    while True:
        print(main_menu)
        user_input = input(": ")
        if is_valid(user_input):
            if user_input == '1':
                create_new_list()
            if user_input == '2':
                # print a short-hand of the lists titles - future update
                # actually not needed. Can do in modify list function
                modify_list()
            if user_input == '3':
                print_lists()
            if user_input == 'q':
                print("- - BYE! Happy Shopping! - -")
                exit()
        else:
            # Telling the user its wrong and to try again. Running program from start
            print(f"\nERROR: Invalid input. Valid Options: {valid_input}. Try again\n")
            main()
main()
        
# A function just to check if user input is valid
# this allows me to update my menu without re-doing a bunch of code
# next idea: some way of creating a dynamic menu. maybe a list of function calls
# which would be referenced by (i+1).... or a dictionary! oh shit
# ie {1 : []}
