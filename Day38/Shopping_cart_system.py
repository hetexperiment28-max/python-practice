class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print("Name :", self.name)
        print("Price :", self.price)
        print("-" * 15)
    
class Cart:

    def __init__(self):
        self.products = []

    def show_products(self):
        if not self.products:
            print("Cart is empty!")
            return
        
        print("--- Cart Contents ---")
        for s in self.products:
            s.show_info()

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            print("Product Added in cart")

        else:
            print("Product already in cart")

    def remove_product(self, name):
        
        for s in self.products:
            if s.name.lower() in name.lower():
                self.products.remove(s)
                print(name, "is Removed succesfully")
                return
            
            else:
                print("product not in cart")

    def total_price(self):
        total = 0
        for s in self.products:
            total += s.price
        
        print("Total cart price: ", total)

    
    def search_product(self, name):

        for s in self.products:
            if name.lower() == s.name.lower():
                return ("Found in cart for price :", s.price)
                
        return("not found in cart")


    def count_products(self):
        count = len(self.products)
        print("Total Products :", count)
    

cart = Cart()
cart.add_product(Product("Mouse",500))
cart.add_product(Product("Keyboard",1200))
cart.add_product(Product("Monitor",8500))
cart.add_product(Product("Headphones",2000))
cart.add_product(Product("USB Cable",250))


while True :
    
    print(" 1. Show products", "\n", "2. Search Product", "\n", "3. Total price", "\n",
          "4. Remove Product", "\n", "5. Product Count", "\n", "6. Exit", "\n")

    try:
        in_choice = False
        choice = int(input("Enter menu choice (1-6):"))
        if 1<= choice <= 6:
            in_choice = True
        if not in_choice:
            print("choice not in menu")
            continue
    except ValueError:
        print("Enter valid input in integer range (1-6).")
        continue


    match(choice):
        
        case 1:
            cart.show_products()
    
        case 2:     
            name = input("Enter product name to search:")
            print(cart.search_product(name))

        case 3:
            cart.total_price()

        case 4:
            product_name = input("Enter product name to remove :")
            cart.remove_product(product_name)

        case 5:
            cart.count_products()

        case 6:
            print("Exiting...")
            break

