class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int maxVal = -1;
        
        for (int i=arr.size() - 1; i >= 0; i--) {
            int new_max = max(arr[i], maxVal);
            arr[i] = maxVal;
            maxVal = new_max;
        }

        return arr;
    }
};