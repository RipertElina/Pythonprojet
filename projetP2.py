import numpy

class Matrice:
 def __init__(self,s1,s2,match,mismatch,gap):
  self.__mt = []
  self.__s1 = s1
  self.__s2 = s2
  self.__match = match
  self.__mismatch = mismatch
  self.__gap = gap
  
 #initialise la matrice a zero
 def initZero(self, shape):
  self.__mt = []
  for x in range(shape[0]):               #nombre de ligne m de la matrice (m,n)
   self.__mt.append([])
  for y in range(shape[1]):
   for z in range(shape[1]):
    self.__mt[-1-y].append(0)
  return self.__mt
  
 def match_score(self, alpha, beta):
  if alpha == beta:
   return self.__match
  elif alpha == '-' or beta == '-':
   return self.__gap
  else:
   return self.__mismatch
	
 #retourne la sequence 1 et 2
 def finalize(self, align1, align2):
  align1 = align1[::-1] 
  align2 = align2[::-1] 
  
  i,j = 0,0
  
  #calcuate identity, score and aligned sequeces
  symbol = ''
  found = 0
  score = 0
  identity = 0
  for i in range(0,len(align1)):
   # if two AAs are the same, then output the letter
   if align1[i] == align2[i]:
    symbol = symbol + align1[i]
    identity = identity + 1
    score += self.match_score(align1[i], align2[i])
    
   # if they are not identical and none of them is gap
   elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-':
    score += self.match_score(align1[i], align2[i])
    symbol += ' '
    found = 0
    
   #if one of them is a gap, output a space
   elif align1[i] == '-' or align2[i] == '-':
    symbol += ' '
    score += self.__gap
    
    
   identity = float(identity) / len(align1) * 100
   print(identity)
   print(score)
   print(align1)
   print(symbol)
   print(align2)
	 
 def needle(self):
  m = len(self.__s1)
  n = len(self.__s2)
  
  #Generate DP table and traceback path pointer matrix
  score = self.initZero((m+1, n+1))
  # Calculate DP table
  for i in range(0, m + 1):
   score[i][0] = self.__gap * i
  for j in range(0, n + 1):
   score[0][j] = self.__gap * j
  for i in range(1, m + 1):
   for j in range(1, n + 1):
    diag = score[i-1][j-1] + self.match_score(self.__s1[i-1], self.__s2[j-1])
    up = score[i-1][j] + self.__gap
    left = score[i][j-1] + self.__gap
    score[i][j] = max(diag, up, left)	

	
  #Traceback and compute the alignment
  #parcour par programmation dynamike 
  align1, align2 = '', ''
  i,j = m,n
  while i > 0 and j > 0: 
   score_current = score[i][j]
   score_diagonal = score[i-1][j-1]
   score_up = score[i][j-1]
   score_left = score[i-1][j]

   if score_current == score_diagonal + self.match_score(self.__s1[i-1],self.__s2[j-1]):
    align1 += self.__s1[i-1]
    align2 += self.__s2[j-1]
    i -= 1
    j -= 1

   elif score_current == score_left + self.__gap:
    align1 += self.__s1[i-1]
    align2 += '-'
    i -= 1
   elif score_current == score_up + self.__gap:
    align1 += '-'
    align2 += self.__2[j-1]
    j -= 1
   
   # Finish tracing up to the top left cell
   while i > 0:
    align1 += self.__s1[i-1]
    align2 += '-'
    i -= 1
   while j > 0:
    align1 += '-'
    align2 += self.__s2[j-1]
    j -= 1
 	
   self.finalize(align1, align2)
  
  
  
seq1 = "ACTG"
seq2 = "CTTG"
matrice = Matrice(seq1,seq2,4,-4,-4)
matrice.needle()