# Invert Binary Tree

LeetCode link https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

## Example 1

```mermaid
graph TD
    subgraph Before
        A((4))
        
        B((2))
        C((7))
        
        D((1))
        E((3))
        F((6))
        H((9))
        
        A --> B
        A --> C
        
        B --> D
        B --> E
        
        C --> F
        C --> H
    end

    subgraph After
        A'((4))
        
        C'((2))
        B'((7))
        
        E'((1))
        D'((3))
        H'((6))
        F'((9))
        
        A' --> C'
        A' --> B'
        
        B' --> E'
        B' --> D'
        
        C' --> H'
        C' --> F'
    end
```

Input: root = `[4,2,7,1,3,6,9]`

Output: `[4,7,2,9,6,3,1]`

## Example 2

Input: root = `[2,1,3]`

Output: `[2,3,1]`

## Example 3

Input: root = `[]`

Output: `[]`

## Constraints

* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100
