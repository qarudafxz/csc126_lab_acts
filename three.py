import math 

def bubble_sort(marks):
    n = len(marks)
    for i in range(n - 1):
        flag = False
        for j in range(n - 1 - i):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                flag = True
        if not flag:
            break
    return marks

def get_average(marks):
    if marks:
        return sum(marks) / len(marks)
    return 0

def get_five_marks(mark, marks):
    if mark != 0:
        marks.append(mark)

def get_equi_grade(mark):
    if mark > 100:
        return "Invalid grade"
    elif mark < 60:
        return 5.00
    elif mark < 65:
        return 4.00
    elif mark < 70:
        return 3.00
    elif mark < 75:
        return 2.75
    elif mark < 80:
        return 2.00
    elif mark < 85:
        return 1.75
    elif mark < 90:
        return 1.50
    elif mark < 95:
        return 1.25
    else:
        return 1.00

def main():
    marks = []
    for _ in range(5):
        x = eval(input("Enter your grade: "))
        get_five_marks(x, marks)

    sorted_marks = bubble_sort(marks)
    print("Sorted Grades:", sorted_marks)
    ave = get_average(marks)
    print("Your average on each grade you entered:", ", ".join(map(str, [get_equi_grade(mark) for mark in sorted_marks])))

if __name__ == "__main__":
    main()
