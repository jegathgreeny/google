def twoSum(nums, target):
    positions = {x: i for i, x in enumerate(nums) }
    for i in range(len(nums)):
        difference = target - nums[i]
        return i, positions[difference]

result = twoSum([1,2,3,4,5], 5)
print(result)
