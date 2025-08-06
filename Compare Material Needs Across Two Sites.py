# ✅ 9. Compare Material Needs Across Two Sites
# You’re given two dicts for Site A and Site B with required material quantities.
# Return a dict
# showing which site needs more of each item.

def compare_material_needs(site_a: dict, site_b: dict) -> dict:
    result = {}
    all_items = set(site_a.keys()).union(site_b.keys())

    for item in all_items:
        qty_a = site_a.get(item, 0)
        qty_b = site_b.get(item, 0)
        if qty_a > qty_b:
            result[item] = 'A'
        elif qty_b > qty_a:
            result[item] = 'B'
    return result


site_a = {'cement': 10, 'sand': 50}
site_b = {'cement': 8, 'sand': 60}

print(compare_material_needs(site_a, site_b))
# Output: {'cement': 'A', 'sand': 'B'}
