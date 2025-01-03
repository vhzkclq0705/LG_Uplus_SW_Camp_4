from functools import reduce

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else reduce(lambda x, y: x * y, num_list)

num_list = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
result = solution(num_list)
print(result)