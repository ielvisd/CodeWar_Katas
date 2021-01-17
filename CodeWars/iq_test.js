// Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

// ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

// ##Examples :

// iqTest("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

// iqTest("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

function iqTest(numbers) {
  let numberArray = numbers.split(" ");
  let numberOfOdd = 0;
  let numberOfEven = 0;

  // Loop through the numbers
  for (let i = 0; i < numberArray.length; i++) {
    // If it's an even number, add it to numberOfEven
    if (numberArray[i] % 2 === 0) {
      numberOfEven += 1;
    }
    // If it's an odd number, add it to numberOfDdd
    if (numberArray[i] % 2 !== 0) {
      numberOfOdd += 1;
    }
  }

  let type = null;
  if (numberOfEven > numberOfOdd) {
    type = "even";
  } else {
    type = "odd";
  }

  //Loop through list looking for first number that's not the current type
  for (let i = 0; i < numberArray.length; i++) {
    if (numberArray[i] % 2 === 0 && type === "odd") {
      return i + 1;
    }
    if (numberArray[i] % 2 !== 0 && type === "even") {
      return i + 1;
    }
  }
}

console.log(iqTest("2 4 7 8 10")); // 3 // Third number is odd, while the rest of the numbers are even

console.log(iqTest("1 2 1 1")); // 2 // Second number is even, while the rest of the numbers are odd

console.log(iqTest("1 2 2")); // 1

// My favorite solution: 

function iqTest(numbers) {
  numbers = numbers.split(" ");

  var evens = [];
  var odds = [];

  for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] & 1) {
      odds.push(i + 1);
    } else {
      evens.push(i + 1);
    }
  }

  return evens.length === 1 ? evens[0] : odds[0];
}

// I like this one because it's similar to mine but a lot shorter and more readable. 