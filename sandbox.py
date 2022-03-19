class Queue:

    

    def __init__(self):
        self.orders = []

    def place_order(self): 
        # enqueue
        name = input("Enter item's name: ")
        price = int(input("Enter item's price"))

        self.orders.append(Order(name, price))

    def ship_order(self):
        # dequeue
        order = self.orders.pop(0)
        print(f"The item {order.name} that costed ${order.price} has been shiped")
        


class Order:
        def __init__(self, name, price):
            self.name = name
            self.price = price


orders = Queue()
orders.place_order()
orders.place_order()
orders.place_order()
orders.place_order()
orders.place_order()
orders.ship_order()
orders.ship_order()
orders.ship_order()
orders.ship_order()
orders.ship_order()

    
        
