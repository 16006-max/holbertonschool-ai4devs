function classifyNumber(n) {
  if (n % 2 === 0) {
    return "even";
  else {
    return "odd";
  }
}

console.log(classifyNumber(4)); // expected: even
console.log(classifyNumber(7)); // expected: odd
