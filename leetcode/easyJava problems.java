

public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode deleteDuplicates(ListNode head) {

        if (head == null){
            return head;
        }
        int val = head.val;
        ListNode prev = head;
        ListNode curr = head;
        while (curr != null){
            if (prev.val != curr.val){
                prev.next = curr;
                prev = curr;
            }
            curr = curr.next;
        }
        prev.next = null;

        return head;
        
    }
}


class Solution {
    public int climbStairs(int n) {
        
        int lastlast = 1;
        int last = 1;
        int curr = 1;

        for (int i = 2; i <= n; i++){
            curr = last + lastlast;
            lastlast = last;
            last = curr;
        }

        return curr;

        
    }
}

class Solution {
    public int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length-1;
        int mid = (int)((high + low) / 2);
        
        
        while (low <= high){
            if (nums[mid] == target){
                return mid;
            } else if (nums[mid] < target){
                low = mid + 1;
            } else {
                high = mid - 1;
            }
            mid = (high + low) / 2;

        }
        return low;
        
    }
}

class Solution {
    public int minOperations(String[] logs) {
        int folder = 0;

        for (int i = 0; i < logs.length; i++){
            String sym = logs[i];
            if (sym.equals("../") ){
                if (folder != 0){

                folder--;
                }
            } else if (!sym.equals("./")) {
                folder++;
            }
        }


        return folder;
    }
}