num = 0

while True:
    num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
    
    try:
        num = int(num)
        is_digit = True
    except ValueError:
        is_digit = False

    if not is_digit:
        print("정수를 입력하세요")
    elif num < 4 and num > 0:
        break
    else:
        print("1, 2, 3 중 하나를 입력하세요")

for i in range(num):
    print("playerA :", i + 1)