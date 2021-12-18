"""Easy Challenge: Cours Forrest, Cours !  : https://tainix.fr/challenge/Code-Cesar"""


class Cesar:
    """Init class"""
    def __init__(self):
        """init list"""
        self.list_mot = "abcdefghijklmnopqrstuvwxyz"
        self.founded = ""

    def find_pwd(self,pas,pwd):
        for i in pwd:
            pos = self.list_mot.find(str(i))-pas
            if pos < 0 :
                pos = 26 + pos
                print("avant a ",pos)
            self.founded += self.list_mot[pos]
        print(self.founded)

    


Code = Cesar()
Code.find_pwd(4,"hbdcmi")
