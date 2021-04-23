"""Second Easy Challenge: Coach de foot : https://code-challenge.webandcow.com/3/Coach-de-foot"""
"""/10 Pylint"""
class Football:
    """init class"""
    def __init__(self):
        """init list"""
        self.list_player = []
        self.list_health = []
        self.drap_list = []

    def set_up(self):
        lst = []
        n = int(
            input(
                "Donnez le nombre de joueur que vous souhaitez ajouter \
                    puis écrivez leur état de fatigue   "
            )
        )
        for i in range(0, n):
            ele = int(input())
            lst.append(ele)
        return lst

    def main_function(self, list_player):
        self.drap_list = list_player.copy()
        list_player.sort(reverse=True)
        for a in range(len(list_player)):
            for b in range(len(list_player)):
                if list_player[a] == self.drap_list[b]:
                    self.list_health.append(b)
                else:
                    pass
        for x in range(len(self.list_health), 11, -1):
            del self.list_health[x - 1]
        print(list_player)
        print(self.drap_list)
        print(self.list_health)


foot = Football()
lst = foot.set_up()
foot.main_function(lst)
