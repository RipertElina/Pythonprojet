#Classe du score de l'allignement
class Score:
 def __init__(self,ma,mi,ga):
  self.__match = ma
  self.__mismatch = mi
  self.__gap = ga
  return
  
 #Get 
 def scoreMa(self) : 
  return self.__match
  
 def scoreMi(self) : 
  return self.__mismatch
  
 def scoreGa(self) : 
  return self.__gap
 
 #Set 
 def set_scoreMa(self,n): 
  self.__match = n
  return 
 def set_scoreMi(self,n): 
  self.__mismatch = n
  return 
 def set_scoreGa(self,n): 
  self.__gap = n
  return

 def __getitem__(cls, x):
  return getattr(cls, x)

#____________________________________________________________________________________________________________

#Classe Matrice d'alignement 
class Matrice:
 def __init__(self,s1,s2):
  self.__mt = []
  self.__s1 = s1
  self.__s2 = s2
  self.__myScore = Score(4,-4,-4)
  return
  
 #Getter 
 def getMt(self) : 
  return self.__mt
 def getS1(self) : 
  return self.__s1
 def getS2(self) : 
  return self.__s2
 
 #Setter
 def set_seqS1(self,s): 
  self.__s1 = s
  return 
 def set_seqS2(self,s): 
  self.__s2 = s
  return 
  
 #Initialise la matrice avec les score de gap sur la premier ligne et premiere colonne (le reste a 0)
 def mtInit(self) : 
  lengthAli1 = len(self.__s1)                         
  lengthAli2 = len(self.__s2)  
  i=0
  j=0
  for i in range(lengthAli1) :
   self.__mt.append([])
   for j in range(lengthAli2) :
    self.__mt[i].append[self.__myScore.scoreGa()*j]
    if i<=1 : 
     self.__mt[i].append([self.__myScore.scoreGa()*i])
     if j<=1 : 
      self.__mt[i].append([0])
   return
 
 #Calcul avec la case du haut 
 def scoreUp(self,i,j) :
  return self.__mt[i-1][j]+self.__myScore.scoreGa()

 #Calcul avec la case de gauche 
 def scoreLeft(self,i,j) : 
  return self.__mt[i][j-1]+self.__myScore.scoreGa()

 #Calcul avec la case diagonale                    
 def scoreDiag(self,i,j) :
  if testMatch() :  
   return mt[i-1][j-1] + self.__myScore.scoreMa(i-1,j-1)
  else :  
   return mt[i-1][j-1] + self.__myScore.scoreGa(i-1,j-1)

 #compare trois valeurs et retourne la meilleur
 def bestScore(x,y,z) :
  if x<=y and x<=z : 
   return x
  elif y<x and y<=z : 
   return y 
  elif z<x and z<y : 
   return z
 
 #test si il y a match (true) ou non 
 def testMatch(self,i,j) : 
  if self.__s1[i] == self.__s2[j] : 
   return True 
  else : 
   return False

 #Remplis la matrice avec la meilleur valeur 
 def mtFilling(self,s1,s2) :
  self.mtInit()
  lengthAli1 = len(self.__s1)                         
  lengthAli2 = len(self.__s2)
  i=1
  j=1
  for i in range(lengthAli1) : 
   for j in range(lengthAli2) : 
   	resBest = bestScore(self.__myScore.scoreDiag(mt[i][j]),self.__myScore.scoreLeft(mt[i][j]),self.__myScore.scoreUp(mt[i][j]))
   	print(resBest)
   	self.__mt[i][j].append(resBest)
   	return

 #Recupere le meilleur score (derniere colonne en bas a droite) 
 def bestAli(self) : 
  i=len(self.__mt-1)
  j=len(self.__mt-1) 
  return self.__mt[i][j]
  

#____________________________________________________________________________________________________________

#Classe Matrice de TrackBack  
class MatriceTB:
 def __init__(self,s1,s2):
  self.__mt = []
  self.__s1 = s1
  self.__s2 = s2
  return
  


  
seq1 = "ACTG"
seq2 = "CTTG"


score = Score(4,-4,-4)
matrice = Matrice(seq1,seq2)
matrice.mtFilling(seq1,seq2)
