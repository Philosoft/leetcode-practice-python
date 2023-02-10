# Symmetric Tree

LeetCode link: https://leetcode.com/problems/symmetric-tree/description/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Example 1

```mermaid
graph TD
    root((1))
    
    root.left((2))
    root.right((2))
    
    lvl_3__n3l((3))
    lvl_3__n4l((4))
    lvl_3__n4r((4))
    lvl_3__n3r((3))
    
    root --> root.left
    root --> root.right
    
    root.left --> lvl_3__n3l
    root.left --> lvl_3__n4l
    
    root.right --> lvl_3__n4r
    root.right --> lvl_3__n3r
```

Input:
```
root = [1,2,2,3,4,4,3]
```

Output:
```
true
```

## Example 2

Input:
```
root = [1,2,2,null,3,null,3]
```
Output:
```
false
```
 
## Constraints

* The number of nodes in the tree is in the range `[1, 1000]`.
* `-100 <= Node.val <= 100`
 
## Follow up

Could you solve it both recursively and iteratively?
