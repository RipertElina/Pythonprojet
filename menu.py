#Necessaire pour la regex
import re

from matrice import Matrice
matrice = Matrice()

#Definition du menu principale de l'alignement
def menu() : 

 print("\n\nBonjour, bienvenue dans l'outil d'alignement needle\nMenu principal : choississez une rubrique\n")
 print("1. Visualiser les scores\n")
 print("2. Changer les scores\n")
 print("3. Alignement avec deux fichiers de sequence \n")
 print("4. Alignement à partir de deux sequences saisit manuellement\n")
 print("5. Lire l'alignement depuis un fichier de sortie\n")
 print("6. Quitter\n")
 choix = input( "Entrez votre choix (1 a 6)  : \n")
 if choix == "1" : 
  affScore()
  print("Retour au menu")
  menu()
 elif choix == "2" : 
  changeScore()
 elif choix == "3" : 
  AliFile()
 elif choix == "4" : 
  AliManu()
 elif choix == "5" : 
  outFile()
 elif choix == "6" : 
  exit(0)
 else : 
  print("Votre choix n'existe pas, veuillez saisir un nombre en 1 a 6 : \n")
  menu()

#Fonction permettant d'afficher les scores actuels 
def affScore() : 
 print("Score de match : "+str(matrice.getMatch())+"\n")
 print("Score de gap : "+str(matrice.getGap())+"\n")
 print("Score de missmatch : "+str(matrice.getMiss())+"\n")

#Fonction permettant de modifier les scores
def changeScore() : 
 match = input("Score de match : \n")

 try :
  int(match)
 except : 
  print("Merci de saisir une valeur correcte")
  changeScore()

 gap = input("Score de gap : \n")

 try :
  int(gap)
 except : 
  print("Merci de saisir une valeur correcte")
  changeScore()

 mismatch = input("Score de mismatch : \n")

 try :
  int(mismatch)
 except : 
  print("Merci de saisir une valeur correcte")
  changeScore()

 matrice.setMatch(match)
 matrice.setGap(gap)
 matrice.setMiss(mismatch)
 return

#Allignement depuis des sequences prises dans des fichiers externes 
def AliFile() : 
 seq1File = None
 seq2File = None

 print("Bienvenue dans le mode d'alignement de sequence à partir de fichiers d'entres \n")

 fichier1 = input("Entrez le nom du fichier comportant la sequence 1 : (Defaut : seq1.txt) \n")
 if(fichier1 == "") :
  fichier1 = "seq1.txt"

 try : 
  seq1File = open(fichier1, "r")
 except : 
  print("** Le fichier 1 ", fichier1, "est introuvable **")
  AliFile()

 fichier2 = input("Entrez le nom du fichier comportant la sequence 2 : (Defaut : seq2.txt) \n")
 if(fichier2 == "") :
  fichier2 = "seq2.txt"

 try : 
  seq2File = open(fichier2, "r")
 except : 
  print("** Le fichier 2 ", fichier2, "est introuvable **")
  AliFile()
 
 #Lecture des fichiers
 seq1 = seq1File.read()
 seq2 = seq2File.read()

 #Attachement des sequences 
 matrice.setS1(seq1)
 matrice.setS2(seq2)

 print("Lancement de l'alignement \n")
 matrice.needle()

 #Fermeture des fichiers
 seq1File.close()
 seq2File.close()
 consult = input("Alignement terminee, pour consultez en tappant 'O', sinon pressez la touche entree : ")

 if consult.upper() == 'O'  :
  outFile()

 return

#Alignement depuis des sequences saisit manuellement
def AliManu() : 
 print("Bienvenue dans le mode d'alignement de sequence à partir de la saisie manuelle de vos sequences \n")
 seq1 = input("Saisir la premier sequence \n")
 seq2 = input("Saisir la deuxieme sequence \n")

 #Control des cararcteres presents dans les chaines de sequences
 reg = re.compile('^[acdefghikllmnpqrstvwyACDEFGHIKLMNPQRSTVWY]+$')

 if reg.match(seq1) != None and reg.match(seq2) != None:
  matrice.setS1(seq1)
  matrice.setS2(seq2)
  print("Lancement de l'alignement \n")
  matrice.needle() 
  consult = input("Alignement terminee, pour consultez en tappant 'O', sinon pressez la touche entree : ")
  if consult.upper() == 'O'  :
   outFile()

 else :
  print("\n** Veuillez saisir deux séquences correcte **\n")
  AliManu()
 return

#Lit le fichier de sortie
def outFile() :
 try : 
  f = open("outFileRes.txt", "r")
  c = f.read()
  print("---------------------------------------------------------------------------------------")
  print("\n",c)
  print("---------------------------------------------------------------------------------------")
  
  f.close()

 except : 
  print("\n\n** Le fichier de sortie est introuvable, veuillez faire un alignement avant de le consulter **")

 return

#Boucle de menu
while True:
 menu()