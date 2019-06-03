# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))


display_inventory(stuff)


def add_to_inventory(inventory: dict, loot: dict):
    for k in loot:
        inventory.setdefault(k, 0)
        inventory[k] += 1



dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(stuff, dragonloot)
print('_________________________')
display_inventory(stuff)

