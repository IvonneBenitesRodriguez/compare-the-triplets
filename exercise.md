**HackerRank Challenge compareTriplets** 
Alice and Bob each created one problem for HackerRank.
A reviewer rates the 2 challenges: 
awarding points on a scale from 1 to 100 for 3 categories :
- problem clarity
- problem originality
- problem difficulty

The rating for Alice's challenge is the triplet :<br/>
a = (a[0], a[1], a[2])<br/>

The task is to find their comparison points by comparing: <br/>
a[0] with b[0] <br/>
a[1] with b[1] <br/>
a[2] with b[2] <br/>

Condition: <br/>
if a[i] > b[i] then Alice is awarded 1 point <br/>
if a[i] < b[i] then Bob is awarded 1 point <br/>
if a[i] = b[i] then neither person receives a point <br/>

Comparison points is the total points a person earned. <br/>
Given a and b, determine their respective comparison points. <br/>

Example <br/>
a = [1,2,3]<br/>
b = [3,2,1]<br/>

For elements *0*, Bob is awarded a point because a[0]<br/>
For the equal elements a[1] and b[1], no points are earned <br/>
Finally, for elements 2, a[2] > b[2] so Alice receives a point <br/>

The return array is [1,1] with **Alice's score first** and **Bob's second.**

🌷 Function Description<br/>

Complete the function compareTriplets in the editor below<br/>
compareTriplets has the following parameter(s):<br/>
int a[3]: Alice's challenge rating<br/> 
int b[3]: Bob's challenge rating<br/>

Return<br/> 

int[2]: Alice's score in the first position,<br/>
and Bob's score is in the second.<br/>

Input Format:<br/>

The first line contains 3 space-separated integers,<br/>
a[0], a[1], and a[2], the respective values in triplet a.<br/>

The second line contains 3 space-separated integers,<br/>
b[0], b[1] and b[2], the respective values in triplet b.<br/>

**Constraints:**<br/>
1 <= a[i] <= 100<br/>
1 <= b[i] <= 100<br/>

Explanation:<br/> 
a = (a[0], a[1], a[2]) = (5, 6, 7)<br/>
b = (b[0], b[1], b[2]) = (3, 6, 10)<br/>

Comparing (individual score):<br/>
This is the condition:<br/>
a[0] > b[0] => Alice receives 1 point.<br/>
a[1] = b[1] => Nobody receives points.<br/>
a[2] < b[2] => Bob receives 1 point.<br/>

**Alice's comparison score is 1, and Bob's comparison score is 1**
**Thus, we return the array [1,1]**

Explanation 1:<br/>

a) comparing 17 < 99 => Bob receives a point<br/>
usually when < is there Bob receives points because<br/> 
that is specified in the challenge.<br/>

b) Now comparing these values:<br/> 
28 < 16 => Alice receives 1 point<br/>
30 > 8 => Alice receives 1 point<br/>
In total Alice has 2 points.<br/>

c) Always Alice is the first value and Bob the second value<br/>
The return array is [2,1]<br/>
the value 2 are the points that Alice won.<br/>
the value 1 is the point that Bob won.<br/>  

Task:<br/>
Complete the compareTriplets function<br/> 
the function is expected to return an integer Array A<br/>
the function is expected to return an integer Array B<br/>

