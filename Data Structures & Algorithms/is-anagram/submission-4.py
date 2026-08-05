class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_one = {}
        map_two = {}

        for c in s:
            if c not in map_one:
                map_one[c] = 1
            else:
                map_one[c] = map_one.get(c) + 1
        
        for c in t:
            if c not in map_two:
                map_two[c] = 1
            else:
                map_two[c] = map_two.get(c) + 1

        return map_one == map_two