---
title: "RandomNotes(1)"
date: 2022-06-14T15:21:30-04:00
categories:
  - blog
tags:
  - Python
  - C++
  - OOP
---
Overall, hashtable is really useful. In reducing the time complexity, there will be a trade off between time and memory.

A very classic problem: adding two numbers.
```ruby
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int length = nums.size();
        vector<int> FinalAnswer;
        for(int i=0;i<length;i++){
            for(int j=i+1; j<length;j++){
                if (nums[j]+nums[i]==target) {
                    FinalAnswer.push_back(i);
                    FinalAnswer.push_back(j);
                }
            }
        }
        return FinalAnswer;
    }
};
```
Compare with the other methods:
```ruby
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = hashtable.find(target - nums[i]);
            if (it != hashtable.end()) {
                return {it->second, i};
            }
            hashtable[nums[i]] = i;
        }
        return {};
    }
};
\
```

The method below can reduce it from O(N^2) to O(N). Very convenient.
It may be said that the method of harsh is not completely clear.
HashTalbe: If key=k, its value is stored in the storage location of (k). Thus, the checked records can be obtained directly without comparison. This correspondence f is called a hash function, and the table established according to this idea is a hash table. "wtf this is the content of 2012, it is completely forgotten..." The disadvantage of not brushing the question. . . Even this very, very basic question has to be sent and received with violence. . .