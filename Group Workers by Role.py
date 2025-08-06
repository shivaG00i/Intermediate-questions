# ✅ 8. Group Workers by Role
# Given a list of workers, each with a role,
# return a dict that groups them by role.

def group_by_role(workers: list[dict]) -> dict:
    grouped = {}
    for worker in workers:
        role = worker['role']
        name = worker['name']
        grouped.setdefault(role, []).append(name)
    return grouped

# ✅ Explanation:
# setdefault(role, []) ensures each role starts with an empty list if not already in the dict.
# Then it appends the worker's name to the appropriate list.

Then it appends the worker's name to the appropriate list.

workers = [
    {'name': 'Raj', 'role': 'painter'},
    {'name': 'Ali', 'role': 'plumber'},
    {'name': 'Sara', 'role': 'painter'}
]

print(group_by_role(workers))
# Output: {'painter': ['Raj', 'Sara'], 'plumber': ['Ali']}

