// Create a function that takes a number and returns an array of strings containing the number cut off at each digit.

// Examples
// 420 should return ["4", "42", "420"]
// 2017 should return ["2", "20", "201", "2017"]
// 2010 should return ["2", "20", "201", "2010"]
// 4020 should return ["4", "40", "402", "4020"]
// 80200 should return ["8", "80", "802", "8020", "80200"]

// PS: The input is guaranteed to be an integer in the range [0, 1000000]

function createArrayOfTiers(num) {
  // Create the array that is to be returned
  let arrayOfTiers = [];

  // Convert the number to a string
  let numString = num.toString();

  // Get the length of the string
  let stringLength = numString.length;

  // Set the string that will get added to each iteration
  let builtUpString = "";

  // Loop over the string and add to the array each time
  for (let i = 0; i < stringLength; i += 1) {
    // Add to the built up string
    builtUpString = builtUpString + numString[i];
    // add that string to the arrayOfTiers
    arrayOfTiers.push(builtUpString);
  }

  return arrayOfTiers;
}

// Favorite solution:

function createArrayOfTiers(num) {
  let prev = "";
  return [...(num + "")].map((value) => {
    return (prev += value);
  });
}

// I like how they used the spread operator and map to add new entry to the array each time. It's also readable.
