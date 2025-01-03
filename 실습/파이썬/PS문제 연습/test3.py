def validate_age(age):
    if age <= 0 or age > 120:
        print("잘못된 나이를 입력하였습니다. 프로그램을 종료합니다.")
        exit()

def calcuate_age(age):
    return 2023 - age

age = int(input())
validate_age(age)
result = calcuate_age(age)

print(f'2022년 기준 {age}살이므로 {result}생입니다.')