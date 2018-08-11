""" implementation of node"""
class Node:
  def __init__(self,key):
    self.left =None
    self.right=None
    self.val=key
"""
struct node 
{
  int data;
  struct node *left;
  struct node *right;
}
"""
##############################################
##############################################
""" implementation of tree"""
class Node:
  def __init__(self,key):
    self.left=None;
    self.right=None;
    self.val=key;

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)

"""
struct node 
{
    int data;
    struct node *left;
    struct node *right;
};
 
/* newNode() allocates a new node with the given data and NULL left and 
   right pointers. */
struct node* newNode(int data)
{
  // Allocate memory for new node 
  struct node* node = (struct node*)malloc(sizeof(struct node));
 
  // Assign data to this node
  node->data = data;
 
  // Initialize left and right children as NULL
  node->left = NULL;
  node->right = NULL;
  return(node);
}
 
 
int main()
{
  /*create root*/
  struct node *root = newNode(1);  
  /* following is the tree after above statement 
 
        1
      /   \
     NULL  NULL  
  */
   
 
  root->left        = newNode(2);
  root->right       = newNode(3);
  /* 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
    NULL NULL NULL NULL
  */
 
 
  root->left->left  = newNode(4);
  /* 4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    NULL  NULL  NULL
  /  \
NULL NULL
*/
 
  getchar();
  return 0;
}
"""

###############################
###############################

""" Tree Traversal"""
class Node:
  def ___init__(self,key):
    self.left=None
    self.right=None
    self.val=key

def printInorder(root):
   if root:
      printInorder(root.left)
      print(root.val)
      printInorder(root.right)

def printPostorder(root):
   if root:
      printPostorder(root.left)
      printPostorder(root.right)
      print(root.val)

def printPreorder(root):
   if root:
      print(root.val)
      printPreorder(root.left)
      printPreorder(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)
printPreorder(root)
printInorder(root)
printPostorder(root)

#########################################################
#########################################################

""" inorder traversal without recursion"""
"""
#include <bits/stdc++.h>
using namespace std;
 struct Node
{
int data;
struct Node* left;
struct Node* right;
Node(int data)
{
this->data=data;
left=right=NULL;
}
};

void inorder(struct Node *root)
{
stack<Node *>s;
Node *curr=root;

while(curr !=NULL || s.empty()==false)
{
while(curr != NULL)
{
s.push(curr);
curr=curr->left;
}

curr=s.top();
s.pop();

cout<< curr->data << " ";
curr=curr->right;
}
}

int main()
{
struct Node *root= new Node(1)
root->left=new Node(2);
root->right=new Node(3);
root->left->left=new Node(4);
root->left->right=new Node(5);

inorder(root);
return 0;
}

"""
###
"""
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
vector<int> Solution::inorderTraversal(TreeNode* A) {
    struct TreeNode *n1=A;
    vector<int>v;
    stack<struct TreeNode* >s;
    while(1)
    {
        while(n1)
        {
            s.push(n1);
            
            
            n1=n1->left;
        }
        if(s.empty())
        return v;
        n1=s.top();
        s.pop();
        v.push_back(n1->val);
        n1=n1->right;
    }
}
"""

####
""""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        current=A
        s=[]
        I=[]
        done=0
        while(not done):
            if current is not None:
                s.append(current)
                current=current.left
            else:
                if(len(s)>0):
                    current=s.pop()
                    I.append(current.val)
                    current=current.right
                else:
                    done=1
        return I
""""

#########################################
#########################################
"""Postorder traversal without recursion"""
###
"""
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
vector<int> Solution::postorderTraversal(TreeNode* A) {
    stack<struct TreeNode*>s1;
    //stack<struct TreeNode*>s2;
    

    //struct TreeNode* n1=A;
    struct TreeNode* nodee=A;

    vector<int>v;
    
    if(A==NULL)
    return v;
    s1.push(A);
    while(!s1.empty())
    {
      nodee=s1.top();
      s1.pop();
      v.push_back(nodee->val);
      if(nodee->left)
      s1.push(nodee->left);
      if(nodee->right)
      s1.push(nodee->right);
        
    }
    reverse(v.begin(),v.end());
    return v;
   
}
"""

###
""" c++ for postordr in book"""










    


   




