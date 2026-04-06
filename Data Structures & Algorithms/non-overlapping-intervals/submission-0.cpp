class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [&](vector<int> a, vector<int> b) {
            return a[1] < b[1];
        });

        int n = intervals.size();
        vector<int> f(n, 0);
        f[0] = 1;
        for (int i = 1; i < n; i++) {
            int l = 0;
            int r = i - 1;
            int k = -1;
            while (l <= r) {
                int mid = (r - l) / 2 + l;
                if (intervals[mid][1] <= intervals[i][0]) {
                    k = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }

            f[i] = f[i - 1];
            if (k != -1) {
                f[i] = max(f[i], f[k] + 1);
            }
        }
        return n - f[n - 1];
    }
};