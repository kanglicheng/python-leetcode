/*
lc problem 9
Determine whether an integer is a palindrome.
*/
public class Solution {
	public boolean isPalindrome(int x) {
		if (x<0) return false;
		int rev = 0, y = x;
		while (y!=0) {
			rev = rev*10 + y%10;
			y /= 10;
		}
		return (x==rev);
	}
}