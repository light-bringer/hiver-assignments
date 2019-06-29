'''

Q. Given a 2D array of digits or grid, try to find the occurrence of a given 2D pattern of digits. For example, consider the following grid: 
1 2 3 
4 5 6 
7 8 9 
Assume we need to look for the following 2D pattern in the above grid: 
2 3 
5 6 
The 2D pattern begins at the first row and the second column of the grid. The pattern is said to be 
present in the grid. 


** Function Description **

Complete the search_in_grid function in the editor below. It should return true if the pattern exists in the grid, or false otherwise. 

search_in_grid has the following parameter(s): 
● the grid to search, an array of strings 
● the pattern to search for, an array of strings 

'''

from __future__ import print_function

def search(arr, combination, i, j):
    for row in combination:
        for count, item in enumerate(row):
            if arr[i+count][j] != item:
                return False
        j+=1
    return True

def search_in_grid(arr, combination):
    for i, row in enumerate(arr):
        for j, item in enumerate(row):
            # found the start of the pattern, then start searching therefore
            if item == combination[0][0]:
                if search(arr, combination, i, j):
                    return True
                else:
                    return False
    return False


def main():
    # the map we need to search
    arr = [
        [1, 1, 2, 3, 4, 1, 1],
        [1, 1, 5, 6, 7, 1, 1],
        [1, 1, 2, 7, 4, 1, 1],
        [1, 1, 7, 8, 6, 1, 1]
    ]
    # the combination we need to find
    pattern = [
        [2, 5, 1, 7],
        [3, 6, 7, 8],
        [4, 7, 4, 6]
    ]
    print(search_in_grid(arr, pattern))

def test():
    arr = [
        [1, 2, 3], 
        [4, 5, 6 ],
        [7, 8, 9 ]
    ]
    testcases = [
        [[2, 3],[4, 5],],
        [[2, 3, 4],[4, 5, 6],],
        [[2],]
    ]
    for pattern in testcases:
        print(search_in_grid(arr, pattern))

if __name__ == "__main__":
    test()
    main()