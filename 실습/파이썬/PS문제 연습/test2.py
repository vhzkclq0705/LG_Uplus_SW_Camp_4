def validate_nums(num):
    if num < 0 or num > 10000:
        print('잘못된 정수를 입력하였습니다. 프로그램을 종료합니다.')
        exit()

def isEqual(num1, num2):
    return num1 == num2

num1 = int(input('첫 번째 정수를 입력하세요: '))
validate_nums(num1)
num2 = int(input('두 번째 정수를 입력하세요: '))
validate_nums(num2)

result = isEqual(num1, num2)
print(f'num1이 {num1}이고 num2가 {num2}이므로 {"같습니다" if result else "다릅니다"}. 따라서 {1 if result else -1}을 return합니다.')