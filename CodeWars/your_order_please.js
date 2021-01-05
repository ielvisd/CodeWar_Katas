function order(words) {
  // if the string is empty, return an empty string
  let stringLength = words.length;

  if (stringLength === 0) {
    return "";
  }

  let returnString = "";

  // Initialize a wordOrder array which will contain the words in the correct index
  let wordOrder = [];
  let currentWord = "";
  let currentIndex = null;

  // loop through the given words
  for (let i = 0; i < stringLength; i++) {
    // If it's a letter, add it to the current word
    if (isNaN(words[i])) {
      currentWord += words[i];
    }
    // If it's a number, add it to the current word & save the index
    if (!isNaN(parseInt(words[i]))) {
      // parseInt converts the string to a number
      currentWord += words[i];
      currentIndex = parseInt(words[i]);
    }
    // If it's a space or the last letter, add the word and letter to the wordOrder array
    // Reset the current word to an empty string
    if (words[i] === " " || i === stringLength - 1) {
      wordOrder[currentIndex] = currentWord;
      currentWord = "";
    }
  }

  // Build up and return the string from the ordered array
  // Start at 1 to skip the 0th, empty entry, numbers are only from 1-9
  for (let i = 1; i < wordOrder.length; i++) {
    returnString += wordOrder[i];
    // Don't add a space at the final word
    if (i !== wordOrder.length - 1) {
      returnString += " ";
    }
  }

  return returnString;
}

// My favorite solution: 
function order(words) {
  return words
    .split(" ")
    .sort(function (a, b) {
      return a.match(/\d/) - b.match(/\d/);
    })
    .join(" ");
}    

// Uses the split and the regexp to sort in place. Pretty cool to wrap it up with the join. Short too. 