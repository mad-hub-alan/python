
def get_average(marks):
    total = 0
    for i in range(len(marks)):
        total += marks[i]
    return total/len(marks)

def get_pass_count(marks):
    count = 0
    for i in range(len(marks)):
        if marks[i] >= 35:
            count += 1
    return count


def get_result(marks):
    passed_subjects = get_pass_count(marks)
    if passed_subjects == len(marks):
        print('Result : PASS')
        average = get_average(marks)
        avg = int(average)
        if avg >= 90:
            print('Average : '+str(average))
            print('Grade : A')
        elif avg >= 75:
            print('Average : ' + str(average))
            print('Grade : B')
        elif avg >= 60:
            print('Average : ' + str(average))
            print('Grade : C')
        else:
            print('Average : ' + str(average))
            print('Grade : D')
    else:
        print('Result : FAIL')
        print('Failed Subject(s) : '+str(len(marks)-passed_subjects))



eng = 82
mat = 90
sci = 100

marks = [eng,mat,sci]

# print(get_pass_count(marks))
# print(get_average(marks))
get_result(marks)

