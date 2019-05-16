"""
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""


class Solution:

    # Algorithm

    def isValid(self, s):
        # If the string is empty, return true
        if len(s) == 0:
            return True

        # Dictionary of bracket pairs:
        bracket_pairs = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        length_of_string = len(s)

        index = 0

        opening_brackets = "({["
        closing_brackets = ")}]"

        # For every character in the string
        while len(s)>0:

            try:

              leading_character = s[index]
              closing_character = bracket_pairs[leading_character]
              print(closing_character)

              # Check remaining characters
              for remaining_index in range(index + 1, len(s) - index):
                print(remaining_index)
                print(s[remaining_index])

                remaining_character = s[remaining_index]

                # Check if it's an opening bracket

                if remaining_character not in opening_brackets:

                  leading_character = s[remaining_index - 1]

                  bad_closing_brackets = closing_brackets.replace(closing_character, "", 1)

                  bad_bracket_one = bad_closing_brackets[0]
                  bad_bracket_two = bad_closing_brackets[1]

                  if remaining_character == bad_bracket_one or remaining_character==bad_bracket_two:

                    return False
                    pass

                  elif remaining_character == closing_character:

                    s = (s.replace(leading_character, '', 1))
                    s = (s.replace(closing_character, '', 1))
                    pass

            except:
              return False

        return True



solution = Solution()

print(solution.isValid(""))

print(solution.isValid("(())"))

"""
Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true 
"""
