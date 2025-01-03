def validate_nums(num):
    while not (0 <= num <= 10000):
        print("1과 10,000 사이의 정수를 입력하세요.")
        num = int(input('정수를 입력하세요: '))
    return num

def isEqual(num1, num2):
    return num1 == num2

num1 = int(input('정수를 입력하세요: '))
validate_nums(num1)
num2 = int(input('정수를 입력하세요: '))
validate_nums(num2)

result = isEqual(num1, num2)
print(f'num1이 {num1}이고 num2가 {num2}이므로 {"같습니다" if result else "다릅니다"}. 따라서 {1 if result else -1}을 return합니다.')