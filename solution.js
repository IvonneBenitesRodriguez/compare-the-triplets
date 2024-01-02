/* For this solution:
I create 2 variables and initialize these variables with 0
because I want to add the values iterated there, 
of course these values are having the conditions specified here:

Conditions:
a[0] > b[0] => Alice receives 1 point
a[1] = b[1] => nobody receives points
a[2] < b[2] => Bob receives 1 point

Then, once we have alice's score and bob'score 
we return this array:
[alice'sscore, bob's score]
*/

function compareTriplets(a,b) {
    let aliceScore = 0;
    let bobScore = 0;

    for (let i = 0; i < 3; i++){ /*we are using i < 3 because it is a triplet we are dealing with */
        if(a[i] > b[i]) {
            aliceScore++;
        } else if(a[i] < b[i]) {
            bobScore++;
        }
    }
    return [aliceScore, bobScore];
}

/* This const a and const b functions 
are used once the user is adding his/her input:
const a  = readline().split('').map(Number);
const be = readline().split('').map(Number);

const result = compareTriplets(a,b);
console.log(result.join(''));
*/
/* Note:
If you have a different number of elements in your arrays
(e.g., if you were dealing with quadruplets,
you might use i < 4), 
you would adjust the loop condition 
accordingly to ensure that the loop iterates 
over all elements in the arrays.
*/
