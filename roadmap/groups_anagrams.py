from typing import List
import collections


def groupAnagrams(strings: List[str]) -> List[List[str]]:
    out = list()
    templates = dict()
    for string in strings:
        template = ''.join(sorted(string))
        if template not in templates.keys():
            lst = list()
            lst.append(string)
            templates[template] = lst
        else:
            templates[template].append(string)
    for value in templates.values():
        out.append(value)
    return out


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strings=strs))

strs = [""]
print(groupAnagrams(strings=strs))

strs = ["a"]
print(groupAnagrams(strings=strs))


def groupAnagrams_2(strings: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for word in strings:      
        ans[tuple(sorted(word))].append(word)
    return ans.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams_2(strings=strs))
