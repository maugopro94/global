#jeu de carte "bataille" avec la particularite d'omettre les cartes qui se ressemble et d'afficher les cartes differents des deux tirages effectifs
from random import*
#declaration des jeux de carte
liste1=["As","2","3","4","5","6","7","8","9","10","Vallet","Dame","Roi"]
couleur=["Coeur","Carreau","Pique","Trèfle"]
jeu1=[]
jeu2=[]
compare=[]
#les jeux etant melanger avec les particularites 
for type in couleur:
	for element in liste1:
		combinaison=element+type
		jeu1.append(combinaison)
		jeu2.append(combinaison)
print(jeu1)
print("\n la taille de jeu 1 est: ",len(jeu1))#affichage de la taille du jeu 
print(jeu2)
print("\n la taille de jeu 2 est: ",len(jeu2))
#affiger des elements d'une liste au hazard avec la syntaxe sample de random
game1=sample(jeu1,10)
print("les carte tirer au hazard dans le jeu1 est:\n", game1)
game2=sample(jeu2,10)
print("les carte tirer au hazard dans le jeu2 est:\n", game2)
#trouvons les cartes identiques dans les deux tirages
for element1 in game1:
	for element2  in game2:
		if element1==element2:
			compare.append(element1)
		else:
			pass
print("les cartes identiques sont: \n",compare)