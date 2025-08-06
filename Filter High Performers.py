# ✅ 5. Filter High Performers
# From a dictionary of workers and their total work,
# return names of those who worked more than
# a given threshold.


def filter_high_performers(work_data: dict, threshold: int) -> list:

    list1=[]
    for i,j in work_data.items():
        if j>threshold:
            list1.append(i)
    print(list1)


work_data = {'Ravi': 120, 'Mohan': 90, 'Ali': 150}
threshold = 100

print(filter_high_performers(work_data,threshold))
# Output: ['Ravi', 'Ali']
