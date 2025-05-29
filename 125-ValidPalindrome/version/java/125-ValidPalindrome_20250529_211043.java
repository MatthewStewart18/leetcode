// Last updated: 29/05/2025, 21:10:43
class Solution {
    public boolean isPalindrome(String s) {
        String cleaned = s.toLowerCase().replaceAll("[^a-z0-9]", "").trim();
        int right = cleaned.length() - 1;

        for (int i = 0; i < cleaned.length(); i++){
            if (cleaned.charAt(i) == cleaned.charAt(right)) {
                right --;
            } else {
                return false;
            }
        }
        return true;
    }
}

            // while (i != right){
            //     if (cleaned.charAt(i) != cleaned.charAt(right)) {
            //         return false;
            //     } else {
            //         right--;
            //     }
            // }