#jeu simplifier de scrabble avec des exceptions 
import random
lettres=["E"]*15+["A"]*9+["I"]*6+["N"]*6+["O"]*6+["R"]*6+["S"]*6+["T"]*6
print("voici le sac plein du scrabble", lettres)
print("le nombre de lettre dans le sac est: ", len(lettres))
voyelle=['E','A','O','I',]  #la liste des voyelles
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
print("les lettres pioches sont:",lettre_pioches)
print("le nombre de voyelle pioches:",x)
if x<2:
	print("ceci est est un mauvais tirage",lettre_pioches)
if x>=2:
	print("ceci est une bonne pioche",lettre_pioches)
