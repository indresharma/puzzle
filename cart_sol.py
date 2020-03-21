'''
a | 50 | 3 for 130
b | 30 | 2 for 45
c | 20
d | 15

ti = total number of item in a category
du = discounted units (units at which discounts is available)
sp = special price
up = unit price
'''

#scanning the items
cartstr = input().upper()
cart = {k: cartstr.count(k) for k in cartstr}

# AVAIABLE PRODUCTS
prod = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

# THIS WEEKS DISCOUNT
discounted_items = {
    'A': {
        'du': 3,
        'sp': 130,
    },
    'B': {
        'du': 2,
        'sp': 45,
    }
}

# CHECK IF PRODUCTED IS DISCOUNTED
def is_discounted(key):
    if key in discounted_items:
        return True

# TO GET THE TOTAL PRICE FOR A PROD IF DISCOUNT IS APPLICATBLE
def discounted_group_total():
    discounted = ti//du*sp
    normal = (ti % du)*up
    return discounted+normal


total_price=0
for k,v in cart.items(): 
    #CHECKING IF WE HAVE A PRICE FOR SCANNED PROD
    if k in prod:
        #CHECKING IF THE PROD IS DISCOUNTED
        if is_discounted(k):
            ti = cart[k]
            up = prod[k]
            sp = discounted_items[k]['sp']
            du = discounted_items[k]['du']
            price = discounted_group_total()
            
        else:
            up = prod[k]
            ti = cart[k]
            price = ti*up
        total_price+=price
           
    else:
        print("Product {} is not available".format(k))
    
    print("Item {} | Quantity {}".format(k,v))
    
print("Total Price: ", total_price)
