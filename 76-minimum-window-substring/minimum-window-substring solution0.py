class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = {}  # Frequency of characters in string t
        for char in t:
            target_freq[char] = target_freq.get(char, 0) + 1

        window_freq = {}  # Frequency of characters in the current window
        count = 0  # Number of characters from t currently in the window
        min_len = float('inf')  # Initialize with positive infinity
        min_window = ""

        left, right = 0, 0
        while right < len(s):
            # Expand the window
            if s[right] in target_freq:
                window_freq[s[right]] = window_freq.get(s[right], 0) + 1
                if window_freq[s[right]] <= target_freq[s[right]]:
                    count += 1

            # Contract the window
            while count == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                if s[left] in target_freq:
                    window_freq[s[left]] -= 1
                    if window_freq[s[left]] < target_freq[s[left]]:
                        count -= 1
                left += 1

            right += 1

        return min_window