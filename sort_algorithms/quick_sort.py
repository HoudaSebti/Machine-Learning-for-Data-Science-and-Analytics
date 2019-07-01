import random
import sys
sys.setrecursionlimit(10000)

def quick_sort(list, first, last):
    if first < last:
        
        pivot_idx = adjust_pivot_idx(list, first, last)
        quick_sort(list, first, pivot_idx - 1)
        quick_sort(list, pivot_idx + 1, last )


def adjust_pivot_idx(list, first, last):

    pivot = list[last]
    print("pivot=",pivot)
    i = first - 1
    for j in range(first, last):
        if list[j] <= pivot:
            i=+1
            tmp = list[j]
            list[j] = list[i]
            print("listj=",list[j])
            list[i] = tmp
    print("i=", i )

    tmp = list[i + 1]
    list[i + 1] = pivot
    list[last] = tmp
    print("list=",list)
    
    return i + 1
if __name__ == "__main__":
    list1 = [12, 11, 13, 5]
    list2 = [6, 29, 4]
    #list3 = [10, 8, 12, 20, 9, 1, 3, 7, 30]
    
    print("list1 before quick sort: ", list1)
    quick_sort(list1, 0, len(list1) - 1)
    print("list1 after quick sort: ", list1)
    
    print("list2 before quick sor: ", list2)
    quick_sort(list2, 0, len(list2) - 1)
    print("list2 after quick sort: ", list2)
    
   # print("list3 before quick sort: ", list3)
   # quick_sort(list3, 0, len(list3) - 1)
   # print("list3 after quick sort: ", list3)