// Given two integers a and b, which can be positive or negative, find the sum of all the integers between including them too and return it. If the two numbers are equal return a or b.

// Note: a and b are not ordered!

// Examples
// GetSum(1, 0) == 1   // 1 + 0 = 1
// GetSum(1, 2) == 3   // 1 + 2 = 3
// GetSum(0, 1) == 1   // 0 + 1 = 1
// GetSum(1, 1) == 1   // 1 Since both are same
// GetSum(-1, 0) == -1 // -1 + 0 = -1
// GetSum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

function getSum(a, b) {
  // If the number are equal, return either number
  if (a === b) {
    return a;
  }
  let sum = 0;
  // Check which number is bigger 
  if (a > b) {
    let range = a - b;
    // loop through the numbers and add to the sum
    for (let i = 0; i <= range; i++) {
      sum += b + i;
    }
  } else {
    let range = b - a;
    // loop through the numbers and add to the sum
    for (let i = 0; i <= range; i++) {
      sum += a + i;
    }
  }
  return sum;
}

 // My favorite solution: 

 const GetSum = (a, b) => {
   let min = Math.min(a, b),
     max = Math.max(a, b);
   return ((max - min + 1) * (min + max)) / 2;
 };

 // I like this because it uses Math functions and also just uses a math formula to get the answer. Clever. 