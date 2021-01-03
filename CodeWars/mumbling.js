// This time no story, no theory. The examples below show you how to write function accum:

// Examples:

// accum("abcd") -> "A-Bb-Ccc-Dddd"
// accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
// accum("cwAt") -> "C-Ww-Aaa-Tttt"
// The parameter of accum is a string which includes only letters from a..z and A..Z.

function accum(s) {
  // Get the length of the string
  var length = s.length;

  // Initiate the string to be returned
  let mumbling = "";

  // Loop through the length of the string
  for (let i = 0; i < length; i++) {
    // If it's not the first letter add a dash ("-")
    if (i !== 0) {
      mumbling += "-";
    }
    // Add the letter at the current index to the string (capitalized)
    mumbling += s[i].toUpperCase();
    // Add the letter at the current index as many times as index (lowercase)
    mumbling += s[i].toLowerCase().repeat(i);
  }

  return mumbling;
}

accum("ZpglnRxqenU"); // Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu

// My favorite solution:

function accum(s) {
  return [...s]
    .map((element, index) => {
      return element.toUpperCase() + element.toLowerCase().repeat(index);
    })
    .join("-");
}

// Again using the spread operator + map combination is really nice.
// I also like how they used the "join" method
