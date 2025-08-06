# ✅ 2. Material Stock Checker
# You have a dictionary with material quantities. Write a function to check
# if all required materials
# are available in sufficient quantity.

def is_stock_sufficient(stock: dict, requirement: dict) -> bool:

    for material, quantity in requirement.items():
        if stock.get(material,0)<quantity:
            return False
        return True

stock = {'cement': 10, 'bricks': 500, 'sand': 20}
requirement = {'cement': 8, 'bricks': 400}
v=is_stock_sufficient(stock,requirement)
print(v)

# Output: True
