from typing import List


# store the elements of first window in map with its number of occurrence
# from the next widow update the removed and added in map
# size of the map is number of unique elements in window
def distinctElementsCountOfEachWindow(arr: List[int], K: int):
    freq_map = {}
    # store the elements with freq in first window
    for i in range(K):
        freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
    result = [len(freq_map)]  # add the first count

    # Update the count of removed and added as per window
    # also append each unique element size of window
    for i in range(K, len(arr)):
        removed_idx = i - K
        if freq_map[arr[removed_idx]] > 1:
            freq_map[arr[removed_idx]] -= 1
        else:
            freq_map.pop(arr[removed_idx])
        freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
        result.append(len(freq_map))

    return result


if __name__ == '__main__':
    test_cases = [
        {  # Base Case
            'arr': [1, 2, 1, 3, 4, 2, 3],
            'K': 4,
            'result': [3, 4, 4, 3]
        },
        {  # With duplicates on last window
            'arr': [1, 2, 1, 2, 3, 3, 3],
            'K': 3,
            'result': [2, 2, 3, 2, 1]
        },
        {  # Only Duplicates
            'arr': [1, 1, 1, 1, 1],
            'K': 2,
            'result': [1, 1, 1, 1]
        },
        {  # No Duplicates
            'arr': [1, 2, 3, 4, 5],
            'K': 5,
            'result': [5]
        },
        {  # same elements in two window
            'arr': [2, 2, 2, 1, 2, 2, 2],
            'K': 4,
            'result': [2, 2, 2, 2]
        }
    ]

    for i in range(len(test_cases)):
        print('-----------------------------------------------')
        arr = test_cases[i]['arr']
        K = test_cases[i]['K']
        result = test_cases[i]['result']
        print(f"Test Case {i + 1}:\n\narr = {arr}\nwindow_size = {K}\n")
        output = distinctElementsCountOfEachWindow(arr, K)
        print(f'Your Output: {output}')
        print(f'Expected Output: {result}')
        print(f'Passed: {result == output}')
