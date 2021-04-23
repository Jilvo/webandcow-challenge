"""First Easy Challenge: Pierre - Feuille - Ciseaux :
'https://code-challenge.webandcow.com/1/Pierre-Feuille-Ciseaux' 9.38/10 Pylint"""
class PierreFeuilleCiseaux:
    """init class"""
    def __init__(self):
        """init var"""
        self.choice_ia = "CCFCCFCFPCC"
        self.my_choice_list = []

    def main_function(self):
        """Watch in the IA choose rock,paper or scissors"""
        for letter in self.choice_ia:
            if letter == "P":
                self.my_choice_list.append("F")
            elif letter == "F":
                self.my_choice_list.append("C")
            elif letter == "C":
                self.my_choice_list.append("P")
            else:
                break
        print(self.my_choice_list)


pfc = PierreFeuilleCiseaux()
pfc.main_function()
