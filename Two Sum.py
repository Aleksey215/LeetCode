nums = [2,7,11,15]
target = 9
out = list()
for index, num in enumerate(nums):
    check = nums.copy()
    check.remove(num)
    if target - num in check:
        out.append(index)
print(out)