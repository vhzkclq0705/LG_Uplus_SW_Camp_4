def calculate(n):
    return n // 7 + (1 if n % 7 else 0)

n = int(input("피자를 나눠먹을 사람의 수: "))
while n < 1 or n > 100:
    print("1과 100 사이의 정수를 입력해주세요.")
    n = int(input("피자를 나눠먹을 사람의 수: "))

result = calculate(n)
print(f'7명이 최소 한 조각씩 먹기 위해서 최소 {result}판이 필요합니다.')