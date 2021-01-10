// A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

// Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

function isPangram(string) {
  var alphabet = "abcdefghijklmnopqrstuvwxyz";
  var alphabetArray = [...alphabet];

  // Loop through the string
  for (let index = 0; index < string.length; index++) {
    // Lowercase the current character
    let character = string[index].toLowerCase();
    // Check if the character is in the alphabet array
    if (alphabetArray.indexOf(character) > -1) {
      // If it is remove it from the alphabet array
      alphabetArray.splice(alphabetArray.indexOf(character), 1);
    }
  }

  // If the alphabet array is empty return true, it is a pangram.
  if (alphabetArray.length === 0) {
    return true;
  } else {
    return false;
  }
}

var string = "The quick brown fox jumps over the lazy dog.";

console.log(isPangram(string)); // true

var string2 = "This is not a pangram.";
console.log(isPangram(string2)); // false

// My favorite solution: 

function isPangram(string) {
  return "abcdefghijklmnopqrstuvwxyz"
    .split("")
    .every((x) => string.toLowerCase().includes(x));
}

// I like how they use 'every' to embed the true/false return statement