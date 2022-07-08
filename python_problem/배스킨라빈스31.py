import random

numlist = []
index = 0

for i in range(31):
    numlist.append(i+1)

class player:
    def __init__(self):
        self.num = 0

    def playerturn(self):
        global index
        while True:
            self.num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
            
            try:
                self.num = int(self.num)
                is_digit = True
            except ValueError:
                is_digit = False

            if not is_digit:
                print("정수를 입력하세요")
            elif self.num < 4 and self.num > 0:
                break
            else:
                print("1, 2, 3 중 하나를 입력하세요")

        for i in range(self.num):
            if index < 31:
                print("player : {0}".format(numlist[index]))
                index += 1
            else:
                self.result = True
                return False
        
        return True

class computer:
    def __init__(self):
        self.num = 0

    def computerturn(self):
        global index
        self.num = random.randint(1, 3)

        for i in range(self.num):
            
            if index < 31:
                print("computer : {0}".format(numlist[index]))
                index += 1
            else:
                self.result = True
                return False
        
        return True

player = player()
computer = computer()

while True:
    if computer.computerturn() != True or player.playerturn() != True:
        break

if player.result:
    print("computer win!")

else:
    print("player win!")
