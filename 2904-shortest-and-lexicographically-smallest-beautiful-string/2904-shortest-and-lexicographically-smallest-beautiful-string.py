class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        ans = ""

        for i in range(n):
            ones = 0

            for j in range(i, n):
                if s[j] == '1':
                    ones += 1

                if ones > k:
                    break

                if ones == k:
                    current = s[i:j + 1]

                    if ans == "" or len(current) < len(ans):
                        ans = current
                    elif len(current) == len(ans) and current < ans:
                        ans = current

                    break

        return ans