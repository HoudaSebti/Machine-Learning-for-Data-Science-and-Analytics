import sys
sys.setrecursionlimit(10000)

def merge_sort(list, first, last):
    if first < last:
        mid = int((first + last) / 2)
        merge_sort(list, first, mid)
        merge_sort(list, mid + 1, last)
        merge(list, first, mid, last)
    
            
def merge(list, first, mid, last):
    L = list[first : mid + 1]
    R = list[mid + 1 : last + 1]
    
    i = j = 0
    k = first
    while i < len(L) and j < len(R):
        
        if L[i] > R[j]:
            list[k] = R[j]
            j+=1
        else:
            list[k] = L[i]
            i+=1
        k+=1
    
    while i <len(L):
        list[k] = L[i]
        i+=1
        k+=1
        
    while j < len(R):
        list[k] = R[j]
        j+=1
        k+=1
     
if __name__ == "__main__":
    list1 = [12, 11, 13, 5]
    list2 = [6, 29, 4]
    list3 = [10, 8, 12, 20, 9, 1, 3, 7, 30]
    
    print("list1 before merge sort: ", list1)
    merge_sort(list1, 0, len(list1) - 1)
    print("list1 after merge sort: ", list1)
    
    print("list2 before merge sor: ", list2)
    merge_sort(list2, 0, len(list2) - 1)
    print("list2 after merge sort: ", list2)
    
    print("list3 before merge sort: ", list3)
    merge_sort(list3, 0, len(list3) - 1)
    print("list3 after merge sort: ", list3)