# Remove Duplicates From Sorted List

LeetCode link https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

## Example 1

```mermaid
graph LR
    subgraph After
        A'((1))
        B'((2))
        
        A' --> B'
    end

    subgraph Before
        A((1))
        B((1))
        C((2))
        
        A --> B
        B --> C
    end
```

Input:
```
head = [1,1,2]
```

Output:
```
[1,2]
```

## Example 2

```mermaid
graph LR
    subgraph After
        A'((1))
        B'((2))
        C'((3))
        
        A' --> B'
        B' --> C'
    end
    
    subgraph Before
        A((1))
        B((1))
        C((2))
        D((3))
        E((3))
        
        A --> B
        B --> C
        C --> D
        D --> E
    end
```

Input:
```
head = [1,1,2,3,3]
```
Output:
```
[1,2,3]
```
 
## Constraints

* The number of nodes in the list is in the range `[0, 300]`.
* -100 <= Node.val <= 100
* The list is guaranteed to be sorted in ascending order.
