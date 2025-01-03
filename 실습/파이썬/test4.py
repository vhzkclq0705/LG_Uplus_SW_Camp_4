def fail_validation():
    print("잘못된 정수를 입력하였습니다. 프로그램을 종료합니다.")
    exit()

def sqrt(n, t):
    return n ** t

n = int(input("처음 세균의 마리수를 입력하세요: "))
if n < 1 or n > 10: fail_validation()
t = int(input("경과한 시간을 입력하세요: "))
if t < 1 or t > 15: fail_validation()

result = sqrt(n, t)

print(f'처음엔 {n}마리, {t}시간 후엔 {result}마리가 됩니다. 따라서 {result}를 return합니다.')