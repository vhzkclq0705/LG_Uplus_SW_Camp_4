def calcuate_age(age):
    return 2023 - age

age = int(input("나이를 입력하세요: "))
while not (0 < age <= 120):
    age = int(input("나이를 입력하세요: "))

result = calcuate_age(age)
print(f'2022년 기준 {age}살이므로 {result}생입니다.')