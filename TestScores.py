
def test_score():
    print('''
        Dear student,
        This is the moment you have been waiting for since you took your mocks,
        Please follow the intructions on the screeen and find out what your
        grade is. It will also have detailed instructions on how to improve.
        Remember "Better never stops".
        Your sincerly, Mr Tompson
        P.S if your grade in unexpectly low don't complain, study harder, no
        tests will be remarked''')
    name= str(input("What's your name?"))
    Form = str(input("What form are you in?"))
    ExpectedGrade = str(input("What grade do you expect to get?"))
    mark = int(input("What did you score in test?"))
    if (mark <= 10):
        print("You," + name + " expected to get a grade " + ExpectedGrade + " and got a Grade 1 ")
        ActualGrade=1
    elif (mark >= 11 and mark <= 20 ): 
        print("You," + name + " expected to get a grade " + ExpectedGrade + " and got a Grade 2 ")
        ActualGrade=2
    elif(mark >= 21 and mark <= 30):
        print("You," + name + " expected to get a grade " + ExpectedGrade + " and got a Grade 3 ")
        ActualGrade=3
    elif (mark>=31 and mark <= 40):
        print("You," + name + " expected to get a grade " + ExpectedGrade + " and got a Grade 4 ")
        ActualGrade=4
    elif (mark>=41 and mark<= 50):
        print("You," + name + " expected to get a grade " + ExpectedGrade + " and got a Grade 5 ")
        ActualGrade=5
    elif (mark>=51 and mark <= 60):
        print("You," + name + " expected to get a grade " + ExpectedGrade + " and got a Grade 6 ")
        ActualGrade=6
    elif(mark>=61 and mark <= 70):
        print("You," + name + " expected to get a grade " + ExpectedGrade + " and got a Grade 7 ")
        ActualGrade=7
    elif(mark>=71 and mark <=80):
        print("You," + name + " expected to get a grade " + ExpectedGrade + " and got a Grade 8 ")
        ActualGrade=8
    elif(mark>=81 and mark <=90):
        print("You," + name + " expected to get a grade " + ExpectedGrade + " and got a Grade 9 ")
        ActualGrade=9
    else:
        print("Please enter a valid number")
        test_score()
    if ActualGrade == ExpectedGrade:
        print("You reached your goal. Well Done")
    elif ActualGrade>=ExpectedGrade:
        print("You have done better that your predicted grade. Well Done")
    elif ActualGrade<=ExpectedGrade:
        print("You have done worse than your predicted grade. You need to study more")
    else:
        print("You have managed to break this program, ByeBYe")

test_score()

