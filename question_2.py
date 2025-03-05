from typing import List

# Using Two Pointers If Number Mismatch Swap
def segregate0sToLeftAnd1sToRight(arr: List[int]):
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] == 0: # if 0 move low -> right
            low += 1
        elif arr[high] == 1: # if 1 move high -> left
            high -= 1
        else: # if both mismatch swap
            arr[low] = 0
            arr[high] = 1
            low += 1
            high -= 1

if __name__ == "__main__":
    test_cases = [
        ([0,1,0,0,0,1,0,1,0,1], [0,0,0,0,0,0,1,1,1,1]), # Base Case
        ([1, 1, 0, 0, 1, 0], [0, 0, 0, 1, 1, 1]),  # Mixed case
        ([0, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1]),  # More complex case
        ([1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]),  # 0s and 1s grouped
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),  # Only 0s
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),  # Only 1s
        ([], []),  # Empty array
        ([0], [0]),  # Single element - 0
        ([1], [1]),  # Single element - 1
        ([0, 1], [0, 1]),  # Already ordered
        ([1, 0], [0, 1])  # Needs ordering
    ]

    for i in range(len(test_cases)):
        print('-----------------------------------------------')
        array = test_cases[i][0]
        print(f"Test Case {i + 1}: Input = {array}")
        segregate0sToLeftAnd1sToRight(array)
        expected = test_cases[i][1]
        print(f"Output = {array}, Passed = {array.__eq__(expected)}")
        print('-----------------------------------------------')