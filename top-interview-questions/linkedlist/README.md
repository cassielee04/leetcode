# Linked List

## Problem Solutions

### Problem 141: Linked List Cycle
[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
Return true if there is a cycle in the linked list. Otherwise, return false.

#### Approach 1 
##### Hash Set 

문제를 읽고 제일 먼저 생각난 방법

1) hash set 을 일단 정의해준다
2) linked list 돌때마다 hashset 에 node 를 넣어주고 node 는 다음 node 로 지정해준다
3) node 가 none 이 될때까지 돈다.
4) 만약 node 가 hashset 에 있다면 True 다 돌때 까지 없으면 False 로 리턴.

Runtime: O(N)
Space Complexity: O(N)

#### Approach 2
##### Fast Slow Pointers
조금 해맨 방법
예전부터 들어본 들어본 알고리즘이지만, 실제로 이해해보거나 써본적이 없음... 

문제:
[3,2,0,-4] 
pos = 1
즉 마지막 원소 "-4" 가 ->  "2" 를 포인트하므로 싸이클이 있다는 뜻.

1) slow 를 0 번째 노드 fast 를 1번째 노드
2) fast 와 fast.next 가 none 아닐때까지 돈다
3) slow == fast 면 return True
4) 아니면 slow = slow.next. fast = fast.next.next

Runtime: O(N)
Space Complexity: O(1)


**해맨이유:**
``` python 
slow = slow.next
fast = fast.next
```
라고 지정을 해둠.
당연히,, 무한루프를 돌수밖에없다.
slow 는 계속 fast 의 전을 가르칠거고 그렇담 둘의 값이 겹칠일이 없다. 
그러니 time limit exceeded error 가 나옴. 

### Problem 234: Palindrome Linked List
[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
Given the head of a singly linked list, return true if it is a palindrome.
#### Approach 1 

1) Create the empty array list
2) while head is not None, append value in to the array
3) array now has the all the linkedlist values
4) loop through to find if end and begin matches. 

Runtime: O(N)
Space Complexity: O(N)

**해맨이유:**
너무 복잡하게 생각함
앞에포인트와 뒤에 포인트를 어떻게 비교해아할지 몰랐음. 

**TODO:**
Recursive로 풀어보기

### Problem 206: Reverse Linked List
[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
Given the head of a singly linked list, reverse the list, and return the reversed list.

#### Approach 1 Iterative

포인트 방향들을 바꿔줌
1->2->3->4->5

5->4->3->2->1
1) prev 와 cur 노드를 지정해준다
2) while loop은 cur node 값이 None 이 아닐때까지 돈다
3) 현재의 다음노드를 템프에 저장
4) 현재 노드 다음값은 prev
5) prev 은 현재노드로 
6) 현재노드는 2) 의 템프값으로 지정해준다. 
7) prev 값으로 리턴한다.

**해맨이유:**
return 값이 왜 prev 인지 이해를 못했음
결국 밑에와 같은 라인때문에 return cur 할경우 None, Null 로 됨 그러므로 
return prev 해야 한다. 
```python
cur = nextTemp
```























