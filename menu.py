'''TO DO 
Ajouter la priorité diag dans l'alignement'''

from matrice import Matrice
matrice = Matrice()

def menu() : 

 while True:
  print("Bonjour, bienvenue dans l'outil d'alignement needle\n Menu principal : choississez une rubrique\n")
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
   print("Retour au menu")
   menu()
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


#Fonction permettant d'afficher les scores actuelles 
def affScore() : 
 print("Score de match : "+str(matrice.getMatch())+"\n")
 print("Score de gap : "+str(matrice.getGap())+"\n")
 print("Score de missmatch : "+str(matrice.getMiss())+"\n")

#Fonction permettant de changer des scores
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

#Allignement depuis des sequence prise dans des fichiers externe 
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
  print("Le fichier 1 ", fichier1, "est introuvable")
  AliFile()

 fichier2 = input("Entrez le nom du fichier comportant la sequence 2 : (Defaut : seq2.txt) \n")
 if(fichier2 == "") :
  fichier2 = "seq2.txt"

 try : 
  seq2File = open(fichier2, "r")
 except : 
  print("Le fichier 2 ", fichier2, "est introuvable")
  AliFile()
 
 # On lit les fichiers
 seq1 = seq1File.read()
 seq2 = seq2File.read()

 # On set les sequences correspondantes
 matrice.setS1(seq1)
 matrice.setS2(seq2)

 print("Lancement de l'alignement \n")
 matrice.needle()

 # On ferme les fichiers en ecriture
 seq1File.close()
 seq2File.close()
 return

#Alignement depuis des sequences saisit manuellement
def AliManu() : 
 print("Bienvenu dans le mode d'alignement de sequence à partir de la saisie manuelle de vos sequences \n")
 seq1 = input("Saisir la premier sequence \n")
 seq2 = input("Saisir la deuxieme sequence \n")
 matrice.setS1(seq1)
 matrice.setS2(seq2)
 print("Lancement de l'alignement \n")
 matrice.needle()
 return

#Lis le fichier de sorti
def outFile() :
 outFileR = open("FichierSortiAlignement.txt", "r")
 contenu = outFileR.read()
 print(contenu)
 outFileR.close()

menu()