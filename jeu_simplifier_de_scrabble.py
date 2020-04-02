#jeu simplifier de scrabble avec des exceptions du nombre de voyelle qui doit depasser 2 pour que le jeu se poursuit 
#afin un document sera ouvert pour comparer votre arrangement par rapport au mots existants afin de valider ou pas votre jeu 
import random
import string
lettres=["e"]*15+["a"]*9+["i"]*8+["n"]*6+["o"]*6+["r"]*6+["s"]*6+["t"]*6+["k"]*1+["l"]*5+["j"]*1+["q"]*1+["u"]*6+["v"]*2+["w"]*1+["x"]*1+["z"]*1+["y"]*1+["p"]*2+["m"]*3+["f"]*2+["c"]*2+["b"]*2+["d"]*3+["g"]*2+["h"]*2
print("voici le sac plein du scrabble: \n", lettres)
print("le nombre de lettre dans le sac est: \n", len(lettres))
voyelle=['e','a','o','i','u']  #la liste des voyelles
random.shuffle(lettres)#melange du sac
lettre_pioches=[0]*7
i=0
x=0
while i<7:
 	pioche=random.choice(lettres)#prendre une lettre tant que vous ne depasser pas 7 
 	lettre_pioches[i]=pioche
 	i+=1
for lettres in lettre_pioches:#on compare les lettres piochets au liste de voyelles au dessus 
	if lettres in voyelle:
		x+=1
print("les lettres pioches au hazard  sont:",lettre_pioches)
print("le nombre de voyelle pioches:",x)
if x<2:
	print("ceci est est un mauvais tirage reessayer encore ",lettre_pioches)
if x>=2:
	print("ceci est une bonne pioche",lettre_pioches)
jeu_du_joueur=str(input("donner nous un mot a partir de votre pioche: \n"))
print ("vous avez choisi d'arranger votre pioche de cette facon: \n",jeu_du_joueur)
#cette partie du code est a revoir car la boucle de comparaison est trop lente et non performante
existe_in_file=False
with open("/home/maugopro/Bureau/bootcamp/python prog/dictionnaire-fr.txt","r") as fic: #ouverture du dossier dico
	for line in fic.readlines():
		if jeu_du_joueur in line: #une comparaison par rapport au contenue de fichier txt 
			existe_in_file=True
			break
if existe_in_file:		
	print("votre choix est valider par le dictionnaire ")
else:
	print("ceci n'est pas accepter reessayer encore")
#le scroring 
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
total_jeu=0
def le_score(jeu_du_joueur):
	total_jeu=0
	for i in jeu_du_joueur:
		i=i.lower()
		total_jeu=total_jeu+score[i]
	return total_jeu
print("le score est:",total_jeu)
#premier prototype a mettre a jour avec la programmation modulaire 



