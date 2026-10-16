class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set: # this character is a duplicate
                char_set.remove(s[l])
                l += 1 # move the left pointer till no more duplicates
            char_set.add(s[r]) # add the right character to the set
            # at this point no duplicates
            # is it the longest substring?
            res = max(res, r - l + 1)
        
        return res