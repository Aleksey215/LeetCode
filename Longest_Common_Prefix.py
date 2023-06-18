# strs = ["dog", "racecar", "car"]
strs = ["flower", "flow", "flight"]
test = list()
index = 0
ans = ''
if strs:
    while True:
        for string in strs:
            if index <= len(string) - 1:
                test.append(string[index])
            else:
                continue
        if len(set(test)) > 1:
            break
        ans += test[0]
        test.clear()
        index += 1
print(ans)
