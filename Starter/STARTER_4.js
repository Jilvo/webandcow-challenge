// Starter Challenge : Boucle for : https://tainix.fr/challenge/Boucle-for

function factorial(stop) {
  let sum = 0;
  for (i = 1; i < stop; i++) {
    sum += i;
  }
  return sum;
}
const stop = 60;
console.log(factorial(stop));
