# Importation de la bibliothèque random pour générer des nombres aléatoires
import random

# Définition de la classe Pokemon
class Pokemon:
    def __init__(self, nom, pv, attaque, defense):
        self.nom = nom
        self.pv = pv
        self.attaque = attaque
        self.defense = defense

    def attaquer(self, adversaire):
        degats = self.attaque - adversaire.defense
        adversaire.pv -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

# Définition de la classe Combat
class Combat:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.joueur_courant = p1 if random.randint(0, 1) == 0 else p2

    def lancer(self):
        print(f"Début du combat entre {self.p1.nom} et {self.p2.nom}.")
        while True:
            print(f"{self.joueur_courant.nom} ({self.joueur_courant.pv} PV) c'est à toi de jouer !")
            action = input("Attaquer (A) ou Passer (P) ? ")
            if action.lower() == "a":
                adversaire = self.p2 if self.joueur_courant == self.p1 else self.p1
                self.joueur_courant.attaquer(adversaire)
                if adversaire.pv <= 0:
                    print(f"{adversaire.nom} est KO, {self.joueur_courant.nom} a gagné !")
                    break
            else:
                print(f"{self.joueur_courant.nom} passe son tour.")
            self.joueur_courant = self.p2 if self.joueur_courant == self.p1 else self.p1

# Création de deux Pokémon
p1 = Pokemon("Pikachu", 50, 10, 5)
p2 = Pokemon("Carapuce", 70, 8, 7)

# Lancement d'un combat entre les deux 1er Pokemon
combat = Combat(p1, p2)
combat.lancer()

# Lancement de combat entre les 2 derniers Pokemons