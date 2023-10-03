print("Sequential Search Algorithm.")
values = ["Mark", "Steven", "Mary", "Jack", "Lucie"]

def find_value():
    search_the_names = input("Enter the name you're looking for? ")
    if search_the_names.capitalize() in values:
        print(f"The name {search_the_names} is in the list.")
    else:
        print("The name you're looking for is not in the list.")


find_value()