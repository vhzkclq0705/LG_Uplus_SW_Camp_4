def calculate(n):
    return n // 7 + (1 if n % 7 else 0)

n = int(input("피자를 나눠먹을 사람의 수: "))
if n < 1 or n > 100:
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    exit()

result = calculate(n)
print(f'7명이 최소 한 조각씩 먹기 위해서 최소 {result}판이 필요합니다.')