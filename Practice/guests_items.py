allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}

def totalItems(guests, item):
    totalCount = 0
    for k, v in guests.items():
        totalCount = totalCount + v.get(item,0)
    return totalCount

print('Number of things being brought:')
print('- Apples ' + str(totalItems(allGuests,'apples')))
print('- Cups ' + str(totalItems(allGuests,'cups')))
print('- Cakes ' + str(totalItems(allGuests,'cakes')))
print('- Ham Sandwiches ' + str(totalItems(allGuests,'ham sandwiches')))
print('- Apple Pies ' + str(totalItems(allGuests,'apple pies')))

#Number of things being brought:
#- Apples 7
#- Cups 3
#- Cakes 0
#- Ham Sandwiches 3
#- Apple Pies 1
