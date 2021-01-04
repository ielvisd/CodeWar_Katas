// Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

// If you want to know more http://en.wikipedia.org/wiki/DNA

// In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

// More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

// DNAStrand ("ATTGC") // return "TAACG"

// DNAStrand ("GTAT") // return "CATA"

function DNAStrand(dna) {
  let complement = "";

  var strandLength = dna.length;

  // Loop through the dna & build up complement string
  for (let i = 0; i < strandLength; i++) {
    if (dna[i] === "A") {
      complement += "T";
    } else if (dna[i] === "T") {
      complement += "A";
    } else if (dna[i] === "C") {
      complement += "G";
    } else if (dna[i] === "G") {
      complement += "C";
    }
  }

  return complement;
}

// Favorite Solution:

var pairs = { A: "T", T: "A", C: "G", G: "C" };

function DNAStrand(dna) {
  return dna
    .split("")
    .map(function (v) {
      return pairs[v];
    })
    .join("");
}

// I like how they used split, map & join along with the pairs object to build up the new string
