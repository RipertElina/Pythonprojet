import numpy


class Matrice:
 "Definition de la classe matrice avec une matrice, deux sequences, les scores de match, mismatch et gap"
 def __init__(self):
  self.__mt = []
  self.__tbMt = []
  self.__s1 = ''
  self.__s2 = ''
  self.__match = 4
  self.__mismatch = -4
  self.__gap = -4
  self.__score = None 

 #getter
 def getMatch(self) : 
  return self.__match
 def getGap(self) : 
  return self.__gap
 def getMiss(self) : 
  return self.__mismatch
 def getScore(self) : 
  return self.__score

 #setter 
 def setMatch(self,x) : 
  self.__match = int(x)
 def setGap(self,x) : 
  self.__gap = int(x)  
 def setMiss(self,x) : 
  self.__mismatch = int(x)
 def setS1(self,s) : 
    self.__s1 = s.upper()
 def setS2(self,s) : 
    self.__s2 = s.upper()
 def setScore(self,score) : 
  self.__score = score


 #initialise la matrice (m,n) a zero
 def initZero(self, shape):
  self.__mt = []
  #Parcours de ligne
  for x in range(shape[0]):               
   self.__mt.append([])
  #Parcours de colonne
  for y in range(shape[0]):
   for z in range(shape[1]):
    self.__mt[-1-y].append(0)
  return self.__mt

 #Intialise la matrice de Traceback a zero 
 def initZeroTB(self, shape):
  self.__tbMt = []
  #Parcours de ligne
  for x in range(shape[0]):
   self.__tbMt.append([])
  #Parcours de colonne
  for y in range(shape[0]):
   for z in range(shape[1]):
    self.__tbMt[-1-y].append(0)
  return self.__tbMt
 
 #Compare deux valeurs, si elles sont egales  : match, si "-" alors gap, sinon mismatch 
 def match_score(self, x, y):
  if x == y:
   return self.__match
  elif x == '-' or y == '-':
   return self.__gap
  else:
   return self.__mismatch
  
 #retourne la sequence 1 et 2 dans le bon sens
 def finalize(self, align1, align2):
  align1 = align1[::-1] 
  align2 = align2[::-1] 
  i,j = 0,0
  
  #calcul de l'identite et retourne l'alignement de sequence dans un fichier de sortie 
  symbol = ''
  identity = 0
  outFileRes = open("outFileRes.txt","w")

  for i in range(0,len(align1)):
   #Si deux AA sont les meme, on aligne 
   if align1[i] == align2[i]:
    symbol = symbol + '*'
    identity = identity + 1
    
   #Si il y a un mismatch 
   elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-':
    symbol += '!'
    
   #Si gap, sortie d'un espace
   elif align1[i] == '-' or align2[i] == '-':
    symbol += '-'
        

  outFileRes.write("Pour cet alignement ont été utilisés comme scores : \n\n")
  outFileRes.write("Match          : "+str(self.getMatch())+"\n")  
  outFileRes.write("Mismatch       : "+str(self.getMiss())+"\n")  
  outFileRes.write("Gap            : "+str(self.getGap())+"\n\n")

  outFileRes.write("Resultats : \n\n")
  outFileRes.write("Score          : "+str(self.getScore())+"\n")  
  outFileRes.write("Identite       : "+str(identity)+"\n")
  outFileRes.write("Sequence 1     : "+str(align1)+"\n")
  outFileRes.write("Sequence 2     : "+str(align2)+"\n")
  outFileRes.write("Correspondance : "+str(symbol)+"\n\n")

  outFileRes.close()
    
 #Rempli la matrice de score  
 def needle(self):
  m = len(self.__s1)
  n = len(self.__s2)
  
  #Genere la matrice par programmation dynamique et le chemin de traceback, initialisation a zero
  scoreMt = self.initZero((m+1, n+1))
  traceback = self.initZeroTB((m+1,n+1))
  #Remplissage des matrices
  traceback[0][0] = "Done"

  #Premiere colonnes de la matrice
  for i in range(0, m + 1):
   scoreMt[i][0] = self.__gap * i
   try:
    traceback[i+1][0] = "L"
   except:
    pass

  #Premier lignes de la matrice 
  for j in range(0, n + 1):
   scoreMt[0][j] = self.__gap * j
   try:
    traceback[0][j+1] = "U"
   except:
    pass
  
  #Remplissage de la matrice par parcours de (1,1) a (n+1,m+1) avec la meilleur valeur entre diag, up et left
  for i in range(1, m + 1):
   for j in range(1, n + 1):
    diag = scoreMt[i-1][j-1] + self.match_score(self.__s1[i-1], self.__s2[j-1])
    up = scoreMt[i][j-1] + self.__gap
    left = scoreMt[i-1][j] + self.__gap
    val = max(diag, up, left)
    scoreMt[i][j] =  val
    #Compare la valeur de max pour remplir la Traceback
    if val == diag : 
        traceback[i][j] = 'D'
    elif val == up : 
        traceback[i][j] = "U"
    elif val == left : 
        traceback[i][j] = "L"
  self.setScore(scoreMt[i][j])

  #Parcours inversé de la Traceback pour la creation de l'alignement
  align1 = ''
  align2 = ''
  i = m
  j = n
  while traceback[i][j] != "Done" :
   if traceback[i][j] == "D" : 
    align1 += self.__s1[i-1]
    align2 += self.__s2[j-1]  
    i -= 1
    j -= 1

   elif traceback[i][j] == "U" : 

    align1 += '-'
    align2 += self.__s2[j-1]
    j -= 1

   elif traceback[i][j] == "L" : 
    align1 += self.__s1[i-1]
    align2 += '-'
    i -= 1
   
  self.finalize(align1, align2)