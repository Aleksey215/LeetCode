# strs = ["flower", "flow", "flight"]
strs = ["dog", "racecar", "car"]

strs_lens = list(map(len, strs))
temp = strs[strs_lens.index(min(strs_lens))]
strs.remove(temp)

check = 0
while True:
    for string in strs:
        if temp in string[:len(temp)]:
            check += 1
    if check == len(strs):
        print(temp)
        break
    else:
        temp = temp[: len(temp) - 1]
        check = 0
