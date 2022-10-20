def twoSum(nums, target):
    # create a dictionary with the number as key and it's position as value.
    positions = {x: i for i, x in enumerate(nums)}
    for i in range(len(nums)):
        # find the deference between the first number of the list and check if that number exists in the list
        # and go on until you find the difference in the dictionary
        difference = target - nums[i]
        # to keep the program going until the difference exists in the list
        try:
            # to check if the difference value position and index of the are the same
            # in that case both the values will be referring the same number so that bug must be avoided
            if positions[difference] == i:
                continue
            else:
                return i, positions[difference]
        except KeyError:
            print('KeyError')
            pass
        else:
            continue

result = twoSum([3, 2, 4], 6)
print(result)
