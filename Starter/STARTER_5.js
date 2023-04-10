function sum_array_sup_5(values) {
  let sum = 0;
  values.forEach((element) => {
    if (element >= 5) {
      sum += element;
    }
  });
  return sum;
}

const values = [
  2, 5, 8, 7, 7, 1, 7, 6, 9, 1, 6, 8, 10, 6, 2, 6, 4, 10, 7, 4, 6, 7, 10, 4, 2,
];
console.log(sum_array_sup_5(values));
