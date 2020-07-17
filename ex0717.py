def findMin(*numbers):
    min = numbers[0]
    for num in numbers[1:]:
        if num> min:
            min = num
        return min

def findMax(*numbers):
    max = numbers[0]
    for num in numbers[1:]:
        if num>max:
            max = num
    return max

lst = [1, 3, 5, 6, 10, 22]

min = min(lst)
max = findMax(*lst)
# * 역할:
print(min)
print(max)
