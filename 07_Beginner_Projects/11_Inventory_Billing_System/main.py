"""Project 11: Inventory and Billing System
A small console billing demo. Stock changes while this program is running.
Concepts: dictionaries, loops, arithmetic and input validation.
"""

PRODUCTS = {
    "P101": {"name": "Pen", "price": 10.0, "stock": 50},
    "P102": {"name": "Notebook", "price": 45.0, "stock": 30},
    "P103": {"name": "Pencil", "price": 5.0, "stock": 60},
    "P104": {"name": "Eraser", "price": 8.0, "stock": 40},
}
TAX_RATE = 0.05


def show_inventory():
    print("\nID    Product       Price    Stock")
    for product_id, product in PRODUCTS.items():
        print(f"{product_id:<5} {product['name']:<13} Rs.{product['price']:<6.2f} {product['stock']}")


def create_bill():
    cart = {}
    while True:
        show_inventory()
        product_id = input("\nEnter product ID, or 0 to finish: ").strip().upper()
        if product_id == "0":
            break
        if product_id not in PRODUCTS:
            print("Product ID not found.")
            continue

        product = PRODUCTS[product_id]
        already_selected = cart.get(product_id, 0)
        available = product["stock"] - already_selected
        if available <= 0:
            print("No more stock available for this product.")
            continue
        try:
            quantity = int(input(f"Quantity (available: {available}): "))
        except ValueError:
            print("Enter a whole number.")
            continue
        if quantity <= 0 or quantity > available:
            print("Quantity must be positive and within available stock.")
            continue
        cart[product_id] = already_selected + quantity
        print("Added to cart.")

    if not cart:
        print("Cart is empty. No bill created.")
        return

    subtotal = 0.0
    print("\n================ BILL ================")
    for product_id, quantity in cart.items():
        product = PRODUCTS[product_id]
        line_total = product["price"] * quantity
        subtotal += line_total
        print(f"{product['name']:<13} x {quantity:<3} Rs. {line_total:.2f}")
    tax = subtotal * TAX_RATE
    print("--------------------------------------")
    print(f"Subtotal:                         Rs. {subtotal:.2f}")
    print(f"Tax (5%):                         Rs. {tax:.2f}")
    print(f"Grand total:                      Rs. {subtotal + tax:.2f}")
    print("======================================")

    for product_id, quantity in cart.items():
        PRODUCTS[product_id]["stock"] -= quantity
    print("Bill complete. Stock updated for this session.")


def main():
    while True:
        print("\n=== INVENTORY AND BILLING ===")
        print("1. View inventory")
        print("2. Create bill")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_inventory()
        elif choice == "2":
            create_bill()
        elif choice == "3":
            print("Billing program closed.")
            break
        else:
            print("Choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
