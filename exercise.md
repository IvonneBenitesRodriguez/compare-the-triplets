Alice and Bob each created one problem for HackerRank.
A reviewer rates the 2 challenges: 
awarding points on a scale from 1 to 100 for 3 categories :
- problem clarity
- problem originality
- problem difficulty

The rating for Alice's challenge is the triplet :
a = (a[0], a[1], a[2])

The task is to find their comparison points by comparing
a[0] with b[0] 
a[1] with b[1]
a[2] with b[2]

if a[i] > b[i] then Alice is awarded 1 point
if a[i] < b[i] then Bob is awarded 1 point
if a[i] = b[i] then neither person receives a point 

Comparison points is the total points a person earned.
Given a and b, determine their respective comparison points.

Example
a = [1,2,3]
b = [3,2,1]

For elements *0*, Bob is awarded a point because a[0]
For the equal elements a[1] and b[1], no points are earned
Finally, for elements 2, a[2] > b[2] so Alice receives a point

The return array is [1,1] with Alice's secore first and Bob's second.

Function Description

Complete the function compareTriplets in the editor below
compareTriplets has the following parameter(s):
int a[3]: Alice's challenge rating 
int b[3]: Bob's challenge rating

Return 

int[2]: Alice's score in the first position,
and Bob's score is in the second.

Input Format:

The first line contains 3 space-separated integers,
a[0], a[1], and a[2], the respective values in triplet a.

The second line contains 3 space-separated integers,
b[0], b[1] and b[2], the respective values in triplet b.

Constraints:
1 <= a[i] <= 100
1 <= b[i] <= 100

Explanation: 
a = (a[0], a[1], a[2]) = (5, 6, 7)
b = (b[0], b[1], b[2]) = (3, 6, 10)

Comparing (individual score):This is the conditional
a[0] > b[0] => Alice receives 1 point.
a[1] = b[1] => Nobody receives points.
a[2] < b[2] => Bob receives 1 point.

Alice's comparison score is 1, and Bob's comparison score is 1
Thus, we return the array [1,1]

Explanation 1:

a) comparing 17 < 99 => Bob receives a point
usually when < is there Bob receives points because 
that is specified in the challenge.

b) Now comparing these values: 
28 < 16 => Alice receives 1 point
30 > 8 => Alice receives 1 point
In total Alice has 2 points.

c) Always Alice is the first value and Bob the second value
The return array is [2,1]
the value 2 are the points that Alice won.
the value 1 is the point that Bob won.  

Task:
Complete the compareTriplets function 
the function is expected to return an integer Array A
the function is expected to return an integer Array B

