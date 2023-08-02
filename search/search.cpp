#include<bits/stdc++.h>
#include<stdio.h>
#include<map>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };
vector<vector<int>> res;
vector<int> ans;
void path(TreeNode* root){
    if (root->left == nullptr && root->right == nullptr){
        ans.push_back(root->val);
        res.push_back(ans);
        ans.pop_back();
        return;
    }
    ans.push_back(root->val);
    if (root->left){
        path(root->left);
    }
    if (root->right){
        path(root->right);
    }
    ans.pop_back();
}
void dfs(TreeNode* root){
    cout<<root->val<<" ";
    if (root -> right){
        dfs(root -> right);
    }
    if (root -> left){
        dfs(root -> left);
    }
}
queue<TreeNode* > q;
void bfs(TreeNode* root){
    q.push(root);
    while (!q.empty()){
        TreeNode* point = q.front();
        q.pop();
        cout<< point->val << " ";
        if (point -> left){
            q.push(point->left);
        }
        if (point -> right){
            q.push(point->right);
        }
    }
}
int main(){
    TreeNode a(0);
    TreeNode b(2);
    TreeNode c(1);
    TreeNode d(3);
    TreeNode e(9);
    TreeNode f(5);
    a.left = &b;
    a.right = &c;
    b.left = &d;
    c.left = &e;
    c.right = &f;
    path(&a);
    for (auto &i : res){
        for (auto &j : i){
            cout<<j<< " ";
        }
        cout <<endl;
    }
    dfs(&a);
    cout<<endl;
    bfs(&a);
    return 0;
}
