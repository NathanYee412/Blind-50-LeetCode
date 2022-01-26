# Week 1 of Blind 50 Leetcode challenge
I will document my progress and explain solutions here and in code. 

## Day 1 (1/26/2022)
Starting with TwoSum. LeetCode's most popular question to solve. 

### Two Sum
My implementation of Two Sum starts with creating an empty dict in Python.

The dict will consist of a value of the array as the key and the index as the value. This will is used this way so when the target difference is found in the dict, we can use the ```dict[difference]``` and return the index.

We will start with a forloop that is enumerated so we can get the index and the value in one go. 

We then calcuate the difference as target - current value. 

We will check if this difference exists inside of the dict. If it does not exist in the dict, we will add the current value and idex to the dict.