class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = dict()
        if not s:
            return 0
        left, right, all_max = 0, 0, 0
        while right < len(s):
            map[s[right]] = map.get(s[right], 0) + 1
            all_max = max(all_max, map[s[right]])
            if right - left + 1 > all_max + k:
                map[s[left]] -= 1
                left += 1
            right += 1
        
        return len(s) - left