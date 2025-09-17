# Import required classes (Product, Store)
import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450.0, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250.0, quantity=500),
    products.Product("Google Pixel 7", price=500.0, quantity=250),
]
best_buy = store.Store(product_list)


def list_products(s: store.Store):
    """ Uses get_all_products from store.Store and displays (prints) them
    indexed by number of product"""
    print("\n--- Products Available ---")
    i = 1
    for product in s.get_all_products():
        (print(f"{i}.", end="\t"), product.show())
        i += 1


def show_total(s: store.Store):
    """ Prints the total quantity in store using
     get_total_quantity() from store.Store"""
    print(f"\nTotal quantity in store: {s.get_total_quantity()}")


def make_order(s: store.Store):
    """ First displays available products (using get_all_products())
    from store.Store and indexed as in main.list_products. Then
    prompts the user to choose a product and the quantity to buy
    and uses the input to add the product to a shopping list
    """
    all_products = s.get_all_products()

    # Display available products
    list_products(s)
    print("-------")

    shopping_list = []
    while True:
        choice = input("\nWhich product # do you want?\n"
            "When you want to finish order, enter empty text. ")
        if choice.lower() == "":
            break

        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(all_products):
                print("Invalid product number.")
                continue

            qty = int(input("Enter quantity: "))
            shopping_list.append((all_products[idx], qty))
            print("Product added to the list!\n")

        except ValueError:
            print("Invalid input. Try again.")

    if shopping_list:
        try:
            total = s.order(shopping_list)  # uses Store.order()
            print(f"\nOrder made! Total payment: {total}")
        except Exception as e:
            print(f"Order failed: {e}")


def start(s: store.Store):
    """ Displays the user a menu of actions. Prompsts the
    user for a choice of that menu and then executes the
    desired action. Gets and uses the store object as aa
    parameter. Basic input protection is provided through the
    usual while loop"""
    actions = {
        "1": list_products,
        "2": show_total,
        "3": make_order,
    }

    while True:
        print("\n===== Store Menu =====")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "4":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice](s)
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    start(best_buy)
