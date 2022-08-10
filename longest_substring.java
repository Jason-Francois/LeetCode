class Solution {
    // Runtime: O(n) - iterate through the whole list once
    // Memory: O(1)
    
    // Finds the length of the longest substring
    // with non-repeating characters
    public int lengthOfLongestSubstring(String s) {
        int i = 0;
        int j = 0;
        int maxLength = 0;
        HashSet<Character> chars = new HashSet();
        
        while (j < s.length()){
            char c = s.charAt(j);
            if(!chars.contains(c)){
                chars.add(c);
                // increment right pointer
                j++;

                // All set values are unique,
                maxLength = Math.max(chars.size(), maxLength);
            }else{
                // Remove the character left pointer is pointing to
                // Note: slides window one to the right
                chars.remove(s.charAt(i));
                // Increment left pointer
                i++;
            }
        }
        return maxLength;
    }
}