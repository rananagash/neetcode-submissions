class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dictionaries 
        # go through s and go through t and put them in dictionaries
        # dicts = {'r': 2}
        
        # goal: return if s and t contain the same character
        # count how many of each character s has vs t and compare

        s_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                # add letter into dict with value 1
                s_dict[letter] = 1
        
        t_dict = {}
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                # add letter into dict with value 1
                t_dict[letter] = 1

        return s_dict == t_dict





