'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

'''
# Time complexity n^2
# Space complexity 1
def add_two_sum1(nums, target):
    nums_size = len(nums)
    for ii in range(0, nums_size):
        for jj in range(ii, nums_size):
            if ((nums[ii] + nums[jj]) == target):
                return [ii, jj]
    return None

# Time complexity n
# Space complexity n (depend on the nums)
def add_two_sum2(nums, target):
    nums_size = len(nums)
    num_dict = dict()
    for ii in range(nums_size):
        if nums[ii] in num_dict.keys():
            return [num_dict[nums[ii]], ii]
        else:
            num_dict[target - nums[ii]] = ii
    return None


if __name__ == '__main__':
    print (add_two_sum1([2, 7, 11, 15], 9))
    print (add_two_sum1([11, 2, 15, 7], 9))
    print (add_two_sum2([2, 7, 11, 15], 9))
    print (add_two_sum2([11, 2, 15, 7], 9))
