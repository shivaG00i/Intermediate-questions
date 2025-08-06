# ✅ 10. List Top N Laborers
# Given a dictionary of laborers and total bricks laid, return top N names.

def top_n_laborers(work_data: dict, n: int) -> list:
    sorted_workers = sorted(work_data.items(), key=lambda x: x[1], reverse=True) # reverse based on value x[1]
    return [name for name, _ in sorted_workers[:n]]



work_data = {'Raj': 500, 'Ali': 700, 'Sara': 450}
print(top_n_laborers(work_data, 2))  # Output: ['Ali', 'Raj']


