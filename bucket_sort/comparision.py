from quick_sort import quick_sort, hoare_quick_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
import time
import random


def comparision():
    # Generate a random list of 10000 elements
    random_list = random.sample(range(1, 20000000), 2000000)

    # Quick sort
    start_time = time.time()
    quick_sort.quickSortAlternative(random_list, 0, len(random_list) - 1)
    quick_sort_time = time.time() - start_time

    # Merge sort
    start_time = time.time()
    merge_sort.mergeSort(random_list)
    merge_sort_time = time.time() - start_time

    # Heap sort
    start_time = time.time()
    heap_sort.heapSort(random_list)
    heap_sort_time = time.time() - start_time

    print("Quick sort time: ", quick_sort_time)
    print("Merge sort time: ", merge_sort_time)
    print("Heap sort time: ", heap_sort_time)


if __name__ == "__main__":
    comparision()
