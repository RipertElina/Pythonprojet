'''
TO DO 

Faire une matrice de traceback, creer une matrice de talle seq1 et seq2 puis
quand on calcul le score max, on recupere la val de max genre si c'est diag on dis que c'est D à la position de i,j
Puis on remonde la traceback pour afficher l'alignement 
Si diag : deux lettre l'une en face de l'autre, même si elles sont differentes
Si left : on met un gap sur la seq verticale (la 2) 
Si right : idem mais avec la seq1
Et du coup on peux parcoucrir dans le sens qu'on veux pour ecrire l'allignement ;) 

Fichier qui peuvent faire des longeurs differentes 
Extension de gap

'''
import numpy


class Matrice:
  #Definition de la classe matrice avec une matrice, deux sequences, les scores de match, mismatch et gap
 def __init__(self):
  self.__mt = []
  self.__tbMt = []
  self.__s1 = ''
  self.__s2 = ''
  self.__match = 4
  self.__mismatch = -4
  self.__gap = -4
  self.__score = None 
  self.__extension = 0.5

 #getter
 def getMatch(self) : 
  return self.__match
 def getGap(self) : 
  return self.__gap
 def getMiss(self) : 
  return self.__mismatch
 def getScore(self) : 
  return self.__score
 def getExt(self) : 
  return self.__extension

 #setter 
 def setMatch(self,x) : 
  self.__match = int(x)
 def setGap(self,x) : 
  self.__gap = int(x)  
 def setMiss(self,x) : 
  self.__mismatch = int(x)
 def setExt(self,e) : 
  self.__extension = e
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

 def initZeroTB(self, shape):
  self.__tbMt = []
  #Ligne
  for x in range(shape[0]):
   self.__tbMt.append([])
  #colonne
  for y in range(shape[1]):
   for z in range(shape[1]):
    self.__tbMt[-1-y].append(0)
  return self.__tbMt
 
 #Renvoie le score si deux entitées sont egales (match), sinon gap, sinon mismatch 
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
  
  #calcul de l'identite et rend l'alignement de sequence 
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
  scoreMt = self.initZero((m+1, n+1))
  traceback = self.initZeroTB((m+1,n+1))
  #Calcul de la matrice
  traceback[0][0] = "Done"
  #colonnes
  for i in range(0, m):
   scoreMt[i][0] = self.__gap * i
   traceback[i+1][0] = "L"
  #Lignes
  for j in range(0, n):
   scoreMt[0][j] = self.__gap * j
   traceback[0][j+1] = "U"
  for i in range(1, m + 1):
   for j in range(1, n + 1):
    diag = scoreMt[i-1][j-1] + self.match_score(self.__s1[i-1], self.__s2[j-1])
    up = scoreMt[i-1][j] + self.__gap
    left = scoreMt[i][j-1] + self.__gap
    extUp = scoreMt[i-1][j] + self.__extension
    extLeft = scoreMt[i][j-1] + self.__extension
    '''Regarder si avant il y a un - si oui, ajour extUp ou extLeft, ca change le score'''
    val = max(diag, up, left)
    scoreMt[i][j] =  val
    if val == diag : 
        traceback[i][j] = 'D'
    elif val == up : 
        traceback[i][j] = "U"
    elif val == left : 
        traceback[i][j] = "L"
  self.setScore(scoreMt[i][j])

  #Taceback et calcul l'alignement
  align1 = ''
  align2 = ''
  i = m
  j = n
  while traceback[i][j] != "Done" :
   if traceback[i][j] == "D" : 
    align1 += self.__s1[i-1]
    align2 += self.__s2[j-1]  
    scoreTot +=   
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