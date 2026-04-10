class Solution:
    """
    The main idea is: 
    encoding: First calculate length of all strs, then use a '#' to seperate, 
    then join all strs together.
    decoding: First split lengths, then use these lengths to slice strs.
    """
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s))
            res += ','
        res += '#'

        for s in strs:
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        cnt, res, i = [], [], 0
        while s[i] != '#':
            curr = ''
            while s[i] != ',':
                curr += s[i]
                i += 1
            i += 1 # i on the first position of next length
            cnt.append(int(curr))
        i += 1 # i is the first element of the string.

        for length in cnt:
            res.append(s[i:i+length])
            i += length
        
        return res
