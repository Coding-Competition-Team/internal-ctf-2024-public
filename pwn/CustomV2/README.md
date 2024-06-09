# Custom

Author: Chen Haowei

**Difficulty: Hard**

## Description

I decided to use urandom now for true randomness, now no one can bypass my canary!

Note/Hint: Minor amounts of brute-forcing is required for this challenge!

## Solution

Keep running the program until the canary starts with a null byte. As such, the strcmp will always return true as long as one enters in null for the canary.