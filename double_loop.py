def twoSum(nums, target):
    for x in range(len(nums)):
        first_digit = nums[x]
        for y in range(len(nums)):
            second_digit = nums[y]
            total = first_digit + second_digit
            if target == total:
                return x,y 

result = twoSum([1,2,3,4,5], 5)
print(result)
