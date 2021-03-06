# Queue

## Introduction
A queue is a data structure that implements the first in first out principle. 

## Python implementation
In python a queue is implemented with a list. Appending when adding a new element to the queue (queuing), but poping the element in index 0 when removing (dequeuing). 

## Common operations efficiency
| Common Queue Operation | Big O notation efficiency |
| ---------------------- | --------------------------|
| enqueue | O(1)
| dequeue | O(n) (Assuming a dynamic array was used)
| dequeue| 0(1) (Assuming a linked list was used)
| size | O(1)
| empty | O(1)

## Example
A good exapmle of a queue is any kind of line. For example the line that is made in the Crossroads when trying to pay your food is a queue. Becaue the first one that makes it to the line is the first one that gets out(pays for his/her food.) 

```

class Line:

    def __init(self):
        self.people = []

    def new_person_in_line(self):
        name = input("Person's name: ")
        self.people.append(name)

    def person_paid_for_food(self):
        self.people.pop(0) 
```

## Probelm
Create a Queue with 5 Amazon order and dequeue them as you ship them. Display the order information after being dequeued.

### Possible Solution

```
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
```

[Go back to Home Page](0-welcome.md)