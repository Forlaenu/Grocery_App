# A user should be able to view all shopping lists and their items:
# Fiesta
# Milk, Soda, Fish

# Walmart
# Paper, Napkins, Plate, Chips

# Sams Club
# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey

def print_lists(shopping_list):
    print("- - Viewing Shopping Lists - -")

    #this may be redundant for the use of printing the lists
    def printing_lists():
        for key,value in shopping_list.items():
            print(f"{key}:")
            pretty_list = ', '.join(value)
            print(f"{pretty_list}\n")
    
    # def printing_lists(list_name):
    #     #we validate that it exists in the modify function
    #     temp_list = do_i_need_this_reference[list_name]
    #     for items in temp_list:
    #         return_list = ', '.join(items)
    #         return return_list

    #calling to run       
    printing_lists()
    # print("Test printing lists with list argument:")
    # printing_lists('Fiesta')