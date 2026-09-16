class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t or len(s) < len(t): return ""

        need = Counter(t)
        required = len(need)

        window = {}
        have = 0

        res = [-1, -1]
        res_len = float('inf')
        left = 0

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]: 
                have += 1

            while have == required:
                current_len = right - left + 1

                if current_len < res_len:
                    res_len = current_len
                    res = [left, right]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1 

        return s[res[0]:res[1]+1] if res[0] != -1 else ""

if __name__ == "__main__":
    sol = Solution()

    s = "OUZODYXAZV"
    t = "XYZ"

    print(sol.minWindow(s,t))











        