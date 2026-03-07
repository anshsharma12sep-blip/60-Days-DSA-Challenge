

def binary_search_iterative(arr, target):
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1 
    
    return -1  



if __name__ == "__main__":
   
    arr = [1, 3, 5, 7, 9, 11, 13]

    targets = [7, 1, 13, 4, 0, 15]
    
    for target in targets:
        index = binary_search_iterative(arr, target)
        if index != -1:
            print(f"Element {target} found at index {index}")
        else:
            print(f"Element {target} not found in the array")


    empty_arr = []
    print("Searching in empty array:", binary_search_iterative(empty_arr, 5)) 


    single_arr = [10]
    print("Searching 10 in single-element array:", binary_search_iterative(single_arr, 10))  
    print("Searching 5 in single-element array:", binary_search_iterative(single_arr, 5))   