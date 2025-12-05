#============= Shoe Class =============

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        Initialise the following attributes:
            ● country
            ● code
            ● product
            ● cost
            ● quantity
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''
        Return the cost of the shoe.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Return a string representation of the Shoe object.
        '''
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#============= Shoe list =============
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#============= Functions outside the class =============

def read_shoes_data():
    '''
    This function opens the file inventory.txt,
    reads each line, creates Shoe objects,
    and appends them into shoe_list.
    '''
    try:
        with open('inventory.txt', 'r') as file:
            next(file)        # skip header line

            for line in file:
                data = line.strip().split(',')

                if len(data) != 5:
                    print("Error: Invalid data format.")
                    continue

                shoe = Shoe(data[0], data[1], data[2], data[3], data[4])
                shoe_list.append(shoe)

    except FileNotFoundError:
        print("Error: inventory.txt not found!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def capture_shoes():
    '''
    This function allows a user to capture data
    about a shoe and append the object inside shoe_list.
    '''
    print("\nEnter new shoe information:")
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    
    # Input validation for cost
    while True:
        try:
            cost = input("Cost: ")
            cost_int = int(cost)
            if cost_int < 0:
                print("Error: Cost cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Cost must be a valid integer. Please try again.")
    
    # Input validation for quantity
    while True:
        try:
            quantity = input("Quantity: ")
            quantity_int = int(quantity)
            if quantity_int < 0:
                print("Error: Quantity cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Quantity must be a valid integer. Please try again.")

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    with open("inventory.txt", "a") as file:
        file.write(f"\n{shoe}")

    print("Shoe successfully captured.\n")


def view_all():
    '''
    This function will iterate over shoe_list and
    print the __str__ representation of each Shoe object.
    '''
    if not shoe_list:
        print("No shoes loaded.")
        return

    print("\n=========== ALL SHOES ===========")
    print(f"{'Country':<15} {'Code':<10} {'Product':<25} {'Cost':>10} {'Quantity':>10}")
    print("-"*80)
    
    for shoe in shoe_list:
        print(f"{shoe.country:<15} {shoe.code:<10} {shoe.product:<25} {shoe.cost:>10} {shoe.quantity:>10}")
    
    print()  # Add blank line after output


def re_stock():
    '''
    Find the shoe with the lowest quantity and allow the user to restock it.
    Update inventory.txt afterwards.
    '''
    if not shoe_list:
        print("No shoes loaded.")
        return

    lowest_shoe = min(shoe_list, key=lambda s: s.quantity)

    print("\n" + "="*60)
    print("RESTOCK NEEDED".center(60))
    print("="*60)
    print(f"\nProduct:  {lowest_shoe.product}")
    print(f"Code:     {lowest_shoe.code}")
    print(f"Country:  {lowest_shoe.country}")
    print(f"Current Quantity: {lowest_shoe.quantity}")
    print(f"Cost:     R{lowest_shoe.cost}")
    print("-"*60)
    
    # Get confirmation before proceeding
    confirm = input("\nDo you want to restock this shoe? (yes/no): ").lower()
    
    if confirm not in ['yes', 'y']:
        print("Restock cancelled.")
        return
    
    # Input validation for quantity to add
    while True:
        try:
            add_amount = input("How many units to add? ")
            add_amount_int = int(add_amount)
            if add_amount_int < 0:
                print("Error: Cannot add negative quantity. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")
    
    lowest_shoe.quantity += add_amount_int

    print("\n✓ Quantity updated successfully!")
    print(f"\nProduct:  {lowest_shoe.product}")
    print(f"New Quantity: {lowest_shoe.quantity}\n")

    # Update file
    with open("inventory.txt", "w") as file:
        file.write("country,code,product,cost,quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe}\n")


def search_shoe():
    '''
    Search for a shoe using its code
    and print the object if found.
    '''
    code = input("\nEnter shoe code: ").upper()

    for shoe in shoe_list:
        if shoe.code.upper() == code:
            print("\n" + "="*60)
            print("SHOE FOUND".center(60))
            print("="*60)
            print(f"\nCountry:  {shoe.country}")
            print(f"Code:     {shoe.code}")
            print(f"Product:  {shoe.product}")
            print(f"Cost:     R{shoe.cost}")
            print(f"Quantity: {shoe.quantity}")
            print("="*60 + "\n")
            return shoe

    print("\n✗ Shoe not found.\n")
    return None


def value_per_item():
    '''
    Calculate and display the total value for each shoe.
    value = cost * quantity
    '''
    if not shoe_list:
        print("No shoes loaded.")
        return
    
    print("\n" + "="*80)
    print("VALUE PER ITEM".center(80))
    print("="*80)
    
    # Table header
    print(f"{'Product':<30} {'Cost':>12} {'Quantity':>12} {'Total Value':>15}")
    print("-"*80)
    
    # Table rows
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product:<30} R{shoe.cost:>11} {shoe.quantity:>12} R{value:>14}")
    
    print("="*80 + "\n")


def highest_qty():
    '''
    Determine the shoe with the highest quantity
    and show that it is for sale.
    '''
    if not shoe_list:
        print("No shoes loaded.")
        return

    highest = max(shoe_list, key=lambda s: s.quantity)

    print("\n" + "="*60)
    print("🔥 ON SALE 🔥".center(60))
    print("="*60)
    print(f"\nProduct:  {highest.product}")
    print(f"Code:     {highest.code}")
    print(f"Country:  {highest.country}")
    print(f"Quantity: {highest.quantity}")
    print(f"Cost:     R{highest.cost}")
    print(f"\n💰 {highest.product} is now ON SALE!")
    print("="*60 + "\n")


#============= Main Menu =============

def main_menu():

    read_shoes_data()

    while True:
        print("\n" + "="*45)
        print("SHOE INVENTORY MENU".center(45))
        print("="*45)
        print("  1 - View All Shoes")
        print("  2 - Search Shoe")
        print("  3 - Restock Lowest Quantity Shoe")
        print("  4 - Value Per Item")
        print("  5 - Highest Quantity (For Sale)")
        print("  6 - Capture New Shoe")
        print("  7 - Exit")
        print("="*45 + "\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all()

        elif choice == "2":
            search_shoe()

        elif choice == "3":
            re_stock()

        elif choice == "4":
            value_per_item()

        elif choice == "5":
            highest_qty()

        elif choice == "6":
            capture_shoes()

        elif choice == "7":
            print("\n✓ Goodbye!\n")
            break

        else:
            print("\n✗ Invalid choice. Please try again.\n")


#============= Required Python Entry-Point =============

if __name__ == "__main__":
    main_menu()