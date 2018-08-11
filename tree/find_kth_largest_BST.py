"""leetcode problem 230 - kth smallest element in bbinary search tree..  https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/"""

##inorder traversal is solution approach 1

"""
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        struct TreeNode *n1=root;
        int a=0;
        while(1)
        {
            
            while(n1)
            {
                s.push(n1);
                n1=n1->left;
                
            }
            if(s.empty())
                break;
            n1=s.top();
            s.pop();
            a++;
            if(a==k)
            {
                return n1->val;
            }
            
            n1=n1->right;
            
        }
        
        
        
        
        
    }
    
};
"""

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        current=root
        s=[]
        done=0
        a=0
        while(not done):
            if current is not None:
                s.append(current)
                current=current.left
            else:
                if(len(s)>0):
                    current=s.pop()
                    a =a+1
                    if a is k:
                        return current.val
                    current=current.right
                else:
                    done=1
        
        
        

"""




