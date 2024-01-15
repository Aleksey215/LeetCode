def isAnagram(s: str, t: str) -> bool:
    try:
        l = list(t)
        for item in s:
            l.remove(item)
        if not l:
            return True
        else:
            return False
    except ValueError:
        return False
