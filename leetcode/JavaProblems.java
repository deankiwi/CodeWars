import java.util.ArrayList;

// 1190. Reverse Substrings Between Each Pair of Parentheses

class Solution {
    public String reverseParentheses(String s) {
        ArrayList<StringBuilder> words = new ArrayList<>();
        words.add(new StringBuilder());
        for (char letter : s.toCharArray()) {
            if (letter == '(') {
                words.add(new StringBuilder());
            } else if (letter == ')') {
                // reverse the string and add to second to last one
                StringBuilder sb = words.removeLast().reverse();
                words.getLast().append(sb);
            } else {
                words.getLast().append(letter);

            }
        }

        return words.get(0).toString();
    }
}

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascal = new ArrayList<>();
        List<Integer> firstRow = new ArrayList<>();
        firstRow.add(1);
        pascal.add(firstRow);
        for (int i = 1; i < numRows;i++){
            List<Integer> nextRow = new ArrayList<>();
            nextRow.add(1);
            List<Integer> lastRow = pascal.getLast();
            int n = lastRow.size();
            
            for (int j = 0; j < n - 1; j++){
                nextRow.add(lastRow.get(j)+lastRow.get(j+1));
            }

            nextRow.add(1);
            pascal.add(nextRow);

        }


        return pascal;
        
    }
}



/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public int minDepth(TreeNode root) {
        int count = 0;
        Deque<TreeNode> deque = new ArrayDeque<>();
        if (root != null){
           deque.push(root);
        }
        while (!deque.isEmpty()){
            count++;
            int width = deque.size();
            for (int i = 0 ; i < width ; i++){
                TreeNode curr = deque.removeFirst();
                if (curr.left != null){
                    deque.addLast(curr.left);
                }
                if (curr.right != null){
                    deque.addLast(curr.right);
                }
                if (curr.left == null && curr.right == null){
                    return count;
                }
            }
        }

        return count;        
        
    }
}