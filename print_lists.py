# A user should be able to view all shopping lists and their items:
# Fiesta
# Milk, Soda, Fish

# Walmart
# Paper, Napkins, Plate, Chips

# Sams Club
# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey

def print_lists(shopping_list):
    print("- - Viewing Shopping Lists - -")

    def printing_lists():
        for key,value in shopping_list.items():
            print(f"{key}:")
            pretty_list = ', '.join(value)
            print(f"{pretty_list}\n")
    printing_lists()