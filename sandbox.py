collection = set()

again = "y"

while again == "y":
    card = input("Enter the name of the player: ")
    if card in collection:
        print("Card already in the collection")
    collection.add(card)
    again = input("Want to add another card?(y,n)")

print(collection)
