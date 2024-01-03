/* using reduce method */
/*The reduce method is used instead the for loop which means
It is used to iterate */

function compareTriplets(a,b) {
    const [aliceScore, bobScore] = a.reduce(([alice, bob], currentA, i) => {
        const currentB = b[i];
        if (currentA > currentB) {
            return [alice + 1, bob];
        } else if (currentA < currentB) {
            return [alice, bob + 1];
        } else {
            return [alice, bob];
        }
    }, [0,0]);
    return [aliceScore, bobScore];
}

const a  = readline().split('').map(Number);
const b = readline().split('').map(Number);

const result = compareTriplets(a,b);
console.log(result.join(''));