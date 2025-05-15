"""
Carlos Gracia
5/14/25

Implements Binary Search iteratively and recursively on a sorted list of items:
"""
import random
import time


def binary_search_iter(items, target):
    #items must be sorted list of numbers for this code to work
    low_point = 0
    high_point = len(items) - 1

    while low_point <= high_point:
        #print(items[low_point:high_point + 1])
        mid_point = (high_point + low_point) // 2
        if items[mid_point] < target:
            low_point = mid_point + 1
        elif items[mid_point] == target:
            return mid_point
        else:
            high_point = mid_point - 1

    return -1 #return negative one if number does not exist in list
                     
def binary_search_recur(items, target):
    #items must be sorted list of numbers for this code to work
    #print(items)
    mid_point = (len(items) - 1) // 2 # gets the middle index
    return_index = 0

    if len(items) == 0:
        return -1 # the list is empty, therefore the target does not exist in it
    elif items[mid_point] == target:
        return mid_point # target found
    elif items[mid_point] < target:
        return_index = binary_search_recur(items[mid_point + 1:], target)
        return return_index + mid_point + 1 if return_index != -1 else -1 # target is greater than midpoint
    else:
        return binary_search_recur(items[:mid_point], target) # target is less than midpoint

def quick_sort(items):
    # print(f"Running: {items}")
    if len(items) >= 10:
        first = items[0]
        middle = items[len(items) // 2]
        last = items[-1]
        if middle > last:
            if middle > first:
                pivot = middle
            else:
                pivot = first
        else:
            if last > first:
                pivot = last
            else:
                pivot = first
    elif items != []:
        pivot = items[len(items) // 2] 
    else:
        return []
    less_than_pivot = []
    greater_than_pivot = []
    same_pivot = []

    for item in items:
        if item < pivot:
            less_than_pivot.append(item)
        elif item > pivot:
            greater_than_pivot.append(item)
        else:
            same_pivot.append(item)
    
    less_than_pivot = quick_sort(less_than_pivot) if less_than_pivot != [] else []
    greater_than_pivot = quick_sort(greater_than_pivot) if greater_than_pivot != [] else []

    return less_than_pivot + same_pivot + greater_than_pivot

def merge_sort(items):
    # print(f"Running: {items}")
    if len(items) >= 2:
        midpoint = (len(items)) // 2
        # print(f"First half: {items[:midpoint]}")
        # print(f"Second half: {items[midpoint:]}")
        half1 = merge_sort(items[:midpoint])
        half2 = merge_sort(items[midpoint:])
        
        sorted_list = []
        while half1 != None or half2 != None:
            # print(sorted_list)
            if half1 == []:
                sorted_list.extend(half2)
                return sorted_list
            elif half2 == []:
                sorted_list.extend(half1)
                return sorted_list
            elif half1[0] >= half2[0]:
                sorted_list.append(half2.pop(0))
            else:
                sorted_list.append(half1.pop(0))
        
    elif len(items) <= 1:
        return items

# test lists for convenience
odd_list = [1, 3, 5, 7, 9]
even_list = [2, 4, 6, 8]

# full test lists for binary search
test_cases_1 = [(odd_list, 5), (odd_list, 1), (odd_list, 9), (odd_list, 4), ([], 4), ([1], 1), ([1], 4), (even_list, 4), (even_list, 5)]
# uncomment for heavy tests
# test_cases_1.append((list(range(1000)), 678))

# full test lists for sorts
test_cases_2 = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [4, 1, 3, 4, 2, 1], [], [7], [9, 3], [0, -5, 3, -1, 2], [2, 2, 2, 2], [10, -2, 33, 0, 5]]
# uncomment for single large test case
shuffled = list(range(1000))
random.shuffle(shuffled)
# test_cases_2.append(shuffled)

# random, unsorted test lists for sorts
test_cases_3 = []
for i in range(100):
    one_test = []
    for i in range(10000):
        one_test.append(random.randint(0, 100000))
    test_cases_3.append(one_test)

# random, sorted test lists for sorts
test_cases_4 = []
for i in range(100):
    one_test = []
    for i in range(10000):
        one_test.append(random.randint(0, 100000))
    one_test.sort()
    test_cases_4.append(one_test)


print("=== Iterative Test ===")
for case in test_cases_1:
    start = time.perf_counter_ns()
    # result = binary_search_iter(case[0], case[1])
    # print(f"{case[0]}, target: {case[1]}, result: {result}")
    end = time.perf_counter_ns()
    duration = end - start
    print(f"{case} runtime: {duration} ns")

print("\n=== Recursive Test ===")
for case in test_cases_1:
    start = time.perf_counter_ns()
    # result = binary_search_recur(case[0], case[1])
    # print(f"{case[0]}, target: {case[1]}, result: {result}")
    end = time.perf_counter_ns()
    duration = end - start
    print(f"{case} runtime: {duration} ns")


print("\n=== Merge Sort Average Runtime ===")
total_duration_ms = 0
num_cases_ms = 0
for case in test_cases_3:
    start = time.perf_counter_ns()
    # print(f"{case}: {merge_sort(case)}")
    end = time.perf_counter_ns()
    duration = end - start
    # print(f"{case} runtime: {duration} ns")
    total_duration_ms += duration
    num_cases_ms += 1
print(f"Unsorted lists: {total_duration_ms / num_cases_ms} ns")

total_duration_ms = 0
num_cases_ms = 0
for case in test_cases_4:
    start = time.perf_counter_ns()
    # print(f"{case}: {merge_sort(case)}")
    end = time.perf_counter_ns()
    duration = end - start
    # print(f"{case} runtime: {duration} ns")
    total_duration_ms += duration
    num_cases_ms += 1
print(f"Sorted lists: {total_duration_ms / num_cases_ms} ns")

print("\n=== Quick Sort Average Runtime ===")
total_duration_qs = 0
num_cases_qs = 0
for case in test_cases_3:
    start = time.perf_counter_ns()

    # print(f"{case}: {merge_sort(case)}")
    
    end = time.perf_counter_ns()
    duration = end - start

    # print(f"{case} runtime: {duration}")

    total_duration_qs += duration
    num_cases_qs += 1
print(f"Unsorted lists: {total_duration_qs / num_cases_qs} ns")
total_duration_qs = 0
num_cases_qs = 0
for case in test_cases_4:
    start = time.perf_counter_ns()

    # print(f"{case}: {merge_sort(case)}")
    
    end = time.perf_counter_ns()
    duration = end - start

    # print(f"{case} runtime: {duration}")

    total_duration_qs += duration
    num_cases_qs += 1
print(f"Sorted lists: {total_duration_qs / num_cases_qs} ns")