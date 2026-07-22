class Solution {
public:
    int myAtoi(string s) {

        int i = 0;
        int n = s.length();

        // Step 1: Skip leading spaces
        while (i < n && s[i] == ' ')
            i++;

        // Step 2: Check sign
        int sign = 1;
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            if (s[i] == '-')
                sign = -1;
            i++;
        }

        // Step 3: Convert digits
        long long ans = 0;

        while (i < n && isdigit(s[i])) {

            ans = ans * 10 + (s[i] - '0');

            // Step 4: Overflow check
            if (sign == 1 && ans > INT_MAX)
                return INT_MAX;

            if (sign == -1 && -ans < INT_MIN)
                return INT_MIN;

            i++;
        }

        return sign * ans;
    }
};