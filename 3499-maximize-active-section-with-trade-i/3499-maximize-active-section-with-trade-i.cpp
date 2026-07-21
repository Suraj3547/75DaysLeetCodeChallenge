class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {

        int ones = 0;
        vector<int> zeroBlocks;

        for (char c : s)
            if (c == '1') ones++;

        // Lengths of every zero block
        for (int i = 0; i < s.size(); ) {
            if (s[i] == '1') {
                i++;
                continue;
            }

            int j = i;
            while (j < s.size() && s[j] == '0') j++;

            zeroBlocks.push_back(j - i);
            i = j;
        }

        // Less than 2 zero blocks => no valid trade
        if (zeroBlocks.size() <= 1)
            return ones;

        int best = 0;
        for (int i = 0; i + 1 < zeroBlocks.size(); i++) {
            best = max(best, zeroBlocks[i] + zeroBlocks[i + 1]);
        }

        return ones + best;
    }
};