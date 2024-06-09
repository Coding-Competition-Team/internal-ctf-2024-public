**Seeing Stars (Stars)**

---

Ryan Chen Yi Xuan wants to see the stars. However, due to Singapore's light pollution, he can barely see any. Fortunately for him, he managed to get his hands on some telescopes, but needs your help to decide which to use.  
Ryan has _n_ telescopes, arranged in increasing order of power from _0_ to _n - 1_ (no 2 telescopes will have the same power). Each telescope incurs a cost due to electricity consumption. Given a star that requires _p_ power to see, Ryan wants to be able to view it incurring the least cost possible due to his stingy nature. Ryan can use any telescope that has _>= p_ power to see the star. Note: Telescopes can be reused.  

## **Input**

Input contains 100 testcases. Each testcase starts with 2 integers, _1 <= n <= 1000000_, which is the number of telescopes ryan owns, and _0 < s <= 50000_, which is the number of stars he wants to see.  
The next line will be a list of the costs of using each telescope. There will be _n_ space seperated integers, with the _ith_ integer having a power of _i_ (starting from 0). The cost of using each telescope will be _> 0_ and _<= 1000000_.<br>
The next _s_ lines of input will contain an integer _p_, _0 <= p < n_, indicating the power of telescope required to see the star.

## **Output**

Output 1 integer, the minimum cost of seeing all the stars.

## **Constraints**

Time limit (per input): 1 second

## **Sample testcase**

6 3<br>
6 5 4 7 1 6<br>
4<br>
5<br>
2

## **Sample output**

8

## **Sample explanation**

For the first star, Ryan can use the fifth telescope (power 4) for a cost of 1.<br>
For the second star, Ryan can use the sixth telescope (power 5) for a cost of 6.<br>
For the third star, Ryan can use the fifth telescope (power 4) for a cost of 1.<br>
Total minimum cost is 1 + 6 + 1 = 8.