from typing import List


# sort two lists and place pointer on each list handle duplicates
def unionAndIntersection(list1: List[int], list2: List[int]) -> (List[int], List[int]):
    # sort two lists
    list1.sort()
    list2.sort()

    union = list()
    intersection = list()

    i = 0
    j = 0

    n1 = len(list1)
    n2 = len(list2)

    while i < n1 or j < n2:
        # no elements left in list 2 to process or element
        # of list 1 at index i is less than  list 2 at index j
        if j == n2 or (i < n1 and j < n2 and list1[i] < list2[j]):
            element = list1[i]
            union.append(element)
            while i < n1 and list1[i] == element:
                i += 1
        # vice versa of above condition
        elif i == n1 or (i < n1 and j < n2 and list1[i] > list2[j]):
            element = list2[j]
            union.append(element)
            while j < n2 and list2[j] == element:
                j += 1
        # both are equal then add in intersection
        else:
            element = list1[i]
            union.append(element)
            intersection.append(element)
            while i < n1 and list1[i] == element:
                i += 1
            while j < n2 and list2[j] == element:
                j += 1
    return union, intersection


if __name__ == '__main__':
    test_cases = [
        {  # Base Case
            "list1": [7, 8, 9, 10, 7, 9],
            "list2": [5, 6, 7, 1, 4, 8, 3],
            "union": [1, 3, 4, 5, 6, 7, 8, 9, 10],
            "intersection": [7, 8]
        },
        {  # General case with common elements
            "list1": [1, 2, 3, 4],
            "list2": [3, 4, 5, 6],
            "union": [1, 2, 3, 4, 5, 6],
            "intersection": [3, 4]
        },
        {  # Lists with overlapping elements
            "list1": [10, 20, 30],
            "list2": [20, 30, 40, 50],
            "union": [10, 20, 30, 40, 50],
            "intersection": [20, 30]
        },
        {  # Lists with duplicate elements
            "list1": [1, 1, 2, 2],
            "list2": [2, 3, 3, 4],
            "union": [1, 2, 3, 4],
            "intersection": [2]
        },
        {  # One list is empty
            "list1": [5, 6, 7],
            "list2": [],
            "union": [5, 6, 7],
            "intersection": []
        },
        {  # Two list are empty
            "description": "Two list are empty",
            "list1": [],
            "list2": [],
            "union": [],
            "intersection": []
        },
        {  # Lists with no common elements
            "list1": [3, 5, 7, 9],
            "list2": [2, 4, 6, 8],
            "union": [2, 3, 4, 5, 6, 7, 8, 9],
            "intersection": []
        }
    ]

    for i in range(len(test_cases)):
        print('-----------------------------------------------')
        list1 = test_cases[i]['list1']
        list2 = test_cases[i]['list2']
        union = test_cases[i]['union']
        intersection = test_cases[i]['intersection']
        print(f"Test Case {i + 1}:\n\nlist1 = {list1}\nlist2 = {list2}\n")
        result_union, result_intersection = unionAndIntersection(list1, list2)
        print(f'Your Output:\nunion = {result_union}\nintersection = {result_intersection}\n')
        print(f'Expected Output:\nunion = {union}\nintersection = {intersection}')
        print(f'Passed = {union == result_union and intersection == result_intersection}')
        print('-----------------------------------------------')
