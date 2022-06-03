"""Easy Challenge: Les plaques d’immatriculation #1  : https://tainix.fr/challenge/Les-plaques-d-immatriculation-1"""


class LicencePlate:
    """Init class"""

    def __init__(self):
        """init data"""
        self.plates = [
            "JX-928-XQ",
            "UX-940-AV",
            "KS-567-OU",
            "PF-377-QU",
            "YY-723-RC",
            "OS-738-NZ",
            "QY-919-CB",
            "SB-525-GE",
            "FM-152-DE",
            "BA-623-CN",
            "GO-634-QC",
            "FZ-257-VJ",
            "DI-717-TY",
            "TZ-155-DB",
            "MM-516-MM",
            "WS-582-GG",
            "TM-826-RN",
            "XO-964-DY",
            "OZ-432-TW",
            "VI-839-QK",
            "JE-218-OQ",
            "IB-288-NI",
            "XD-814-DH",
            "ZO-555-OA",
            "PO-040-OP",
            "PE-740-EW",
            "WR-951-AW",
        ]
        self.sum = 0

    def symmetry(self):
        """calculated the score of a list of plates by checking
        symmetry of a plate and summit by power of ten"""
        for i in self.plates:
            start = [i[j] for j in range(0, 4)]
            end = [i[-j] for j in range(1, 5)]
            start.remove("-")
            end.remove("-")
            flag = 0
            for s, e in zip(start, end):
                if s == e:
                    flag += 1
            self.sum += 10**flag
        print("Result", self.sum)


Car = LicencePlate()
Car.symmetry()
