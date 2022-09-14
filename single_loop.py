def twoSum(nums, target):
    positions = dict()
    for i, x in enumerate(nums):
        # add the position of the each number into the dictionary
        positions[x] = i
        # find the deference
        difference = target - x
        # if the difference is in the keys(already added number)
        if difference in positions.keys():
            # returns the current number's position and the position of the already added matched number's position
            return i, positions[difference]

result = twoSum([1,2,3,4,5], 5)
print(result)
