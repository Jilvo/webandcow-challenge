
class Pierre_Feuille_Ciseaux():
    def __init__(self):
        self.choice_ia = "CCFCCFCFPCC"
        self.my_choice_list = []

    def main_function(self):
        for letter in self.choice_ia:
            if letter == 'P':
                self.my_choice_list.append("F")
            elif letter == 'F':
                self.my_choice_list.append("C")
            elif letter == 'C':
                self.my_choice_list.append("P")
            else:
                break
        print(self.my_choice_list)        


pfc = Pierre_Feuille_Ciseaux()
pfc.main_function()        