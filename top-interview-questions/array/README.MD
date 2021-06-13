# ARRAY

## Problem Solutions

### Problem 168: Majority Element
[Majority Element](https://leetcode.com/problems/majority-element)
Find the element that was occurred maximum time in the array

#### Approach 1

1) Hashmap 을 만들어 준다 --> python 의 경우 dictionary 사용
2) key 값을 원소로 value 값을 원소가 발견된 횟수로 지정하여 nums 의 for loop 을 돈다
3) for loop을 돌고 난뒤, 또 다른 for loop 을 만들어 max_val 즉, 가장 많이 발견된  key 와 value 값을 찾는다. 

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = {}
        max_val = 0 
        max_key = 0
        
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        for key,value in dic.items():
            
            if value > max_val:
                max_val = value
                max_key = key
                
        return max_key
```

Runtime: O(n)

Space Complexity: O(n)

#### Approach 2

1) Hashmap 을 만들어 준다 --> python 의 경우 dictionary 사용
2) key 값을 원소로 value 값을 원소가 발견된 횟수로 지정하여 nums 의 for loop 을 돈다
3) 같은 for loope 안에서 가장 많이 발견된 원소와 그 값을 찾는다

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = {}
        max_val = 0 
        max_key = 0
        
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
            
            key = num
            value = dic[num]
            if value > max_val:
                max_val = value
                max_key = key
        return max_key
```

Runtime: O(n)

Space Complexity: O(n)

#### Note:

첫번째의 경우 하나의 for loop 을 다시 만들어서 비효율적이였으나 
2번째의 경우는 같은 for loop 안에서 최빈값을 찾게 하여 실제로 400 ms - > 184 ms 로 줄일 수 있었다. 


### Problem 268: Majority Element
[Missing Number](https://leetcode.com/problems/missing-number/)

Find the missing number that is in range [0,n].
Follow up ** runtime O(n) with space complexit O(1) ** .

#### Approach 1

1) 먼저 missing number 찾기 쉽도록 sort 를 해준다
2) sort 된 list 를 for loop 으로 돌면서 다음값이 지금값 + 1 을 해준다.
3) 다음 값이 list 에 있는지 찾는다 그리고 0부터 시작 하기때문에 nums[0] = 0 인지도 확인 해준다.   
4) 다음값이 list 에 있다면 계속 for loop을 돈다, 없다면 그것이 missing number 이므로 리턴 해준다. 또는, 만약 num[0] != 0 이라면 0 이 list 에 없는것이므로 return 0 해준다.
5)edge case 로 만약 num = [1] 라면 리턴 0 을 해준다.

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort first
        nums.sort()
        
        for num in nums:
            next_num = num + 1
            
            if next_num in nums and nums[0] == 0:
                continue
            
            elif nums[0] != 0:
                return 0

            else:
                return num + 1
            
        if len(num) == 1 and num[0] == 1:
            return 0
```

Runtime: O(nlogn)

Space Complexity: O(n)


#### Approach 2

1) Hashset 에 nums 를 넣어준다(set 에 넣으면 자동 sort 된다)
2) for loop 길이를 set 의 길이보다 1 더해서 돈다. range(0,n) n 값은 포함이 안되므로..
3) 결국 for loop 돈다는건 set 의 크기 만큼 도는것이고 원소값이 nums list 에 없다면 그 값을 리턴 해주면 된다

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        set_num = set(nums)
        n = len(set_num)
        #set_num = {0,1,
        print(set_num)
        for num in range(0, n+1): 
            if num not in set_num:
                return num

```

Runtime: O(n)

Space Complexity: O(n)

첫번째의 경우 는 sort 를 하고 또 for loop 을 돌면서 missing number 을 찾아야해서 코드도 길어지고 런타임도 효율적이지 못했으나 두번째 경우에는 set 자체가 O(1) 밖에 안되고 그냥 set이 알아서 sort 도 해주기 때문에 set 길이 만큼 을 for loop 돌면서 없는값을 리턴 해주면 된다. 이경우가 코드도 간단하고 당연히 런타임도 효율적이다. 


                
        


