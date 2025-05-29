// Last updated: 29/05/2025, 21:16:23
// while loop approach
class Solution {
    public boolean isPalindrome(String s) {
        String cleaned = s.toLowerCase().replaceAll("[^a-z0-9]", "").trim();
        int right = cleaned.length() - 1;
        int left = 0;

        while (left < right){
            if (cleaned.charAt(left) != cleaned.charAt(right)){
                return false;
            }
            left ++;
            right--;
        }
        return true;
    }
}