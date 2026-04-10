class Solution:


    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + '#' + string

        return result


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            cur_length = int(s[i:j])
            i = j + 1 # 1st index of the string need to be translated.
            j = i + cur_length # index after the index of last char in cur_string
            cur_string = s[i:j]
            res.append(cur_string)
            i = j

        return res
            
