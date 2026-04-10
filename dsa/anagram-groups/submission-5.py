from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = [] # array of tuples(str, sorted_str)
        for string in strs:
            temp = sorted(string)
            ordered_str = ''.join(temp)
            A.append((ordered_str, string))

        group = defaultdict(list)

        for ordered_str, string in A:
            group[ordered_str].append(string)
        return list(group.values())
