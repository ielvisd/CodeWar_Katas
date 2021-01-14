// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

// Examples
// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"

function reverseWords(str) {
  // New strategy: use a array for the spaces
  let reverseWords = [];
  let currentWord = "";
  let priorSpace = false

  // Loop through the string
  for (let i = 0; i < str.length; i++) {

    // if it's a letter, add it to the end of the current word
    if (str[i] !== " ") {
        console.log(priorSpace)
      // if there's a prior space, add the previous word to the reverse string
      if (priorSpace) {
          reverseWords += currentWord;
      }
      console.log(reverseWords)
      currentWord = str[i] + currentWord;
      console.log(currentWord);
    }

    // if it's a space
    if (str[i] === " ") {
        console.log(i)
        priorSpace = true
      // if the previous character was a letter, this word will end at the next letter or end of string
      let previous = i - 1;

      if (str[previous] !== " ") {
        let newWord = false;
      }
      currentWord += str[i];

      if (newWord === true) {
        // reverseWords += currentWord;
      }
    //   // reset current word
    //   currentWord = "";
    }

    // if it's the last letter
    if (i === str.length - 1) {
      console.log(reverseWords);
      // add the current word to the reverseWords string
      reverseWords += currentWord;
      return reverseWords;
    }
  }
}

console.log(reverseWords('This is')); // "sihT si na !elpmaxe"
// console.log(reverseWords("double  spaces")); // "elbuod  secaps"
