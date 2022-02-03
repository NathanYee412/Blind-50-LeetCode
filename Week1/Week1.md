# Week 1 of Blind 50 Leetcode challenge
I will document my progress and explain solutions here and in code. 


### Two Sum (1/26/2022)
My implementation of Two Sum starts with creating an empty dict in Python.

The dict will consist of a value of the array as the key and the index as the value. This will is used this way so when the target difference is found in the dict, we can use the ```dict[difference]``` and return the index.

We will start with a forloop that is enumerated so we can get the index and the value in one go. 

We then calcuate the difference as target - current value. 

We will check if this difference exists inside of the dict. If it does not exist in the dict, we will add the current value and idex to the dict.

### Contains Duplicate (1/26/2022)
Start with an empty dict
Key: array value, Value: index

Loop through array and check if the value is already in the dictionary.
if the value exists in there already, return True
Outside of the for loop, return False. If the loop finishes without seeing a duplicate the first thing to do is to return False

### Best time to buy and sell stock (1/27/2022)
Two pointer 
l = 0, r = 1

maxProfit = 0

while the r pointer is less than the length of the input array,
    check if the value at the left pointer is less than the value of the right pointer
        calculate the profit
        Compare max profit to current profit 

    if the value of the left pointer is greater than the value of the right pointer
        set the position of the left pointer to the right
    

    iter ate the right pointer

return the max profit 

### Valid Anagram (1/27/2022)

Was only able to solve with a time complexity O(n^2)

used one loop to check one letter
    then another loop to check all letters until it matched
    when matched remove that letter and break from the loop


### Product Except Self

Used a left and right pointer that starts at the beginning and end. 

Calculate the value of the prefix and iterate one forward
Calculate the value of the postfix and iterate one backward

start the lvalue = 1 and rvalue = 1
then do *= to calculate the rolling total 

When the array is done iterating then do a forloop for the length of the prefix and multiply the two together 

Runtime: O(n^2) at the moment because two forloops are used

Will look at other solutions to improve runtime 




    


