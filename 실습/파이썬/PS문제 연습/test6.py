def validate_input(str, is_char):
    if is_char and (len(str) != 1 or not validate_lowercase(str)):
        return "알파벳은 소문자 하나만 입력해야 합니다."
    if not is_char and (not (1 <= len(str) <= 1000) or not validate_lowercase(str)):
        return "길이는 1 이상 1,000 이하여야 하며, 알파벳 소문자만 입력해야 합니다."
    return None

def validate_lowercase(str):
    for char in str:
        if not ("a" <= char <= "z"):
            return False
    return True

def convert_to_uppercase(str, char):
    return (str.replace(char, char.upper()), char in str)

while True:
    my_string = input("문자열 입력: ")
    error = validate_input(my_string, False)
    if not error: break
    print(error)

while True:
    alp = input("알파벳 하나 입력: ")
    error = validate_input(alp, True)
    if not error: break
    print(error)

new_string, flag = convert_to_uppercase(my_string, alp)
print(f'alp는 \"{alp}\"이고 my_string \"{my_string}\"에 {alp}는 {"있습니다" if flag else "없습니다"}. 따라서 \"{new_string}\"을 return 합니다.')