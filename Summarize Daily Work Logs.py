# ✅ 4. Summarize Daily Work Logs
# Given a list of daily logs (each with laborer name and bricks laid),
# summarize the total work
# done per laborer.


def summarize_work(logs: list[dict]) -> dict:

    result={}
    for i in logs:
        name=i['name']
        bricks=i['bricks']
        result[name] = result.get(name, 0) + bricks

    for resname,resbricks in result.items():
        print(f"{resname} has laid {resbricks} ")

    return result

logs = [{'name': 'Ravi', 'bricks': 50}, {'name': 'Ravi', 'bricks': 70}, {'name': 'Mohan', 'bricks': 100}]
# Output: {'Ravi': 120, 'Mohan': 100}

print(summarize_work(logs))
