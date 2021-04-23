"Third Easy Challenge: Pokemon 1 : https://code-challenge.webandcow.com/5/Team-Pokemon"
"""9.41/10 Pylint"""
class Pokemon:
    """init class"""
    def __init__(self):
        """init list and dict"""
        self.types = [
            "Insecte",
            "Feu",
            "Eau",
            "Eau",
            "Eau",
            "Herbe",
            "Feu",
            "Eau",
            "Feu",
            "Glace",
            "Eau",
            "Eau",
            "Eau",
            "Herbe",
            "Eau",
            "Herbe",
            "Feu",
            "Herbe",
            "Eau",
            "Eau",
            "Glace",
            "Psychique",
            "Feu",
            "Herbe",
            "Herbe",
            "Feu",
        ]
        self.squad = []
        self.squad_rare = []
        self.number_team = 0
        self.bases = ["Eau", "Feu", "Herbe"]
        self.rares = ["Air", "Poison", "Glace", "Psychique", "Insecte"]

    def create_squad(self):
        """This function say how much squad we can
        create with in everyone ,3 basics pokemons and 1 rare type"""
        for base in self.bases:
            self.squad.append(self.types.count(base))
        for rare in self.rares:
            self.squad_rare.append(self.types.count(rare))
        self.number_team = min(min(self.squad), sum(self.squad_rare))
        return self.number_team


Poke = Pokemon()
Poke.create_squad()
