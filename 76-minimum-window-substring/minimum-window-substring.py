class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # print(f"{ord('A') = }, {ord('a') = }, {ord('Z') = }, {ord('z') = }")
        map = [0] * 128
        count = len(t)
        start = 0
        end = 0
        min_len = math.inf
        start_index = 0
        # UPVOTE !
        for char in t:
            map[ord(char)] += 1

        while end < len(s):
            if map[ord(s[end])] > 0:
                count -= 1
            map[ord(s[end])] -= 1
            end += 1

            while count == 0:
                # print(f"{start = }, {end = }, {s[start:end] = }")
                if end - start < min_len:
                    start_index = start
                    min_len = end - start
                # print(f"{map[ord(s[start])] = }")
                if map[ord(s[start])] == 0:
                    count += 1
                map[ord(s[start])] += 1
                start += 1

        return "" if min_len == math.inf else s[start_index:start_index + min_len]