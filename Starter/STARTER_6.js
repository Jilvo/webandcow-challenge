// Starter Challenge : Utilisation d’une fonction : https://tainix.fr/challenge/Utilisation-d-une-fonction

function find_modulo_3(values) {
  let resultat = [];

  for (const value of values) {
    if (value % 3 == 0) {
      resultat.push(value);
    }
  }
  console.log(resultat.join("-"));
}

const values = [
  42, 92, 50, 73, 36, 28, 74, 34, 90, 58, 77, 10, 51, 98, 34, 56, 35, 25, 31,
  24, 96, 19, 44, 18, 78, 82,
];
find_modulo_3(values);
