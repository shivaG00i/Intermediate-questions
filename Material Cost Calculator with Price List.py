# ✅ 6. Material Cost Calculator with Price List
# You’re given a price list and a quantity dictionary.
# Return total cost.



def calculate_material_cost(prices: dict, quantities: dict) -> int:
    total = 0
    for item, qty in quantities.items():
        price = prices.get(item, 0)
        total += price * qty
    return total


prices = {'cement': 300, 'sand': 50, 'bricks': 5}
quantities = {'cement': 2, 'bricks': 100}

print(calculate_material_cost(prices, quantities))  # Output: 1100

# Output: 300*2 + 5*100 = 1100
