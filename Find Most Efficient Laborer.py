# ✅ 3. Find Most Efficient Laborer
# Given a list of laborers with total bricks laid,
# return the name of the one who worked the most.


def most_efficient_laborer(logs: list[dict]) -> str:
    top_worker = max(logs, key=lambda x: x['bricks']) #top_worker is dictionary and in max we are apssing whole logs
    return top_worker['name']



logs = [{'name': 'Ravi', 'bricks': 500}, {'name': 'Mohan', 'bricks': 700}]
print(most_efficient_laborer(logs))  # Output: 'Mohan'

# Output: 'Mohan'
