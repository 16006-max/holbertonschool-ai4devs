function calculateAverage(numbers) {
  if (numbers.length === 0) {
    return 0;
  }
  let total = 0;
  for (let i = 0; i < numbers.length; i++) {
    total += Number(numbers[i]);
  }
  return total / numbers.length;
}

const scores = ["10", "20", "30"];
console.log(calculateAverage(scores)); // expected: 20
console.log(calculateAverage([]));     // expected: 0
