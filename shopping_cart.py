# shopping_cart.py

#from pprint import pprint
import time

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25},
    {"id":21, "name": "Organic Bananas", "department": "produce", "aisle": "Fruit", "price": 0.79, "price_per": 1}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

localtime = time.asctime( time.localtime(time.time()) )
total_price = 0
selected_ids = []
id_list = []
for i in products:
    id_list.append(i["id"])

while True:
    selected_id = input("Please input a product identifier or type 'Done': ").lower()
    if selected_id == "done":
        break
    while selected_id not in str(id_list):
        print("ID Not found.  Please try again.")
        break
    else:
        selected_ids.append(selected_id)
        #[p for p in selected_ids if str(p["price_per"])] == 1
        #pounds == input("# of Pounds").lower()

        
print("---------------------------------")
print("Green Foods Grocery")
print("www.Green-Foods-Grocery.com")
print("---------------------------------")
print("Checkout at: " + localtime)
print("---------------------------------")
print("SELECTED PRODUCTS:")

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    print("... " + matching_product["name"] + " (" + str('${:,.2f}'.format(matching_product["price"])) + ")")
    total_price = matching_product["price"]
    tax = total_price * 0.0875
    total_total = total_price + tax

print("---------------------------------")
print("SUBTOTAL: " + str('${:,.2f}'.format(total_price)))
print("TAX: " + str('${:,.2f}'.format(total_price*.0875)))
print("TOTAL: " + str('${:,.2f}'.format(total_price*1.0875)))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")