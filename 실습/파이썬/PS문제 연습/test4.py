def sqrt(n, t):
    return n ** t

n = int(input("처음 세균의 마리수를 입력하세요: "))
while not (1 <= n <= 10):
    print("1과 10 사이의 정수를 입력해주세요.")
    n = int(input("처음 세균의 마리수를 입력하세요: "))
    
t = int(input("경과한 시간을 입력하세요: "))
while not (1 <= t <= 15):
    print("1과 15 사이의 정수를 입력해주세요.")
    t = int(input("경과한 시간을 입력하세요: "))

result = sqrt(n, t)
print(f'처음엔 {n}마리, {t}시간 후엔 {result}마리가 됩니다. 따라서 {result}를 return합니다.')