#삽입
nums =[1,2,3,4]
nums[2]=[90,91,92]
print(nums)

list1 = [1,2,3,4,5]
list2 = [10,11]
list3 = list1 + list2 # 새로운 리스트를 리턴
print(list3)
list1.extend(list2) #기존 리스트 확장
print(list1)

#삭제

score = [88,98,70,100,99,88,78,50]
score.remove(100) #값 삭제
print(score)

del(score[2]) #인덱스 삭제
print(score)

score[1:4] = [] #범위 삭제
print(score)

#삭제 Pop
score = [88,98,70,100,99,88,78,50]
print(score.pop())
print(score.pop())
print(score.pop(1))
print(score)

#큐
score = [88,95,70,100,99]
score.append(50)
print('큐',score)
print('큐',score.pop(0))
print('큐',score)


#스택
score = [88,95,70,100,99]
score.append(50)

print('스택',score)
print('스택',score.pop())
print('스택',score)

# ans = input("결제 하시겠습니까?")
#
# if ans in ['yes','y','ok','e']:
#     print("결제를 진행합니다")
# else:
#     print("결제를 취소합니다")


#정렬 sort
score = [88,95,70,100,99]
score.sort()
print(score)

score.reverse()
print(score)


country = ["Korea", "japan", "CHINA", "america"]

country.sort()
print(country)
country.sort(key = str.lower) #본문에는 변화가 없음
print(country)


score = [88,95,70,100,99]
sorted_score = sorted(score)
print(score)
print(sorted_score)

sorted_score = sorted(score, reverse=True )
print(score)
print(sorted_score)



def main():
    country = ["korea" ,"japan", "China", "america"]

    newlist = [c.lower() for c in country]
    print(newlist)

    print([n for n in range(1,11) if n % 3 == 0])
    #n이 if문을 먼저가서 확인후 True 인경우만 앞으로옴
    
    
    for i in range(len(country)):
        country[i] =country[i].lower()
    country.sort()
    print(country)

    country = ["korea" ,"japan", "China", "america"]
    country.sort(key=str.lower)
    for c in country:
        print(c.lower(),end=",")




main()
