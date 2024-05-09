import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
      m = len(S)
      n = len(T)
     
      fMED = [[0 for x in range(n + 1)] for x in range(m + 1)]
      for i in range(m + 1):
        for j in range(n + 1):
          if i == 0:
            fMED[i][j] = j # Min. operations = j
          elif j == 0:
            fMED[i][j] = i
          elif S[i-1] == T[j-1]:
            fMED[i][j] = fMED[i-1][j-1]
          else:
            fMED[i][j] = 1 + min(fMED[i][j-1], fMED[i-1][j], fMED[i-1][j-1])
      return fMED

def fast_align_MED(S, T, MED={}):
    fMED = fast_MED(S, T)
    S_align = []
    T_align = []
    i = len(S)
    j = len(T)
    while True:
      if(i == 0 and j==0):
        break
      else:
        insert = fMED[i][j-1]
        remove = fMED[i-1][j]
        sub = fMED[i-1][j-1]
        minimum = min(insert,remove,sub)
        if(sub == minimum):
          S_align = [S[i-1]] + S_align
          T_align = [T[j-1]] + T_align
          i = i-1
          j = j-1
        elif(insert == minimum):
          S_align = ['-'] + S_align
          T_align = [T[j-1]] + T_align
          j = j-1
        elif(remove == minimum):
          T_align = ['-'] + T_align
          S_align = [S[i-1]] + S_align
          i = i-1

    s_str = ""
    t_str = ""
    s_str = s_str.join(S_align)
    t_str = t_str.join(T_align)

    return s_str, t_str

