s = "MCMXCIV"
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
check = list()
res = 0
for item in range(len(s)):
    if not res or values[s[item]] == check[-1]:
        res += values[s[item]]
        check.append(values[s[item]])
    elif values[s[item]] < check[-1]:
        res += values[s[item]]
        check.append(values[s[item]])
    elif values[s[item]] > check[-1]:
        res = (res - check[-1]) + (values[s[item]] - check[-1])
        check.append(values[s[item]])

print(check)
print(res)
