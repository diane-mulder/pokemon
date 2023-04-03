import random

# determiner les attributs des joueurs
class Pokemon:
    def __init__(self, nom, points_de_vie,attaque, defense):
               self._nom = nom
               self._points_de_vie = points_de_vie
               self.attaque = attaque
               self.defense = defense

    def set_nom(self,nom):
        self._nom = nom
    
    def get_nom(self):
        return self._nom

    def set_point_de_vie(self, point_de_vie):
        self._points_de_vie = point_de_vie
    
    def get_point_de_vie(self):
        return self._points_de_vie


# infos generales du pokemon
    def afficher_informations(self):
        print(f"{self._nom},{self._points_de_vie}, {self.defense}, {self.attaque}")

# principe du jeu avec regle des points
    def attaquer(self, adversaire):
        degats = self.attaque - adversaire.defense
        adversaire._points_de_vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")



# Definir les 4 types de Pokemon : 
class Normal(Pokemon):
    def __init__(self, nom, points_de_vie, attaque, defense):    
        Pokemon.__init__(self, nom, points_de_vie, attaque,defense)


class Feu(Pokemon):
    def __init__(self, nom, points_de_vie, attaque, defense):    
        Pokemon.__init__(self, nom, points_de_vie, attaque, defense)


class Eau(Pokemon):
    def __init__(self, nom, points_de_vie, attaque, defense):    
        Pokemon.__init__(self, nom, points_de_vie, attaque, defense)

class Terre(Pokemon):
    def __init__(self, nom, points_de_vie, attaque, defense):    
        Pokemon.__init__(self, nom, points_de_vie, attaque, defense)         


