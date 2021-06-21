import collections



def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()


A = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(A))
