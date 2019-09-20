def second_lowest(gradebook):
    temp_students = []
    temp_second = None
    gradebook.sort(key=lambda i: i[1])
    lowest_grade = gradebook[0][1]

    for i in gradebook:
        if i[1] > lowest_grade:
            temp_second = i[1]
            break

    for i in gradebook:
        if i[1] == temp_second:
            temp_students.append(i[0])
        if i[1] > temp_second:
            break

    temp_students.sort()

    for each in temp_students:
        print(each)
