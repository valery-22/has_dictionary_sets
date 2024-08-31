def exclusive_products(inventory1, inventory2):
    set1 = set(product.upper() for product in inventory1)
    set2 = set(product.upper() for product in inventory2)
    intersection = set1 & set2
    only_in_inventory1 = set1 - set2
    only_in_inventory2 = set2 - set1
    
    return (sorted(list(only_in_inventory1)), sorted(list(only_in_inventory2))) # implement this
    

inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])