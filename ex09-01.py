nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = list(range(10)) # 똑같다.
print(nums[:] )
print(nums[2:5] )
print(nums[:4] )
print(nums[6:] )
print(nums[1:7:2] )

score = [88, 95, 70, 100, 99]
print(score[2])
score[2] = 55
print(score[2])


nums2 = nums
print(nums == nums2)
nums[1] = -1
print(nums)
print(nums2)
print(nums == nums2)

nums = list(range(10))
nums2 = list(range(10))
print(nums == nums2)

#독자적인 객체 별도의 객체를 만들기위해서 Sclicing 이용
nums2 = nums[:]
nums2[0] = -3   
print(nums2 == nums)