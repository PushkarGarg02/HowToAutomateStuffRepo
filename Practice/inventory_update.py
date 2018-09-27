dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']

inventory = {'gold coin': 38, 'dagger': 20}

def addToInventory(inventory, addedItems):
    for newItem in dragonLoot:
        inventory.setdefault(newItem, 0)
        inventory[newItem] += 1
        
addToInventory(inventory,dragonLoot)
    
for k,v in inventory.items():
    print(str(v)+ ' ' +k)
