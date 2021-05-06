"""Fourth Easy Challenge: Avengers : https://code-challenge.webandcow.com/6/Avengers"""
"""9.14/10 Pylint"""


class Avengers:
    """Init class of the Avengers """
    def __init__(self, thanos):
        """Init variables"""
        self.competances = [0, 0, 0, 0]
        self.heroes_name = ["ironman", "spiderman", "captain america", "thor"]
        self.thanos = thanos
        self.round = 1
        self.ironman = (self.competances[0] * 3) + 10
        self.spiderman = (self.competances[1] * 4) + 5
        self.captain = (self.competances[2] * 3) + 7
        self.thor = (self.competances[3] * 4) + 20
        self.team_force = self.ironman + self.spiderman + self.captain + self.thor

    def input_strength(self):
        """Set the input"""
        for i in range(0, 4):
            get_info = input(
                str("Entrez vos données pour le héro " + self.heroes_name[i] + " : ")
            )
            self.competances[i] = get_info
        print(self.competances)
        return self.competances

    def fight(self):
        """This function simulate the fight of the avengers team \
            in order to know the number of round to take thanos down"""
        while int(self.thanos) > self.team_force:
            # self.competances  = [int(increm) + 1 for increm in self.competances]
            for i in range(0, len(self.competances)):
                self.competances[i] = int(self.competances[i]) + 1
                self.ironman = (int(self.competances[0]) * 3) + 10
                self.spiderman = (int(self.competances[1]) * 4) + 5
                self.captain = (int(self.competances[2]) * 3) + 7
                self.thor = (int(self.competances[3]) * 4) + 20
                self.team_force = (
                    self.ironman + self.spiderman + self.captain + self.thor
                )
                self.round += 1
                # print(self.competances)
                # print(self.team_force)
                if int(self.thanos) < self.team_force:
                    break
        print(self.round)


thanos = input("Quel est la force de thanos : ")
Ave = Avengers(thanos=thanos)
compt = Ave.input_strength()
Ave.fight()
