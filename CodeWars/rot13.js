// ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

// Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

function rot13(message) {
  let rot13Message = "";
  let messageLength = message.length;

  // Loop through the message
  for (let i = 0; i < messageLength; i++) {
    let varShiftBy = 13;
    // If character is between 'A' & 'Z' shift it by 13 characters
    // 'A' = 65 & 'Z' = 90
    if (message[i].charCodeAt() >= 65 && message[i].charCodeAt() <= 90) {
      let charcode = message[i].charCodeAt() + 13;
      // If past Z (90), go back to 'A' and contiue count from there
      if (charcode > 90) {
        let varShiftBy = charcode - 91;
        charcode = 65 + varShiftBy;
      }
      rot13Message += String.fromCharCode(charcode);
    }
    // Else if character is between 'a' & 'z' shift it by 13 characters
    // 'a' = 97 & 'z' = 123
    else if (message[i].charCodeAt() >= 97 && message[i].charCodeAt() <= 122) {
      let charcode = message[i].charCodeAt() + 13;
      // If past z (122), go back to 'a' and count from there
      if (charcode > 122) {
        let varShiftBy = charcode - 123;
        charcode = 97 + varShiftBy;
      }
      rot13Message += String.fromCharCode(charcode);
    } else {
      rot13Message += String.fromCharCode(message[i].charCodeAt());
    }
  }

  return rot13Message;
}

console.log(rot13("TesZ")); //grfg

// Test.describe("Rot13", function () {
//   Test.it("test", function () {
//     Test.expect(
//       "grfg" == rot13("test"),
//       "Input: test , Expected Output: grfg , Actual Output: " + rot13("test")
//     );
//   });
//   Test.it("Test", function () {
//     Test.expect(
//       "Grfg" == rot13("Test"),
//       "Input: Test , Expected Output: Grfg , Actual Output: " + rot13("Test")
//     );
//   });
// });

// My favorite solution: 

function rot13(message) {
  var a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  var b = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM";
  return message.replace(/[a-z]/gi, (c) => b[a.indexOf(c)]);
}

// Although it it may not be the cleanest solutoin it's very readable. 
