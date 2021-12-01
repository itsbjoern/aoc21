import util

nums = util.get_nums(1)
print([num[1] > num[0] for num in zip(nums, nums[1:])].count(True))

print([num[1] + num[2] + num[3] > num[0] + num[1] + num[2] for num in zip(nums, nums[1:], nums[2:], nums[3:])].count(True))
