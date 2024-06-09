**Haowei's Journey (Journey)**

---

The trek from Woodlands to ACS(I) is a long and painful one, and is the cruel fate Haowei has to suffer everyday. In order to make his life easier, Haowei wants to write a script to find the fastest route to complete his journey.  

Being a pro geogger, Haowei has created a map, containing all locations he passes through in his journey, inclusive of the start and endpoints. His map also has all the distances from each location to its surrounding locations.   

Haowei is a pro grammer, but as of recent he has been too busy winning ctfs to code the script, and needs your help to do it!  
Write a script to find the minimum distance travelled from to Woodlands to ACS(I), given Haowei's map.

## **Input**

Input contains 100 testcases. Each testcase starts with 2 integers, _2 <= n <= 10000_, which is the number of locations on the map, and _0 < e <= 10000_, which is the number of edges (bidirectional path between 2 locations).  
The locations are labelled from _0_ to _n - 1_, with Woodlands being location _0_ and ACS(I) being location _n - 1_.<br>
The next _e_ lines of input will contain 3 integers, _0 <= u, v < n_, which are the 2 locations where an edge exists, and _0 < d <= 1000000_, which is the distance between these 2 locations.<br>
Note: There might not be a possible route from Woodlands to ACS(I)

## **Output**

Output 1 integer, the minimum distance of Haowei's Journey.<br>  
If there is no possible route, output `-1`.

## **Constraints**

Time limit (per input): 1 second

## **Sample testcase**

5 5<br>
0 1 1<br>
0 2 5<br>
1 2 2<br>
2 3 1<br>
3 4 3

## **Sample output**

7

## **Sample explanation**

Haowei has two routes:
- 0 to 1, 1 to 2, 2 to 3, 3 to 4
- 0 to 2, 2 to 3, 3 to 4
The first route has a distance of 7.  
The second route has a distance of 9.  
Therefore the minimised distance is 7.