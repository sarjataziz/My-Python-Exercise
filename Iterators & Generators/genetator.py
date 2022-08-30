def current_beat():
	nums = (1,2,3,4,5,6,7,8,9,10)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1

print(current_beat())
