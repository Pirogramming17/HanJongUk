num = 0
numlist = []
index = 0

for i in range(31):
    numlist.append(i+1)

class player:
    def __init__(self, name):
        self.name = name

    def playerturn(self):
        global index
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
            if index < 31:
                print("player{0} : {1}".format(self.name , numlist[index]))
                index += 1
            else:
                self.result = True
                return False
        
        return True

playerA = player("A")
playerB = player("B")

while True:
    if playerA.playerturn() != True or playerB.playerturn() != True:
        break

# if playerA.result:
#     print("playerB win!")

# else:
#     print("playerA win!")
