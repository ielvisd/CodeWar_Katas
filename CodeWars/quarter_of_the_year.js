// Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

// For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

const quarterOf = (month) => {
  // Assign quarters to variables
  if (month >= 1 && month <= 3) {
    return 1;
  }
  if (month >= 4 && month <= 6) {
    return 2;
  }
  if (month >= 7 && month <= 9) {
    return 3;
  }
  if (month >= 10 && month <= 12) {
    return 4;
  }
};

// My Favorite solution:
const quarterOf = (month) => {
  return Math.ceil(month / 3);
};

// Math.ceil is returning the next largest integer rounded up which is the correct quarter.
