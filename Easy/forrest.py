"""Easy Challenge: Cours Forrest, Cours ! 
: https://code-challenge.webandcow.com/9/Cours-Forrest-Cours"""
"""5.71/10 Pylint"""


class Runing:
    """Init class"""
    def __init__(self, stop_running):
        """init list"""
        self.kms = [39, 70, 132]
        self.runners = [5, 5, 5]
        self.total = 0

    def how_much(self):
        """Calculate how kms Forrest and his friends run"""
        for i in range(0, len(self.kms)):
            self.total = self.total + (int(stop_running) - int(self.kms[i])) * int(
                self.runners[i]
            )
        self.total += int(stop_running)
        print(self.total)


Course = Runing(10)
stop_running = input("Cbn : ")
Course.how_much()
