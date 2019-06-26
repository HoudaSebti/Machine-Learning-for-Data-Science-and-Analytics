import sys
sys.setrecursionlimit(10000)

def longest_common_subsequence(list1, list2):

  lcs = [[None]*(len(list2) + 1) for i in range(len(list1) + 1)] 
  for i in range(0, len(list1) + 1):
    for j in range(0, len(list2) + 1):
      if i == 0 or j == 0:
        lcs[i][j] = 0
      elif list1[i - 1] == list2[j - 1]:
        lcs[i][j] = lcs[i - 1][j - 1] + 1
      else:
        lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

  return lcs[len(list1)][len(list2)]

if __name__ == "__main__":
  X = "AGGTAB"
  Y = "GXTXAYB"
  lcs = longest_common_subsequence(X, Y)
  print("logest common subsequence is: ", lcs)
