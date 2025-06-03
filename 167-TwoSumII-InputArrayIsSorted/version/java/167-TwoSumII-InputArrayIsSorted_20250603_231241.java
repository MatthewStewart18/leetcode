// Last updated: 03/06/2025, 23:12:41
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while(left != right){
            int currentsum = numbers[left] + numbers[right];
            if (currentsum > target){
                right--;
            } else if (currentsum < target){
                left ++;
            } else {
                return new int[] {left + 1, right + 1};
            }
        }
        return new int[] {left + 1, right + 1}; 
    }
}