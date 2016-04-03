'''
TO DO 
Faire une matrice de traceback, creer une matrice de talle seq1 et seq2 puis
quand on calcul le score max, on recupere la val de max genre si c'est diag on dis que c'est D à la position de i,j
Puis on remonde la traceback pour afficher l'alignement 
Si diag : deux lettre l'une en face de l'autre, même si elles sont differentes
Si left : on met un gap sur la seq verticale (la 2) 
Si right : idem mais avec la seq1
Et du coup on peux parcoucrir dans le sens qu'on veux pour ecrire l'allignement ;) 

'''
import numpy


class Matrice:
  #Definition de la classe matrice avec une matrice, deux sequences, les scores de match, mismatch et gap
 def __init__(self):
  self.__mt = []
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
 	self.__s1 = s
 def setS2(self,s) : 
 	self.__s2 = s
 def setScore(self,score) : 
  self.__score = score

 #initialise la matrice (m,n) a zero
 def initZero(self, shape):
  self.__mt = []
  #Ligne
  for x in range(shape[0]):               
   self.__mt.append([])
  #colonne
  for y in range(shape[1]):
   for z in range(shape[1]):
    self.__mt[-1-y].append(0)
  return self.__mt
 
 #Renvoie le score si deux entitées sont egales (match), sinon gap, sinon mismatch 
 def match_score(self, x, y):
  if x == y:
   return self.__match
  elif x == '-' or y == '-':
   return self.__gap
  else:
   return self.__mismatch
  
 #retourne la sequence 1 et 2
 def finalize(self, align1, align2):
  align1 = align1[::-1] 
  align2 = align2[::-1] 
  
  i,j = 0,0
  
  #calcul de l'identite, score et rend l'alignement de sequence 
  symbol = ''
  score = 0
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
        
   identity = round(float(identity) / len(align1) * 100, 2)
  
  outFileRes.write("Score          : "+str(self.getScore())+"\n")
  outFileRes.write("Identite       : "+str(identity)+"%\n")
  outFileRes.write("Sequence 1     : "+str(align1)+"\n")
  outFileRes.write("Sequence 2     : "+str(align2)+"\n")
  outFileRes.write("Correspondance : "+str(symbol)+"\n\n")

  outFileRes.close()
    
  #Rempli la matrice avec les bon scores 
 def needle(self):
  m = len(self.__s1)
  n = len(self.__s2)
  
  #Genere la matrice par programmation dynamique et le chemin de traceback
  score = self.initZero((m+1, n+1))
  #Calcul de la matrice
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
  self.setScore(score[i][j])

  
  #Taceback et calcul l'alignement
  align1 = ''
  align2 = ''
  i = m
  j = n
  while i > 0 and j > 0: 
   score_current = score[i][j]
   score_diagonal = score[i-1][j-1]
   score_up = score[i][j-1]
   score_left = score[i-1][j]
   
   score_match2 = score_current == score_diagonal + self.__match
   score_match = self.match_score(self.__s1[i-1],self.__s2[j-1])

   if (score_current == (score_diagonal + score_match2)) or (score_current == (score_diagonal + score_match2) and (score_current == (score_left + self.__gap))) or (score_current == (score_diagonal + score_match2) and (score_current == (score_up + self.__gap))) or (score_current == (score_diagonal + score_match2) and (score_current == (score_left + self.__gap)) and (score_current == (score_left + self.__gap))) : 
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
   

   '''ICI Y A UN PUTAIN DE PROBLEME'''
   while i > 0:
    align1 += self.__s1[i-1]
    align2 += '-'
    i -= 1
   while j > 0:
    align1 += '-'
    align2 += self.__s2[j-1]
    j -= 1
  
   self.finalize(align1, align2)