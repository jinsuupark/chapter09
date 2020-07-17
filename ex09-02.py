def getSubjectTotal(student):
    subject_total = 0
    for subject in student:
        subject_total += subject
    return subject_total

def printTotalAvg(subject_total, student):
    subjects = len(student)  # 과목의 수
    avg = subject_total / subjects
    print(f"총점 {subject_total}, 평균 {avg:.2f}")
    return subjects

def main():

    #기존값을 삭제하고, 새로운 값으로 대체(삽입)
    nums = list(range(10))
    nums[2:5] = [20,30,40]
    print(nums)
    nums[6:8] = [60,70]
    # nums[6:8] = [60,70,80,90]
    print(nums)


    # Insert 방법
    nums[6:6] = [100]
    print(nums)

    str1 = "hello"
    str2 = "world"
    str3 = str1 + str2
    print(type(str3))
    str4 = str1*3
    print(type(str4))

    #리스트의 요소
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 11]
    listadd = list1 + list2
    print(listadd)
    print(type(listadd))
    listmulti = list2*3
    print(listmulti)
    print(type(listmulti))

    #이중 리스트
    lol =[
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]

    print(lol[0])
    print(lol[2][1])

    #순회
    for sub in lol:
        for item in sub:
            print(item, end='')
        print()




# 3학생 성적 평균 구하기

    score = [
        [88, 76, 92, 98],
        [65, 70, 58, 82],
        [82, 80, 78, 88]
    ]

    total = 0
    totalsub = 0

    for student in score:
        subject_total = getSubjectTotal(student)

        subjects = printTotalAvg(subject_total, student)

        total += subject_total
        totalsub += subjects
    total_avg = total / totalsub
    print(f"전체평균 {total_avg:.2f}")
    # 계산하여 변수에 담고 변수를 출력하는것이 권장됨




main()