from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:

    def __init__(self, n, m):
        self._n = n
        self._m = m
        self.pole = [[Cell() for _ in range(n)] for _ in range(n)]
        self.init()

    def init(self):
        index_mines = self.good_places()
        # формирование минного поля
        for i in range(self._n):
            for j in range(self._n):
                if [i, j] in index_mines:
                    self.pole[i][j].mine = True
                self.pole[i][j].around_mines = self.how_mines(i, j, index_mines)

    def good_places(self):
        # генерация индексов расположения мин
        index_mines = []
        for i in range(self._m):
            flag = False
            while flag is not True:
                cords = [randint(0, self._n - 1), randint(0, self._n - 1)]
                if cords not in index_mines:
                    index_mines.append(cords)
                    flag = True
        return index_mines

    def how_mines(self, i, j, indexes):
        # счетчик мин в округе
        count = 0
        for k in range(-1, 2):
            for p in range(-1, 2):
                if k == 0 and p == 0:
                    continue
                x, y = i + k, j + p
                if [x, y] in indexes and self._n >= x >= 0 and self._n >= y >= 0:
                    count += 1
        return count

    def show(self):
        tablo = ''
        for x in self.pole:
            for y in x:
                if y.fl_open is True:
                    if y.mine is True:
                        tablo += '* '
                    else:
                        if y.around_mines > 0:
                            tablo += str(y.around_mines) + ' '
                        else:
                            tablo += '. '
                else:
                    tablo += '# '
            tablo += '\n'
        print(tablo)


pole_game = GamePole(10, 12)
pole_game.show()
