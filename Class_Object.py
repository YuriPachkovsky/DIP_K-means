class MyObject:
    square = perimeter = compactness = index = claster = elongation = None

    def __init__(self, index, square, perimetr):
        self.index = index
        self.square = square
        self.perimeter = perimetr

    def CalcCompactness(self):
        self.compactness = self.square ** 2 / self.perimeter/ 1000
        # if self.compactness > 31.3:
        #     self.compactness = self.compactness * 200                   #костыль для обнаружения изогнутых фигур
        self.compactness = round(self.compactness, 3)
        return

    def set_claster(self, numb_claster):
        self.claster = numb_claster
        return

    def get_claster(self):
        return self.claster

    def set_elon(self, elon):
        self.elongation = elon
        return