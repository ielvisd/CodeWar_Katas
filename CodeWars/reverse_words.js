// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

// Examples
// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"

function reverseWords(str) {
  // New strategy: use a array for the spaces
  var reverseWordsArray = [];
  let currentWord = "";
  let reversedString = ''

  // Loop through the string
  for (let i = 0; i < str.length; i++) {
    // if it's a space
    if (str[i] === " ") {
      // If the previous character is a letter
      if (str[i - 1] !== " ") {
        // add the currentWord to the reverseWordsArray string
        for (j = 0; j < currentWord.length; j++) {
          reverseWordsArray[j + i - currentWord.length] = currentWord[j];
        }
      }
      // add it to the array at the current index
      reverseWordsArray[i] = str[i];
    }

    // if it's a letter & the previous character was a space, reset the word
    if (str[i] !== " " && str[i -1] === " ") {
      currentWord = "";
    }

    // if it's a letter
    if (str[i] !== " ") {
      // add it to the currentWord at the beginning
      currentWord = str[i] + currentWord;
    }

    // if it at the end of the string and it's a character
    if (i === str.length - 1) {
      for (j = 0; j < currentWord.length; j++) {
        reverseWordsArray[i + j - currentWord.length + 1] = currentWord[j];
      }
      for (k = 0; k < reverseWordsArray.length; k++) {
        // if it's a space
        if (reverseWordsArray[k] === " ") {
          reversedString += ` `;
        } else {
          reversedString += reverseWordsArray[k];
        }
      }
      return reversedString;
    }
  }
}

console.log(reverseWords('This is an example!')); // "sihT si na !elpmaxe"
console.log(reverseWords("double  spaced  words")); // "elbuod  secaps"

// My favorite solution: 

function reverseWords(str) {
  return str
    .split(" ")
    .map(function (word) {
      return word.split("").reverse().join("");
    })
    .join(" ");
}

// I had something like this earlier but was getting strange behavior on the tests. To the next one. 