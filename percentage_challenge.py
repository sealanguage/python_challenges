n = int(input())     # n is number of students
    student_marks = {}

    for grade in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        # print("grade in loop ", grade)
    query_name = input()

    count = 0
    sum = 0

    for grade in line :
        grade = float(grade)
        sum = sum + grade
        # print("grade is ", grade)
        # print("scores is ", scores)
        # print("sum is ", sum)

        avg = sum/3
        print(avg)
        


    # print(scores)      # scores is list of grades for nth person
    # print(name)
    # print(student_marks)