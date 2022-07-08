student_list = []

class Student:
    def __init__(self, name, score1, score2):
        self.name = name
        self.mid_score = score1
        self.final_score = score2
        self.avg = (self.mid_score + self.final_score)/2
        self.grade = "default"

    def getGrade(self):
        if self.avg >= 90:
            self.grade = "A"

        elif self.avg >= 80:
            self.grade = "B"

        elif self.avg >= 70:
            self.grade = "C"
        
        else:
            self.grade = "D"

class IsExist(Exception):
    def __init__(self):
        super().__init__("Already exist name!")

class NotPositiveNumber(Exception):
    def __init__(self):
        super().__init__("Score is not positive integer!")

class NoStudent(Exception):
    def __init__(self):
        super().__init__("No student data!")

class NoCheckGrade(Exception):
    def __init__(self):
        super().__init__("There is a student who didn't get grade.")

class NoExist(Exception):
    def __init__(self):
        super().__init__("Not exist name!")

##############  menu 1
def Menu1(name, score1, score2) :
    student = Student(name, score1, score2)
    student_list.append(student)

##############  menu 2
def Menu2(student_list) :
    for i in student_list:
        if i.grade == "default":
            i.getGrade()

# ##############  menu 3
def Menu3(student_list) :
    print("-----------------------------")
    print("name\tmid\tfinal\tgrade")
    print("-----------------------------")
    for i in student_list:
        print("{0}\t{1}\t{2}\t{3}".format(i.name, i.mid_score, i.final_score, i.grade))

##############  menu 4
def Menu4(name):
    for i in student_list:
        if i.name == name:
            student_list.remove(i)


#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            name, score1, score2 = input("Enter name mid-score final-score : ").split()
        except ValueError:
            print("Num of data is not 3!")
        else:
            try: 
                for i in student_list:
                    if i.name == name:
                        raise IsExist

                score1 = int(score1)
                score2 = int(score2)
            except ValueError:
                print("The score is not integer!")
            except IsExist as e:
                print(e)
            else:
                try:
                    if score1 < 0 or score2 < 0:
                        raise NotPositiveNumber
                except NotPositiveNumber as e:
                    print(e)
                else:
                    Menu1(name, score1, score2)
        
    
    elif choice == "2" :
        try:
            if student_list == []:
                raise NoStudent
        except NoStudent as e:
            print(e)
        else:
            Menu2(student_list)
            print("Grading to all students")


    elif choice == "3" :
        try:
            if student_list == []:
                raise NoStudent
        except NoStudent as e:
            print(e)
        
        else:
            try:
                for i in student_list:
                    if i.grade == "default":
                        raise NoCheckGrade
            except NoCheckGrade as e:
                print(e)
            else:
                Menu3(student_list)

    elif choice == "4" :
        try:
            if student_list == []:
                raise NoStudent
        except NoStudent as e:
            print(e)
        else:
            try:
                student_name = input("Enter the name to delete: ")
                
                for i in student_list:
                    if i.name == student_name:
                        Menu4(student_name)
                        print("{0} student information is deleted.".format(student_name))
                        break
                    else:
                        raise NoExist
            except NoExist as e:
                print(e)

    elif choice == "5" :
        print("Exit Program!")
        exit()

    else :
        print("Wrong number. Choose again.")