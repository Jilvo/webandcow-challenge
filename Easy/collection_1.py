"""Fifth Easy Challenge: Collectionneur-de-figurines : https://code-challenge.webandcow.com/8/Collectionneur-de-figurines"""
"""8.5/10 Pylint"""


class Collection:
    """init class"""
    def __init__(self):
        """init list"""
        self.exemplaires = [
            2000,
            50000,
            500,
            50000,
            2000,
            50000,
            50000,
            50,
            50000,
            2000,
            2000,
            2000,
            50000,
            50000,
            50000,
            50000,
            2000,
        ]
        self.cotes = [
            0.8,
            0.6,
            1.2,
            0.6,
            0.8,
            0.6,
            0.6,
            4,
            1.2,
            1.2,
            1.2,
            1.2,
            0.8,
            0.6,
            1.2,
            0.8,
            1.2,
        ]
        self.sell = []

    def calculate(self):
        """compare diff between buy and sell"""
        for i in range(0, len(self.exemplaires)):
            if self.exemplaires[i] >= 2000:
                calc = (15 * self.cotes[i]) - 15
                print(self.cotes[i])
                self.sell.append(calc)
                print(calc)
            else:
                calc = (30 * self.cotes[i]) - 30
                print(self.cotes[i])
                self.sell.append(calc)
                print(calc)
        print(sum(self.sell))


Pokemon = Collection()
Pokemon.calculate()
