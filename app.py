products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Headphones", "price": 2000},
    {"id": 3, "name": "Keyboard", "price": 1500},
    {"id": 4, "name": "Mouse", "price": 800}
]


def view_products():
    print("\n--- Available Products ---")

    for product in products:
        print(
            f'{product["id"]}. {product["name"]} '
            f'- Rs. {product["price"]}'
        )


def search_products():
    keyword = input("Enter product name: ").strip().lower()

    results = [
        product for product in products
        if keyword in product["name"].lower()
    ]

    if results:
        for product in results:
            print(f'{product["name"]} - Rs. {product["price"]}')
    else:
        print("No products found.")


def main():
    while True:
        print("\n=== E-Commerce Store ===")
        print("1. View Products")
        print("2. Search Products")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_products()
        elif choice == "2":
            search_products()
        elif choice == "3":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
