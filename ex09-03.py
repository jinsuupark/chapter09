nums = [1, 2, 3, 4]
nums.append(5)
print(nums)

nums[0]=2
print(nums)

nums.insert(2, 99)
print(nums)

import random

def rand(start,end):
    num =int(random.random()*(end-start+1))+start
    return num

def getRandomList(start,end,count):
    nums =[]
    for _ in range(count): # n 단순 루프만을 위한 변수 이름의 의미가없음   ---> _(언더바 하나) 로 대체
        r = rand(start,end)
        nums.append(r)
    return nums



nums = getRandomList(1,100,100)

l = [rand(1,100)  for _ in range(6)]

print(l)

print(nums)
print(len(nums))