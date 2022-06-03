"""Easy Challenge: Chiffrement de mots de passe #1  : https://tainix.fr/challenge/Chiffrement-de-mots-de-passe-1"""


class MotDePasse:
    """Init class"""

    def __init__(self):
        """init list"""
        self.words = [
            "affabule",
            "repentie",
            "copine",
            "terree",
            "sablat",
            "homicide",
            "affermie",
            "machisme",
            "mouchoir",
        ]
        self.crypted_string = ""
        self.keys = [15, 21]

    def encrypter(self):
        for i in self.words:
            new_word = ""
            for j in i:
                pos_in_alphabet = ord(j) - 97
                new_letter = ((self.keys[0] * pos_in_alphabet) + self.keys[1]) % 26
                new_word += str(chr(new_letter + 97))
            self.crypted_string += new_word
            self.crypted_string += "-"
        print(self.crypted_string[:-1])


Code = MotDePasse()
Code.encrypter()
