class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. DP: not the optimal, since the dp(current_state) depends on all previous states, O(N^2)
        # 2. Sliding Window. The idea comes from maintaining the substring within the window has no repeat char, while update the length of window.
        # The problems are: 1. A hash table to record the visited char (key: char, value: index of the most recent key), every time meet a new char, check whether it's in the hash table, if not, expand the length of window, if it's existing, first move left boundry to left of previous hash[char], then update the index of new char.
        if len(s) == 0 or len(s) == 1:
            return len(s)

        n = len(s)
        char_idx = {s[0] : 0} # the first ele is on 1st position.
        res = 1
        left, right = 0, 1
        while right < n and left <= right: #pitfall: the last is not unique will stuck into infinite loop.
            if s[right] not in char_idx:
                char_idx[s[right]] = right # pitfall: everytime meet a new char, record it.
                res = max(res, right - left + 1)
                right += 1
            else:
                repeat = s[right] # now we have 2 char == repeat, one on right, one on char_idx[repeat].
                left = max(left, char_idx[repeat] + 1) # the next position of the first repeat. To make sure the substring is no repeat. left can not jump back.
                char_idx[repeat] = right # update the new idx of repeat.
                res = max(res, right - left + 1)
                right += 1 # also need to update right.
        
        return res