#튜플
score = 88, 95, 70, 100, 99
print(score)

score = 88  #튜플X
print(score)

score = 88, #튜플O
print(score)

score = (88)    #튜플X
print(score)

score = (88,)   #튜플O
print(score)

#튜플 Unpack
names = "이순신", "김유신", "강감찬"
lee, kim, kang = names
print(lee)
print(kim)
print(kang)
#same as
lee, kim, kang = "이순신", "김유신", "강감찬"
print(lee)
print(kim)
print(kang)


a, b = 12, 34
print(a,b)

a, b = b, a
print(a,b)

#return 10, 20  가능하다
#개수를 맞추는것이 중요하다
#함수로 튜플을 리턴하면 여러값을 받을수있음.

import time
#모듈
def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print("지금은 %d시 %d분 입니다"%(result[0],result[1]))

hour, minute = gettime()
print(f"지금은 {hour}시 {minute}분 입니다")

d, m =divmod(7,3)
print("목",d)
print("나머지",m)

score = [88,95,70,100,99]
tu = tuple(score)
print(tu)

li =list(tu)
li[0]=100
print(li)
#튜플에서 수정을 하고싶을때 리스트로 만든다음
#수정 후 다시 튜플로 만들면된다.