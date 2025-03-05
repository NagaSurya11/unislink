# The logic behind the recursion is remove the ending duplicates and take only starting value
def removeConsecutiveDuplicates(s: str, prev_idx: int = 0, curr_idx: int = 1) -> str:
    n = len(s)
    if n == 0: # Edge Case if length is 0
        return ''
    if curr_idx == n: # idx exceeds add last char
        return s[prev_idx]

    if s[prev_idx] == s[curr_idx]: # if same char skip the curr_idx
        return removeConsecutiveDuplicates(s, prev_idx, curr_idx + 1)
    else:
        return s[prev_idx] + removeConsecutiveDuplicates(s, curr_idx, curr_idx + 1)

if __name__ == "__main__":
    test_cases = [
        ("AAABCCDDEDDE", "ABCDEDE"),  # General case with duplicates
        ("AABBCC", "ABC"),  # Consecutive duplicates at different positions
        ("A", "A"),  # Single character case
        ("", ""),  # Empty string case
        ("AAAAAA", "A"),  # All characters are the same
        ("ABABAB", "ABABAB"),  # No consecutive duplicates
        ("AABBBAA", "ABA"),  # Mixed duplicates
        ("XYZZZZYX", "XYZYX"),  # Duplicates in the middle and end
        ("aabbAABB", "abAB"),  # Case-sensitive check
    ]

    for i in range(len(test_cases)):
        print('-----------------------------------------------')
        print(f"Test Case {i + 1}: Input = {test_cases[i][0]}")
        input_str = test_cases[i][0]
        output = removeConsecutiveDuplicates(input_str)
        expected = test_cases[i][1]
        print(f"Output = {output}, Passed = {output.__eq__(expected)}")
        print('-----------------------------------------------')
