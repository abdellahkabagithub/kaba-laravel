#Les listes 
liste = ["Kaba","Kallo","Condé","Camara"] ;
#print(liste)
# modification d'un element
liste[0] = "Diallo"
print(liste)
#Modifier plusieur de plusieurs elements à la fois et à partir d'un indice
liste[2:4] = ["Mara","Sayon"]
print(liste)
#insertion d'un element dans un index spécifique
liste.insert(1, "Mohamed")
#print(liste)
#Ajout dans une liste
liste.append("Issa")
#print(liste)
#Ajout de plusieurs listes
liste.extend(["Ismael","Binta","Sayon"])
#print(liste)
#Enlever ou supprimer un element avec son indice
del liste[1]
liste.pop(1)
#print(liste)

liste2 = ["Kaba","Fanta","Mussa"]
liste2.pop(1)
print(liste2)
#NB supprimer un element par son nom
liste2.remove("Kaba")
print(liste2)
#Supprimer tous les elements de la liste
#del liste2[:] liste2.clear()
print(liste2)