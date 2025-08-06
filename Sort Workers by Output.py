# ✅ 7. Sort Workers by Output
# Given a list of worker records (dicts with name and total output),
# return them sorted by output
# descending.

def sort_workers_by_output(workers: list[dict]) -> list[dict]:
    return sorted(workers, key=lambda worker: worker['output'], reverse=True) # based on output we have to work



workers = [{'name': 'A', 'output': 120}, {'name': 'B', 'output': 200}]
print(sort_workers_by_output(workers))
# Output: [{'name': 'B', 'output': 200}, {'name': 'A', 'output': 120}]

