import sys
sys.setrecursionlimit(10000)

def find_ugly_number(n):
    if n == 1:
        return 1

    multiplied_by2 = 1
    multiplied_by3 = 1
    multiplied_by5 = 1
    index = 1
    multiples = [2 * multiplied_by2, 3 * multiplied_by3, 5 * multiplied_by5]
    while index < n:
        ugly_index = min(multiples)
        if ugly_index == 2 * multiplied_by2:
            multiplied_by2 += 1
        if ugly_index == 3 * multiplied_by3:
            multiplied_by3 += 1
        if ugly_index == 5 * multiplied_by5:
            multiplied_by5 += 5

        multiples = [2 * multiplied_by2, 3 * multiplied_by3, 5 * multiplied_by5]
        index += 1

    return min(multiples)

if __name__ == "__main__":
    n = 11
    ugly = find_ugly_number(n)
    print(" ugly number of rank: ", n, " is: ", ugly)    
