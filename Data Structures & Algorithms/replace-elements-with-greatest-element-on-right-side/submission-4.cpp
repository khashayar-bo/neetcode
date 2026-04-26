class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        if (n == 0) return arr;
        int maxVal = arr[n - 1];
        arr[n - 1] = -1;
        for (int i = n - 2; i >= 0; --i) {
            int curr = arr[i];
            arr[i] = maxVal;
            if (curr > maxVal) maxVal = curr;
        }
        return arr;
    }
};