# ✅ 1. Track Laborers and Their Daily Output
# You have a list of workers with their daily output (in bricks).
# Create a dictionary that maps each
# worker's name to their total output after D days.

def calculate_total_output(workers: list[dict], days: int) -> dict:
    if days < 0:
        raise ValueError("Days must be non-negative")
    result={} # output is a dictionary and in it we have key[name] and value[days output]
    for work in workers:
        name=work['name']
        output=work['daily_output']*days
        result[name]=output
    return result

workers = [{'name': 'Raj', 'daily_output': 50}, {'name': 'Ali', 'daily_output': 60}]
days = 5
# Output: {'Raj': 250, 'Ali': 300}

print(calculate_total_output(workers,days))