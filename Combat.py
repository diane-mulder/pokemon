import random
import Pokemon

# règles du jeu et conditions : système de combat
class Combat:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.joueur_courant = p1 if random.randint(0, 1) == 0 else p2

    def lancer(self):
        print(f"Début du combat entre {self.p1.nom} et {self.p2.nom}.")
        while True:
            print(f"{self.joueur_courant.nom} ({self.joueur_courant._points_de_vie} _points_de_vie) c'est à toi de jouer !")
            action = input("Attaquer (A) ou Passer (P) ? ")
            if action.lower() == "a":
                adversaire = self.p2 if self.joueur_courant == self.p1 else self.p1
                self.joueur_courant.attaquer(adversaire)
                if adversaire._points_de_vie <= 0:
                    print(f"{adversaire.nom} est KO, {self.joueur_courant.nom} a gagné !")
                    break
            else:
                print(f"{self.joueur_courant.nom} passe son tour.")
            self.joueur_courant = self.p2 if self.joueur_courant == self.p1 else self.p1


# Création des quatre Pokémon
p1 = Pokemon.Normal("Rattata", 100, 1,1,1)
p2 = Pokemon.Feu("Salameche", 100,1, 1, 1)
p3 = Pokemon.Eau("Carapuce", 100, 1, 1, 1)
p4 = Pokemon.Terre("Sabelette", 100, 1, 2, 1)

# Lancement d'un combat entre les deux 1er Pokémon
combat = Combat(p1, p2)
combat.lancer()

#Lancement de combat entre les 2 derniers Pokemon
combat = combat(p3, p4)
combat.lancer()  











#   def __init__(self, pokemon1, pokemon2):
#     self._pokemon1 = pokemon1
#     self._pokemon2 = pokemon2
#     self._attaquant = None
#     self._defenseur = None
#     self._gagnant = None

#   def _choix_premier_attaquant(self):
#         if random.randint(0, 1) == 0:
#             self._attaquant = self._pokemon1
#             self._defenseur = self._pokemon2
#         else:
#             self._attaquant = self._pokemon2
#             self._defenseur = self._pokemon1

#   def _attaque(self):
#         print(f"{self._attaquant.get_nom()} attaque !")
#         degats = self._attaquant.get_attaque() - self._defenseur.get_defense()
#         if degats < 0:
#             degats = 0
#         self._defenseur.set_pv(self._defenseur.get_pv() - degats)
#         print(f"{self._defenseur.get_nom()} perd {degats} points de vie !")

# # methode qui verifie qui est le vainqueur
#   def _verifie(self):
#         if self._pokemon1.get_points_de_vie() <= 0:
#             self._gagnant = self._pokemon2
#             return True
#         elif self._pokemon2.get_points_de_vie() <= 0:
#             self._gagnant = self._pokemon1
#             return True
#         return False
 
# # methode qui renvoie le nom du vinqueur
#   def renvoie(self):
#       if self._gagnant == self._pokemon1:
#           return self._gagnant.get_nom()
#       else : 
#           return self._pokemon2.get_nom()

# # methode qui calcul les points apres chaque attaque
#   def recupère(self):
#       if self._attaquant.Normal()









        