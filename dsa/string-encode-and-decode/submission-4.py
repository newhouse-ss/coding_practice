class Solution:
    # my idea is using unique place-holder to join the strs at first, then decode them from place-holders, the problem is: how to choose place-holder which will not show in the input strs?
    # but the input contains 256 valid ASCII characters, not avaliable.
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for stg in strs:
            encoded += str(len(stg)) + '#' + stg

        return encoded

    def decode(self, s: str) -> List[str]:
        encoded = s
        n = len(encoded)
        res = []

        i = 0 # the means of i is to keep tracking on the 1st digit of count.
        while i < n:
            j = i
            while encoded[j] != '#':
                j += 1
            # now, encoded[j] == '#'
            length = int(encoded[i : j])
            res.append(encoded[j+1 : j+1+length])
            i = j+1+length
        return res