# Set

## Introduction
A set is a data structure that does not keep the elements in any order, but it is very efficient when searching for an element in the set. 

## Python implementation
In python a set is implemented by using the set keyword. You add and remove by using these same keywords. 

## Common operations efficiency
| Common Queue Operation | Big O notation efficiency |
| ---------------------- | --------------------------|
| add | O(1)
| remove | O(1)
| memebr | O(1)
| size | O(1)

## Example
An example of how a set might be used is in a collection of cards.
Lets say you are a Pokemon enthusiast and collect Pokemon card, and want to keep track of which one you have. In this case you could try to add duplicates as much as you can, but it will never be added. This is good because you just want to know which ones you have and a set is perfect for searching for membership. 

## Probelm
Create a set of baseball cards. If the user tries to buy a card that he or she already has display a message to the user. Represent the cards with a string of a baseball player. 

### Possible Solution

```
collection = set()

again = "y"

while again == "y":
    card = input("Enter the name of the player: ")
    if card in collection:
        print("Card already in the collection")
    collection.add(card)
    again = input("Want to add another card?(y,n)")

print(collection)

```

