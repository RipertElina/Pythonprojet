'''TO DO 
Faire la boucle pour le menu
import os 
Ajouter la priorité diag dans l'alignement'''

def menu() : 
 print("Bonjour, bienvenu dans l'outils d'alignement needle\n Menu principal : choississez une rubrique\n")
 print("1. Visualiser les scores\n")
 print("2. Changer les scores\n")
 print("3. Alignement avec deux fichiers de sequence \n")
 print("4. Alignement à partir de deux sequences saisit manuellement\n")
 print("5. Lire l'alignement depuis un fichier de sortie\n")
 print("6. Quitter\n")

 choix = input( "Entrez votre choix (1 a 6)  : \n")

 if choix == 1 : 
  affScore()
  print("Retour au menu")
  menu()
 if choix == 2 : 
  changeScore()
  print("Retour au menu")
  menu()
 if choix == 3 : 
  AliFile()
  break()
 if choix == 4 : 
  AliManu()
  break()
 if choix == 5 : 
  outFile()
  break()
 if choix == 6 : 
  exit(0)
 elif : 
  print("Votre choix n'existe pas, veuillez saisir un nombre en 1 a 6 : \n")
  menu()




 #Fonction permettant d'afficher les scores actuelles 
 def affScore(self) : 
  print("Score de match : "+str(getMatch())+"\n")
  print("Score de gap : "+str(getGap())+"\n")
  print("Score de missmatch : "+str(getMiss())+"\n")

 #Fonction permettant de changer des scores
 def changeScore(self) : 
  match = imput("Score de match : \n")
  gap = input("Score de gap : \n")
  mismatch = input("Score de mismatch : \n")
  setMatch(match)
  setGap(gap)
  setMiss(mismatch)

 #Allignement depuis des sequence prise dans des fichiers externe 
 def AliFile(self) : 
  print("Bienvenu dans le mode d'alignement de sequence à partir de fichiers d'entres \n")
  fichier1 = raw_input("Entrez le nom du fichier comportant la sequence 1 : \n")
  try : 
   seq1File = open(fichier1, "r")
  except : 
   print("Le fichier", fichier1, "est introuvable")
  fichier2 = raw_input("Entrez le nom du fichier comportant la sequence 2 : \n")
  try : 
   seq2File = open(fichier2, "r")
  except : 
   print("Le fichier", fichier2, "est introuvable")
  seq1 = seq1File.read()
  seq2 = seq2File.read()
  needle(seq1,seq2)
  seq1File.close()
  seq2File.close()

 #Alignement depuis des sequences saisit manuellement
 def AliManu(self) : 
  print("Bienvenu dans le mode d'alignement de sequence à partir de la saisie manuelle de vos sequences \n")
  seq1 = raw_input("Saisir le premier sequence \n")
  seq2 = raw_input("Saisir la deuxieme sequence \n")
  print("Lancement de l'alignement \n")
  needle(seq1,seq2)
  outFile = open("FichierSortiAlignement.txt",w)

 #Lis le fichier de sorti
 def outFile(self) 
  outFileR = open("FichierSortiAlignement.txt", "r")
  contenu = outFileR.read()
  print(contenu)
  outFileR.close()
