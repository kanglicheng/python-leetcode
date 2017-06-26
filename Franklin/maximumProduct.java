/*
lc contest 38, problem 1
Given an array of integers, return the maximum product of three elements in the array.
Spec: Array length >=3, element in the range [-1000, 1000].
*/
public class Solution {
    public int maximumProduct(int[] nums) {
        int product = Integer.MIN_VALUE;
        List<Integer> pos = new ArrayList();
        List<Integer> neg = new ArrayList();
        for (int i=0; i<nums.length; i++) {
            if (nums[i]>0) {pos.add(nums[i]);}
            else {neg.add(nums[i]);}
            
        }
        Collections.sort(pos);
        Collections.sort(neg, Collections.reverseOrder());
        
        // two cases
        int result = Integer.MIN_VALUE;
        
        if (pos.size()==0) {
            result = neg.get(neg.size()-1)*neg.get(neg.size()-2)*neg.get(neg.size()-3);
        } else if (pos.size()==1) {
            result = pos.get(pos.size()-1) * neg.get(neg.size()-1)*neg.get(neg.size()-2);
        } else if (pos.size()==2) {
            if (neg.size()>=2)
                result = pos.get(pos.size()-1) * neg.get(neg.size()-1) * neg.get(neg.size()-2);
            else if (neg.size()==1)
                result = nums[0]*nums[1]*nums[2];
        } else if (pos.size()>=3) {
            if (neg.size()<=1) {
                result = pos.get(pos.size()-1)*pos.get(pos.size()-2)*pos.get(pos.size()-3);
            } else if (neg.size()>=2) {
                int neg_prod = neg.get(neg.size()-1)*neg.get(neg.size()-2);
                int pos_prod = pos.get(pos.size()-2)*pos.get(pos.size()-3);
                result = pos.get(pos.size()-1)*Integer.max(pos_prod,neg_prod);
            }
        }
        return result;
    }
}
